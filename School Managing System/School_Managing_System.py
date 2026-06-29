
class Pessoa:
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


class Aluno(Pessoa):
    def __init__(self, nome: str, idade: int, id: int):
        super().__init__(nome, idade, id)
        self._notas = []

    def setNotas(self, nota: float):
        self._notas.append(nota)

    def getNotas(self) -> list:
        return self._notas

    def getMedia(self) -> float:
        media = sum(self._notas) / len(self._notas)
        return media

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

        media = sum(al.getNotas()) / len(al.getNotas())

        if media >= 5:
            print(f"O aluno {al.getNome()} foi aprovado!")
        else:
            print(f"O aluno {al.getNome()} foi reprovado!")

aluno1 = Aluno("Felipe", 17, 1234)
aluno1.setNotas(7)
aluno1.setNotas(6)
aluno1.setNotas(5)
aluno1.setNotas(9)
print(aluno1.getMedia())