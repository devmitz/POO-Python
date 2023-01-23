class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    def dar_like(self):
        self._likes += 1

    @property
    def likes(self):
        return self._likes

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def imprime(self):
        print(f"{self._nome} - {self.duracao}min - {self.ano} - {self._likes} Likes")


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def imprime(self):
        print(f"{self._nome} - {self.temporadas} temporadas - {self.ano} - {self._likes} Likes")


vingadores = Filme("vingadores - guerra infinita", 2018, 160)
interstelar = Filme("interestelar", 2014, 169)

atlanta = Serie("atlanta", 2018, 2)
lost_in_space = Serie("lost in space", 2018, 3)
bones = Serie("bones", 2005, 12)

lista_series_filmes = [vingadores, interstelar, lost_in_space, bones, atlanta]

lost_in_space.dar_like()
lost_in_space.dar_like()
lost_in_space.dar_like()
bones.dar_like()
bones.dar_like()
bones.dar_like()

for programa in lista_series_filmes:
    programa.imprime()

