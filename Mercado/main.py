import os
import json

def clear_screen():
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Linux/Mac
        os.system('clear')

class Produto:
    def __init__(self, id, nome, quantidade, preco):
        self.id = id
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco

    def exibir_produto(self):
        print(f"ID: {self.id} Nome: {self.nome} Quantidade: {self.quantidade} Preço: {self.preco}")

class Mercado:
    last_id = 0
    def __init__(self):
        self.itens = []

    def adicionar_item(self, id, nome, quantidade, preco):
        novo_item = Produto(id, nome, quantidade, preco)
        self.last_id = novo_item.id
        self.itens.append(novo_item)
        return novo_item

    def exibir_estoque(self):
        for item in self.itens:
            item.exibir_produto()

    def adicionar_item_avulso(self, nome, quantidade, preco):
        id = self.last_id + 1
        novo_item = self.adicionar_item(id, nome, quantidade, preco)
        print('')
        print("Produto novo adicionado com sucesso!")
        novo_item.exibir_produto()

mercado = Mercado()

with open('lista.json', 'r', encoding='utf-8') as itens:
    produtos = json.load(itens)
    for produto in produtos:
        mercado.adicionar_item(produto['id'], produto['nome'], produto['quantidade'], produto['preco'])

clear_screen()
while True:
    print('--------------------------------')
    print('######## Mercado Bieger ########')
    print('--------------------------------')
    print('Selecione uma das opções:')
    print('1 - Adicionar produto')
    print('2 - Listar produtos')
    print('3 - Sair')
    print('--------------------------------')

    opcao = input()
    if opcao == "3":
        break

    clear_screen()
    if opcao == "1":
        print("Digite os dados abaixo para adicionar um produto")
        nome = input('Nome do produto: ')
        quant = float(input('Quantidade em estoque: '))
        preco = float(input('Preço do produto: '))
        mercado.adicionar_item_avulso(nome, quant, preco)
    else:
        mercado.exibir_estoque()

    input("Tecle qualquer tela para continuar")
    clear_screen()