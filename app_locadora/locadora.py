import requests
from bs4 import BeautifulSoup
from filme import Filme


class Locadora:
    def __init__(self, url) -> None:
        self.url = url
        self.all_movies = []
        self.html_doc = requests.get(self.url).content
        self.soup = BeautifulSoup(self.html_doc, 'html.parser')
        self._buscar_filme_na_web()
    
    
    def _buscar_filme_na_web(self):
        class_to_find = 'shortcode-featured-title'
        for filme in self.soup.find_all('div', attrs={'class':class_to_find}):
            id, titulo, diretor, ano = Filme.find_info(filme.text)
            novo_filme = Filme(id, titulo, diretor, ano)
            self.all_movies.append(novo_filme)


    def _print_filme(self, filme: Filme):
        string_formatada = '/'.join(map(str, filme.ano))
        print(f'- {filme.titulo} ({string_formatada}), de {filme.diretor}')


    def catalogo(self):
        print('\nCatálogo:')
        for filme in self.all_movies:
            self._print_filme(filme)
    

    def filmes_anteriores(self, ano: int):
        print(f'\nFilmes lançados antes de {ano}:\n')
        for filme in self.all_movies:
            if filme.ano[0] < ano:
                self._print_filme(filme)

    def filmes_posteriores(self, ano: int):
        print(f'\nFilmes lançados após {ano}:\n')
        for filme in self.all_movies:
            if filme.ano[0] > ano:
                self._print_filme(filme)