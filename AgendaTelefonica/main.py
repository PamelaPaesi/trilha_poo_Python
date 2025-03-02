class Contato:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

    def __repr__(self):
        return f"Nome: {self.nome} Telefone: {self.telefone}"
class AgendaTelefonica:
    def __init__(self):
        self.contatos = []
    def adicionar_contato(self, contato):
        pessoa = self.busca_contato(contato.nome)
        if not pessoa:
            self.contatos.append(contato)
            print("Contato adicionado com sucesso!")
        else:
            if contato.nome == pessoa.nome and contato.telefone == pessoa.telefone:
                print("Contato já existe!")
            else:
                self.contatos.append(contato)
                print("Contato adicionado com sucesso!")
    def remove_contato(self, nome):
        remover = self.busca_contato(nome)
        if remover:
            self.contatos.remove(remover)
            print(f"{nome} removido!")
        else:
            print(f"{nome} não encontrado!")
    def busca_contato(self, nome):
        for contato in self.contatos:
            if contato.nome == nome:
                return contato
    def atualizar_cadastro(self, nome, novo_contato):
        contato_antigo = self.busca_contato(nome)
        if contato_antigo:
            self.contatos.remove(contato_antigo)
            self.contatos.append(novo_contato)
            print("Contato atualizado!")
        else:
            print("Contato não encontrado.")
    def listar_contatos(self):
        if self.contatos:
            for contato in self.contatos:
                print(contato)
        else:
            print("Agenda sem nenhum contato!")

agenda = AgendaTelefonica()

operacao = ''
while(operacao != '6'):
    print("Bem vindo a sua agenda!!!\n")
    print("1 - Adicionar contato")
    print("2 - Remover contato")
    print("3 - Buscar contato")
    print("4 - Atualizar contato")
    print("5 - Listar contatos\n")
    print("6 - Sair do programa")

    operacao = input("Escolha uma das opções: ")
    if operacao == '6':
        break

    match operacao:
        case '1':
            nome = input("Digite um nome: ")
            telefone = input("Digite o telefone: ")
            contato = Contato(nome,telefone)
            agenda.adicionar_contato(contato)
        case '2':
            nome = input("Informe o nome a ser removido: ")
            agenda.remove_contato(nome)
        case '3':
            nome = input("Informe o nome a ser pesquisado: ")
            contato = agenda.busca_contato(nome)
            if contato:
                print(contato)
            else:
                print("Contato não encontrado")
        case '4':
            nome_antigo = input("Informe o contato a ser atualizado: ")
            nome = input("Digite um nome: ")
            telefone = input("Digite o telefone: ")
            contato = Contato(nome,telefone)
            agenda.atualizar_cadastro(nome_antigo, contato)
        case '5':
            agenda.listar_contatos()

    input("Pressione qualquer tecla para continuar .....")

