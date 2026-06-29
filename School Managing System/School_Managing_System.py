from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome: str, idade: int, id: int):
        self._nome = nome
        self._idade = idade
        self._id = id

    def getNome(self):
        return self._nome

    def getIdade(self):
        return self._idade

    def getId(self):
        return self._id

    def setNome(self, nome):
        self._nome = nome

    def setIdade(self, idade):
        self._idade = idade

    def setId(self, id):
        self._id = id

    @abstractmethod
    def printAttributes(self):
        print(f"Nome: {self._nome}\n"
              f"Idade: {self._idade}\n"
              f"Id: {self._id}.")

class Aluno(Pessoa):
    def __init__(self, nome: str, idade: int, id: int):
        super().__init__(nome, idade, id)
        self._notas = []

    def setNotas(self, nota: float):
        self._notas.append(nota)

    def getNotas(self) -> list:
        return self._notas

    def getMedia(self) -> float:
        if not self._notas:
            return 0
        return sum(self._notas) / len(self._notas)

    def printAttributes(self):
        super().printAttributes()
        for i, nota in enumerate(self._notas, start=1):
            print(f"Nota {i}: {nota}")
        print(f"Media do aluno: {self.getMedia()}")

class Professor(Pessoa):
    def __init__(self, nome: str, idade: int, id: int,
                 salario: float, graduacao: str):
        super().__init__(nome, idade, id)
        self._salario = salario
        self._graduacao = graduacao

    def getSalario(self):
        return self._salario

    def setSalario(self, salario):
        self._salario = salario

    def getGraduacao(self):
        return self._graduacao

    def setGraduacao(self, graduacao):
        self._graduacao = graduacao

    def aprovar_ou_reprovar(self, al: "Aluno"):
        if len(al.getNotas()) == 0:
            print(f"{al.getNome()} não possui notas.")
            return

        if al.getMedia() >= 5:
            print(f"O(a) professor(a) {Professor.getNome()} aprovou o aluno {al.getNome()}!")
        else:
            print(f"O(a) professor(a) {Professor.getNome()} reprovou o aluno {al.getNome()}!")

    def printAttributes(self):
        super().printAttributes()
        print(f"Salário: {self._salario}\n"
              f"Graduação: {self._graduacao}\n")


aluno1 = Aluno("Felipe", 17, 1234)
aluno1.setNotas(7)
aluno1.setNotas(6)
aluno1.setNotas(5)
aluno1.setNotas(9)
aluno1.printAttributes()

print()

aluno2 = Aluno("Laura", 16, 1235)
aluno2.setNotas(8)
aluno2.setNotas(8)
aluno2.setNotas(9)
aluno2.setNotas(10)
aluno2.printAttributes()

print()

professor1 = Professor("Carlos", 67, 25, 4_569.34, 'Mestrado Em Letras e em Filosofia')
professor1.printAttributes()

print()

print(f'Média Felipe: {aluno1.getMedia()}')
professor1.aprovar_ou_reprovar(aluno1)

print()

print(f'Média Laura: {aluno2.getMedia()}')
professor1.aprovar_ou_reprovar(aluno2)
