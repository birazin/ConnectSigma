import json
import re
import os

DATA_DIR = os.path.join(os.path.dirname(__file__), "dados")


class Cliente:
    def __init__(self, cpf, nome, endereco, telefone_residencial, celular, renda):
        self.cpf = cpf
        self.nome = nome
        self.endereco = endereco
        self.telefone_residencial = telefone_residencial
        self.celular = celular
        self.renda = renda

    def to_dict(self):
        return self.__dict__

class ClienteManager:
    FILENAME = os.path.join(DATA_DIR, "clientes.json")

    @staticmethod
    def validar_cpf(cpf):
        return re.match(r"\d{11}", cpf) is not None  # CPF deve ter 11 dígitos 

    @staticmethod
    def carregar_clientes():
        try:
            with open(ClienteManager.FILENAME, "r") as file:
                return [Cliente(**dados) for dados in json.load(file)]
        except FileNotFoundError:
            return []

    @staticmethod
    def salvar_clientes(clientes):
        os.makedirs(DATA_DIR, exist_ok=True)  
        with open(ClienteManager.FILENAME, "w") as file:
            json.dump([cliente.to_dict() for cliente in clientes], file, indent=4)

    def adicionar_cliente(self, cpf, nome, endereco, telefone_residencial, celular, renda):
        if not self.validar_cpf(cpf):
            print("CPF inválido.")
            return
        clientes = self.carregar_clientes()
        if any(cliente.cpf == cpf for cliente in clientes):
            print("CPF já cadastrado.")
            return
        cliente = Cliente(cpf, nome, endereco, telefone_residencial, celular, renda)
        clientes.append(cliente)
        self.salvar_clientes(clientes)
        print("Cliente adicionado com sucesso!")

    def buscar_cliente(self, cpf):
        clientes = self.carregar_clientes()
        for cliente in clientes:
            if cliente.cpf == cpf:
                return cliente
        print("Cliente não encontrado.")
        return None

    def listar_clientes(self):
        clientes = self.carregar_clientes()
        clientes.sort(key=lambda x: x.nome)
        for cliente in clientes:
            print(cliente.to_dict())
