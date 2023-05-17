from random import randint


class Aluno:
    def __init__(self, nome, senha):
        self.nome = nome
        self._senha = senha
        self.matricula = randint(0, 1000000)
        print('-' * 50)
        print(f'Aluno (a): {self.nome}\nMatrícula: {self.matricula}\nSenha: propriedade protegida...\n')


class Disciplina:
    def __init__(self, nome):
        self.nome = nome
        self.alunos = [
            [],
            [],
            []
        ]

    def matricular(self, aluno):
        self.alunos[0].append(aluno)
        self.alunos[1].append(10)
        self.alunos[2].append(10)
        self.alunos[1].append(3)
        self.alunos[2].append(4)

    def listar_alunos(self):
        for x in range(len(self.alunos[0])):
            print(f'Aluno (a): {self.alunos[0][x].nome} | N1: {self.alunos[1][x]} | N2: {self.alunos[2][x]}')


p1 = Aluno("Amanda", "senha123")
p2 = Aluno("Ariza", "senha234")
d1 = Disciplina("POO")
d1.matricular(p1)
d1.matricular(p2)
print(d1.nome)
d1.listar_alunos()
