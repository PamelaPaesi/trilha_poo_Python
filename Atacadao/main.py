import csv

class Produto:
    def __init__(self, id, nome, preco):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.total = 0.00
        self.subtotal = 0.00
        self.quantidade = 0.00

    def __repr__(self):
        return f'Id: {self.id} - {self.nome} = R$ {float(self.preco):.2f}'

class EstoqueAtacado:
    def __init__(self):
        self.produtos = []

    def adicionar_item(self, id, nome, preco):
        novo_item = Produto(id, nome, float(preco))
        self.produtos.append(novo_item)

    def imprimir_produtos(self):
        print("\nExibir o catalogo dos produtos:\n")
        for prod in self.produtos:
            print(prod)

class Venda:
    def __init__(self, tipo):
        self.tipo = tipo
        self.produtos = []
        self.subtotal = 0
        self.total = 0

    def calcular_desconto(self, produto):
        percent = 1.00
        if (produto.quantidade > 25):
            percent = 0.75
        elif (produto.quantidade > 15):
            percent = 0.80
        elif (produto.quantidade > 5):
            percent = 0.90
        produto.total = produto.preco * produto.quantidade
        produto.subtotal = percent * produto.total

    def adicionar_produto(self, produto):
        self.calcular_desconto(produto)
        self.produtos.append(produto)
        self.subtotal += produto.subtotal

    def calcular_total(self):
        if (self.tipo == 'dinheiro'):
            self.total = self.subtotal * 0.95
        elif (self.tipo == 'credito'):
            self.total = self.subtotal * 1.03
        else:
            self.total = self.subtotal
    def imprimir_venda(self):
        print(f"Venda tipo: {self.tipo}")
        for prod in self.produtos:
            print(f"{prod.nome} - R$ {prod.preco:.2f} x {prod.quantidade:.2f} \n"
                  f"          Total: R$ {prod.total} Subtotal: R$ {prod.subtotal:.2f}")
        self.calcular_total()

        print("-------------------")
        print(f"Subtotal: R$ {self.subtotal:.2f}")
        print(f"Total:    R$ {self.total:.2f}\n")

class CaixaDoAtacado:
    def __init__(self):
        self.vendas = []
        self.estoque = EstoqueAtacado()
        self.venda = None

    def iniciar_venda(self, tipo):
        self.venda = Venda(tipo)

    def adicionar_item(self, id_produto, quantidade):
        produto = next((p for p in self.estoque.produtos if p.id == id_produto), None)
        if produto:
            produto.quantidade = quantidade
            self.venda.adicionar_produto(produto)
        else:
            print(f"Produto com ID {id_produto} não encontrado.")

    def finalizar_venda(self):
        if (self.venda != None):
            self.vendas.append(self.venda)

caixa = CaixaDoAtacado()
# Importa os produtos
with open('produtos.csv', mode='r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    for index, row in enumerate(csv_reader):
        if index > 0:
            caixa.estoque.adicionar_item(int(row[0]), row[1], row[2])

# Importa as vendas
with open('vendas.csv', mode='r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        if len(row) == 1:
            caixa.finalizar_venda()
            caixa.iniciar_venda(row[0])
        else:
            caixa.adicionar_item(int(row[0]), float(row[1]))
    caixa.finalizar_venda()

for venda in caixa.vendas:
    venda.imprimir_venda()
