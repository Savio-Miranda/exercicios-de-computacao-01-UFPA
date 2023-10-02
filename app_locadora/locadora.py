import requests
from bs4 import BeautifulSoup
from filme import Filme

'''
    Alguns breves comentários sobre as bibliotecas usadas nesse programa...

    A biblioteca requests permite que o programador possa utilizar os métodos HTTP da Web.
    O método GET usado em um link http é equivalente ao acesso desse link dando enter no browser.
    Neste caso, estamos usando o método GET para acessar o link que contém a lista de filmes que estamos interessados.
    
    Já o beautifulsoup é uma biblioteca de webscrapping que permite o programador buscar em bloco de texto HTML
    as informações que ele desejar. Assim, a gente usa essas duas bibliotecas em conjunto:
        1 - A requests dá um get no nosso link (chamamos de URL) e coleta o texto em formato HTML da página.
        2 - Então o beautifulsoup vai vasculhar nesse texto as informações que nós queremos.
'''

class Locadora:
    '''
    Uma classe que utiliza a dataclass Filme criada no arquivo filme.py para mostrar ao usuário
    um catálago de todos os filmes nessa URL e filmes anteriores e posteriores a um determinado ano.
    '''
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