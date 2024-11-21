import json
import os

DATA_DIR = os.path.join(os.path.dirname(__file__), "dados")


class Veiculo:
    def __init__(self, chassi, placa, marca, modelo, ano_fabricacao, ano_modelo, cor, valor):
        self.chassi = chassi
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.ano_fabricacao = ano_fabricacao
        self.ano_modelo = ano_modelo
        self.cor = cor
        self.valor = valor

    def to_dict(self):
        return self.__dict__

class VeiculoManager:
    FILENAME = os.path.join(DATA_DIR, "veiculos.json")

    @staticmethod
    def carregar_veiculos():
        try:
            with open(VeiculoManager.FILENAME, "r") as file:
                return [Veiculo(**dados) for dados in json.load(file)]
        except FileNotFoundError:
            return []

    @staticmethod
    def salvar_veiculos(veiculos):
        os.makedirs(DATA_DIR, exist_ok=True)
        with open(VeiculoManager.FILENAME, "w") as file:
            json.dump([veiculo.to_dict() for veiculo in veiculos], file, indent=4)

    def adicionar_veiculo(self, chassi, placa, marca, modelo, ano_fabricacao, ano_modelo, cor, valor):
        veiculos = self.carregar_veiculos()
        if any(v.chassi == chassi for v in veiculos):
            print("Veículo com esse número de chassi já cadastrado.")
            return
        veiculo = Veiculo(chassi, placa, marca, modelo, ano_fabricacao, ano_modelo, cor, valor)
        veiculos.append(veiculo)
        self.salvar_veiculos(veiculos)
        print("Veículo adicionado com sucesso!")

    def listar_veiculos(self):
        veiculos = self.carregar_veiculos()
        veiculos.sort(key=lambda x: (x.marca, x.modelo))
        for veiculo in veiculos:
            print(veiculo.to_dict())
