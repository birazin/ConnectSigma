import json
import os

DATA_DIR = "dados"

class Montadora:
    def __init__(self, cnpj, razao_social, marca, contato, telefone_comercial, celular):
        self.cnpj = cnpj
        self.razao_social = razao_social
        self.marca = marca
        self.contato = contato
        self.telefone_comercial = telefone_comercial
        self.celular = celular

    def to_dict(self):
        return vars(self)


class MontadoraManager:
    FILENAME = os.path.join(DATA_DIR, "montadoras.json")

    @staticmethod
    def carregar_montadoras():
        try:
            with open(MontadoraManager.FILENAME, "r") as file:
                return [Montadora(**dados) for dados in json.load(file)]
        except FileNotFoundError:
            return []

    @staticmethod
    def salvar_montadoras(montadoras):
        os.makedirs(DATA_DIR, exist_ok=True)
        with open(MontadoraManager.FILENAME, "w") as file:
            json.dump([montadora.to_dict() for montadora in montadoras], file, indent=4)

    def adicionar_montadora(self, cnpj, razao_social, marca, contato, telefone_comercial, celular):
        montadoras = self.carregar_montadoras()
        montadora = Montadora(cnpj, razao_social, marca, contato, telefone_comercial, celular)
        montadoras.append(montadora)
        self.salvar_montadoras(montadoras)
        print("Montadora registrada com sucesso!")

    def listar_montadoras(self):
        montadoras = self.carregar_montadoras()
        if not montadoras:
            print("Nenhuma montadora registrada.")
            return

        print("\n=== Lista de Montadoras ===")
        for montadora in montadoras:
            print(f"{montadora.razao_social} (CNPJ: {montadora.cnpj}), Marca: {montadora.marca}, Contato: {montadora.contato}")
