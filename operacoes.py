import json
import os
from datetime import datetime

DATA_DIR = "dados"

class Operacao:
    def __init__(self, numero, data, cliente, vendedor, veiculo, tipo, valor=None, valor_entrada=None, valor_financiado=None, valor_total=None):
        self.numero = numero
        self.data = data
        self.cliente = cliente
        self.vendedor = vendedor
        self.veiculo = veiculo
        self.tipo = tipo  # 'compra' ou 'venda'

        if tipo == 'venda':
            self.valor_entrada = valor_entrada
            self.valor_financiado = valor_financiado
            self.valor_total = valor_total
        else:
            self.valor = valor

    def to_dict(self):
        if self.tipo == 'venda':
            return {
                'numero': self.numero,
                'data': self.data,
                'cliente': self.cliente,
                'vendedor': self.vendedor,
                'veiculo': self.veiculo,
                'valor_entrada': self.valor_entrada,
                'valor_financiado': self.valor_financiado,
                'valor_total': self.valor_total,
                'tipo': self.tipo
            }
        else:
            return {
                'numero': self.numero,
                'data': self.data,
                'cliente': self.cliente,
                'vendedor': self.vendedor,
                'veiculo': self.veiculo,
                'valor': self.valor,
                'tipo': self.tipo
            }


class OperacaoManager:
    FILENAME = os.path.join(DATA_DIR, "operacoes.json")

    @staticmethod
    def carregar_operacoes():
        try:
            with open(OperacaoManager.FILENAME, "r") as file:
                operacoes_dados = json.load(file)
                operacoes = []
                for dados in operacoes_dados:
                    if dados["tipo"] == "compra":
                        operacoes.append(Operacao(
                            numero=dados["numero"],
                            data=dados["data"],
                            cliente=dados["cliente"],
                            vendedor=dados["vendedor"],
                            veiculo=dados["veiculo"],
                            tipo=dados["tipo"],
                            valor=dados["valor"]
                        ))
                    elif dados["tipo"] == "venda":
                        operacoes.append(Operacao(
                            numero=dados["numero"],
                            data=dados["data"],
                            cliente=dados["cliente"],
                            vendedor=dados["vendedor"],
                            veiculo=dados["veiculo"],
                            tipo=dados["tipo"],
                            valor_entrada=dados["valor_entrada"],
                            valor_financiado=dados["valor_financiado"],
                            valor_total=dados["valor_total"]
                        ))
                return operacoes
        except FileNotFoundError:
            return []

    @staticmethod
    def salvar_operacoes(operacoes):
        os.makedirs(DATA_DIR, exist_ok=True)
        with open(OperacaoManager.FILENAME, "w") as file:
            json.dump([operacao.to_dict() for operacao in operacoes], file, indent=4)

    def adicionar_operacao(self, numero, cliente, vendedor, veiculo, tipo, valor=None, valor_entrada=None, valor_financiado=None, valor_total=None):
        operacoes = self.carregar_operacoes()
        data = datetime.now().strftime("%Y-%m-%d")
        operacao = Operacao(numero, data, cliente, vendedor, veiculo, tipo, valor, valor_entrada, valor_financiado, valor_total)
        operacoes.append(operacao)
        self.salvar_operacoes(operacoes)
        print(f"Operação de {tipo} registrada com sucesso!")

    def listar_operacoes(self):
        operacoes = self.carregar_operacoes()
        if not operacoes:
            print("Nenhuma operação registrada.")
            return

        print("\n=== Lista de Operações ===")
        for operacao in operacoes:
            if operacao.tipo == "compra":
                print(f"Compra #{operacao.numero}: Cliente {operacao.cliente}, Veículo {operacao.veiculo}, Valor: R$ {operacao.valor}")
            elif operacao.tipo == "venda":
                print(f"Venda #{operacao.numero}: Cliente {operacao.cliente}, Veículo {operacao.veiculo}, Entrada: R$ {operacao.valor_entrada}, Financiado: R$ {operacao.valor_financiado}, Total: R$ {operacao.valor_total}")
