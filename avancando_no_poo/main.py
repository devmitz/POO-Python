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


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas


vingadores = Filme("vingadores - guerra infinita", 2018, 160)
interstelar = Filme("interestelar", 2014, 169)

atlanta = Serie("atlanta", 2018, 2)
lost_in_space = Serie("lost in space", 2018, 3)
bones = Serie("bones", 2005, 12)

print("================================Filmes================================")
print(f"Nome: {vingadores.nome} - {vingadores.ano} - {vingadores.duracao}min : {vingadores.likes}")
print(f"Nome: {interstelar.nome} - {interstelar.ano} - {interstelar.duracao}min : {interstelar.likes}")
print("================================Series================================")
print(f"Nome: {atlanta.nome} - {atlanta.ano} - {atlanta.temporadas} : {atlanta.likes}")
print(f"Nome: {lost_in_space.nome} - {lost_in_space.ano} - {lost_in_space.temporadas} : {lost_in_space.likes}")
print(f"Nome: {bones.nome} - {bones.ano} - {bones.temporadas} : {bones.likes}")
