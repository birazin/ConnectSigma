import json
import os

DATA_DIR = os.path.join(os.path.dirname(__file__), "dados")


class Vendedor:
    def __init__(self, codigo, usuario):
        self.codigo = codigo
        self.usuario = usuario

    def to_dict(self):
        return self.__dict__

class VendedorManager:
    FILENAME = os.path.join(DATA_DIR, "vendedores.json")

    @staticmethod
    def carregar_vendedores():
        try:
            with open(VendedorManager.FILENAME, "r") as file:
                return [Vendedor(**dados) for dados in json.load(file)]
        except FileNotFoundError:
            return []

    @staticmethod
    def salvar_vendedores(vendedores):
        os.makedirs(DATA_DIR, exist_ok=True)
        with open(VendedorManager.FILENAME, "w") as file:
            json.dump([vendedor.to_dict() for vendedor in vendedores], file, indent=4)

    def adicionar_vendedor(self, codigo, usuario):
        vendedores = self.carregar_vendedores()
        if any(v.codigo == codigo for v in vendedores):
            print("Código de vendedor já cadastrado.")
            return
        vendedor = Vendedor(codigo, usuario)
        vendedores.append(vendedor)
        self.salvar_vendedores(vendedores)
        print("Vendedor adicionado com sucesso!")

    def listar_vendedores(self):
        vendedores = self.carregar_vendedores()
        for vendedor in vendedores:
            print(vendedor.to_dict())
