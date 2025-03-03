class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

class Aluno:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

class Biblioteca:
    def __init__(self):
        self.livros = []
        self.alunos = []

    def busca_livro(self, titulo, autor):
        for livro in self.livros:
            if livro.titulo == titulo and livro.autor == autor:
                return livro

    def busca_aluno(self, nome):
        for aluno in self.alunos:
            if aluno.nome == nome:
                return aluno

    def adicionar_livro(self, titulo, autor):
        encontrou = self.busca_livro(titulo, autor)
        if encontrou:
            raise Exception("Livro já cadastrado")
        else:
            livro = Livro(titulo, autor)
            self.livros.append(livro)
            print("Livro adicionado com sucesso")

    def cadastra_aluno(self, nome, telefone):
        encontrou = self.busca_aluno(nome)
        if encontrou:
            raise Exception("Aluno já cadastrado!")
        else:
            aluno = Aluno(nome, telefone)
            self.alunos.append(aluno)
            print("Aluno cadastrado com sucesso!")

    def empresta_livro(self, titulo, autor, nome):
        livro = self.busca_livro(titulo, autor)
        if not livro:
            raise Exception("Livro não encontrado.")
        else:
            if not livro.disponivel:
                raise Exception(f"Livro não disponível, foi emprestado para o {livro.aluno.nome}")
            else:
                aluno = self.busca_aluno(nome)
                if not aluno:
                    raise Exception("Aluno não cadastrado.")
                else:
                    livro.disponivel = False
                    livro.aluno = aluno
                    print("Livro emprestado!!!")

    def devolver_livro(self, titulo, autor):
        livro = self.busca_livro(titulo, autor)
        if not livro:
            raise Exception("Livro não consta no sistema.")
        else:
            if livro.disponivel:
                raise Exception("Livro não foi emprestado.")
            else:
                livro.disponivel = True
                livro.aluno = None
                print("Livro devolvido.")

def main():
    biblioteca = Biblioteca()

    try:
        biblioteca.adicionar_livro("Os criminosos vieram para o chá", "Stella.Carr")
        biblioteca.adicionar_livro("Os criminosos vieram para o chá", "Stella.Carr")
    except Exception as e:
        print(e)

    try:
        biblioteca.cadastra_aluno("José", "123")
        biblioteca.cadastra_aluno("José", "123")
    except Exception as e:
        print(e)

    try:
        biblioteca.empresta_livro("Os criminosos vieram para o chá", "Stella.Carr", "José")
        biblioteca.empresta_livro("Os criminosos vieram para o chá", "Stella.Carr", "José")
    except Exception as e:
        print(e)

    try:
        biblioteca.adicionar_livro("Dexter: é delicioso", "Jeff Lindsay")
        biblioteca.empresta_livro("Dexter: é delicioso", "Jeff Lindsay", "Maria")
    except Exception as e:
        print(e)

    try:
        biblioteca.empresta_livro("Duplo Dexter", "Jeff Lindsay", "José")
    except Exception as e:
        print(e)

    try:
        biblioteca.devolver_livro("Os criminosos vieram para o chá", "Stella.Carr")
        biblioteca.devolver_livro("Os criminosos vieram para o chá", "Stella.Carr")
    except Exception as e:
        print(e)

    try:
        biblioteca.devolver_livro("Duplo Dexter", "Jeff Lindsay")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()