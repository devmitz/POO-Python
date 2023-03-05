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

    def __str__(self):
        return f"{self._nome} - {self.duracao}min - {self.ano} - {self._likes} Likes"


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f"{self._nome} - {self.temporadas} temporadas - {self.ano} - {self._likes} Likes"


class Playlist(list):
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    @property
    def listagem(self):
        return self._programas

    @property
    def tamanho(self):
        return len(self._programas)

vingadores = Filme("vingadores - guerra infinita", 2018, 160)
interstelar = Filme("interestelar", 2014, 169)

atlanta = Serie("atlanta", 2018, 2)
bones = Serie("bones", 2005, 12)
lost_in_space = Serie("lost in space", 2018, 3)

lista_series_filmes = [interstelar, lost_in_space, bones, vingadores, atlanta]

interstelar.dar_like()
interstelar.dar_like()
interstelar.dar_like()
interstelar.dar_like()
lost_in_space.dar_like()
lost_in_space.dar_like()
lost_in_space.dar_like()
bones.dar_like()
bones.dar_like()
bones.dar_like()

playlist_fim_de_semana = Playlist("fim de semana", lista_series_filmes)

print(f"tamanho da playlist: {len(playlist_fim_de_semana)} ")

for programa in playlist_fim_de_semana.listagem:
    print(programa)

print(f"Tá ou não tá? {interstelar in playlist_fim_de_semana}")
