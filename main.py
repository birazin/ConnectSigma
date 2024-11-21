from datetime import datetime
import json
import os

from clientes import ClienteManager
from veiculos import VeiculoManager
from vendedores import VendedorManager
from operacoes import OperacaoManager
from pedidos import PedidoManager
from montadoras import MontadoraManager

def menu_clientes():
    cliente_manager = ClienteManager()
    while True:
        print("\n--- Menu Clientes ---")
        print("1. Adicionar Cliente")
        print("2. Listar Clientes")
        print("3. Voltar ao Menu Principal")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cpf = input("CPF: ")
            nome = input("Nome: ")
            endereco = input("Endereço (bairro, cidade, estado): ")
            telefone_residencial = input("Telefone residencial: ")
            celular = input("Celular: ")
            renda = float(input("Renda: "))
            cliente_manager.adicionar_cliente(cpf, nome, endereco, telefone_residencial, celular, renda)
        elif opcao == "2":
            cliente_manager.listar_clientes()
        elif opcao == "3":
            break
        else:
            print("Opção inválida.")

def menu_veiculos():
    veiculo_manager = VeiculoManager()
    while True:
        print("\n--- Menu Veículos ---")
        print("1. Adicionar Veículo")
        print("2. Listar Veículos")
        print("3. Voltar ao Menu Principal")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            chassi = input("Número do chassi: ")
            placa = input("Placa: ")
            marca = input("Marca: ")
            modelo = input("Modelo: ")
            ano_fabricacao = input("Ano de fabricação: ")
            ano_modelo = input("Ano do modelo: ")
            cor = input("Cor: ")
            valor = float(input("Valor: "))
            veiculo_manager.adicionar_veiculo(chassi, placa, marca, modelo, ano_fabricacao, ano_modelo, cor, valor)
        elif opcao == "2":
            veiculo_manager.listar_veiculos()
        elif opcao == "3":
            break
        else:
            print("Opção inválida.")

def menu_vendedores():
    vendedor_manager = VendedorManager()
    while True:
        print("\n--- Menu Vendedores ---")
        print("1. Adicionar Vendedor")
        print("2. Listar Vendedores")
        print("3. Voltar ao Menu Principal")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            codigo = input("Código do vendedor: ")
            usuario = input("Nome do usuário: ")
            vendedor_manager.adicionar_vendedor(codigo, usuario)
        elif opcao == "2":
            vendedor_manager.listar_vendedores()
        elif opcao == "3":
            break
        else:
            print("Opção inválida.")

def menu_operacoes():
    operacao_manager = OperacaoManager()
    while True:
        print("\n=== Menu Operações ===")
        print("1. Registrar Compra")
        print("2. Registrar Venda")
        print("3. Listar Operações")
        print("4. Voltar ao Menu Principal")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            numero = input("Número da operação: ")
            cliente = input("CPF do cliente: ")
            vendedor = input("Código do vendedor: ")
            veiculo = input("Modelo do veículo: ")
            valor = float(input("Valor da compra: "))
            operacao_manager.adicionar_operacao(numero, cliente, vendedor, veiculo, "compra", valor=valor)

        elif opcao == "2":
            numero = input("Número da operação: ")
            cliente = input("CPF do cliente: ")
            vendedor = input("Código do vendedor: ")
            veiculo = input("Modelo do veículo: ")
            valor_entrada = float(input("Valor de entrada: "))
            valor_financiado = float(input("Valor financiado: "))
            valor_total = valor_entrada + valor_financiado
            operacao_manager.adicionar_operacao(
                numero, cliente, vendedor, veiculo, "venda", valor_entrada=valor_entrada, 
                valor_financiado=valor_financiado, valor_total=valor_total
            )

        elif opcao == "3":
            operacao_manager.listar_operacoes()

        elif opcao == "4":
            break

        else:
            print("Opção inválida.")


def menu_montadoras():
    montadora_manager = MontadoraManager()
    while True:
        print("\n=== Menu Montadoras ===")
        print("1. Adicionar Montadora")
        print("2. Listar Montadoras")
        print("3. Voltar ao Menu Principal")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cnpj = input("CNPJ: ")
            razao_social = input("Razão Social: ")
            marca = input("Marca: ")
            contato = input("Nome do contato: ")
            telefone_comercial = input("Telefone comercial: ")
            celular = input("Celular: ")
            montadora_manager.adicionar_montadora(cnpj, razao_social, marca, contato, telefone_comercial, celular)

        elif opcao == "2":
            montadora_manager.listar_montadoras()

        elif opcao == "3":
            break

        else:
            print("Opção inválida.")


def menu_pedidos():
    pedido_manager = PedidoManager()
    while True:
        print("\n=== Menu Pedidos ===")
        print("1. Registrar Pedido")
        print("2. Listar Pedidos")
        print("3. Voltar ao Menu Principal")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            numero = input("Número do pedido: ")
            data = input("Data (dd/mm/aaaa): ")
            cliente = input("CPF do cliente: ")
            vendedor = input("Código do vendedor: ")
            montadora = input("CNPJ da montadora: ")
            modelo = input("Modelo do veículo: ")
            ano = input("Ano de fabricação: ")
            cor = input("Cor do veículo: ")
            acessorios = input("Acessórios do veículo: ")
            valor = float(input("Valor total do pedido: "))
            pedido_manager.registrar_pedido(numero, data, cliente, vendedor, montadora, modelo, ano, cor, acessorios, valor)

        elif opcao == "2":
            pedido_manager.listar_pedidos()

        elif opcao == "3":
            break

        else:
            print("Opção inválida.")

def main():
    while True:
        print("\n=== Menu Principal ===")
        print("1. Gerenciar Clientes")
        print("2. Gerenciar Veículos")
        print("3. Gerenciar Vendedores")
        print("4. Gerenciar Operações")
        print("5. Gerenciar Montadoras")
        print("6. Gerenciar Pedidos")
        print("7. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            menu_clientes()

        elif opcao == "2":
            menu_veiculos()

        elif opcao == "3":
            menu_vendedores()

        elif opcao == "4":
            menu_operacoes()

        elif opcao == "5":
            menu_montadoras()

        elif opcao == "6":
            menu_pedidos()

        elif opcao == "7":
            print("Encerrando o programa...")
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
