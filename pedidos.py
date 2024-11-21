import json
import os

DATA_DIR = "dados"

class Pedido:
    def __init__(self, numero, data, cliente, vendedor, montadora, modelo, ano, cor, acessorios, valor):
        self.numero = numero
        self.data = data
        self.cliente = cliente
        self.vendedor = vendedor
        self.montadora = montadora
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.acessorios = acessorios
        self.valor = valor

    def to_dict(self):
        return vars(self)


class PedidoManager:
    FILENAME = os.path.join(DATA_DIR, "pedidos.json")

    @staticmethod
    def carregar_pedidos():
        try:
            with open(PedidoManager.FILENAME, "r") as file:
                return [Pedido(**dados) for dados in json.load(file)]
        except FileNotFoundError:
            return []

    @staticmethod
    def salvar_pedidos(pedidos):
        os.makedirs(DATA_DIR, exist_ok=True)
        with open(PedidoManager.FILENAME, "w") as file:
            json.dump([pedido.to_dict() for pedido in pedidos], file, indent=4)

    def registrar_pedido(self, numero, data, cliente, vendedor, montadora, modelo, ano, cor, acessorios, valor):
        pedidos = self.carregar_pedidos()
        pedido = Pedido(numero, data, cliente, vendedor, montadora, modelo, ano, cor, acessorios, valor)
        pedidos.append(pedido)
        self.salvar_pedidos(pedidos)
        print("Pedido registrado com sucesso!")

    def listar_pedidos(self):
        pedidos = self.carregar_pedidos()
        if not pedidos:
            print("Nenhum pedido registrado.")
            return

        print("\n=== Lista de Pedidos ===")
        for pedido in pedidos:
            print(f"Pedido #{pedido.numero}: Modelo {pedido.modelo}, Ano {pedido.ano}, Cor {pedido.cor}, Valor: R$ {pedido.valor}")
