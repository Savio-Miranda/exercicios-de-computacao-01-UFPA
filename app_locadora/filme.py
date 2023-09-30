import re
from dataclasses import dataclass

'''
    A biblioteca requests permite que o programador possa utilizar os métodos HTTP da Web.
    O método GET usado em um link http é equivalente ao acesso desse link dando enter no browser.
    
    Já o beautifulsoup é uma biblioteca de webscrapping que permite o programador buscar em bloco de texto
    as informações que ele desejar. Assim, a gente usa essas duas bibliotecas em conjunto:
        1 - A requests dá um get no nosso link (chamamos de URL) e coleta o texto em formato HTML da página.
        2 - Então o beautifulsoup vai vasculhar nesse texto as informações que nós queremos.
'''

@dataclass
class Filme:
    id: int
    titulo: str
    diretor: str
    ano: list


    '''
        A função find_info() é aquela que criamos para editar o bloco de texto que coletamos com a requests.
        E como fazemos isso? Utilizando a biblioteca regex. Com ela, podemos criar um padrão que queremos encontrar
        dentro do texto. Parecida com a beautifulsoup, porém a diferença é que a beautifulsoup é específica pra web
        e a regex é específica para padrões.
        
        Obs: Se quiser saber mais sobre regex, basta pesquisar a documentação e fazer alguns testes. Até porque eu
        pedi pro chatGPT fazer isso já que eu não queria perder tempo aprendendo :D
    '''
    def find_info(text: str) -> tuple:
        # usando regex, estabelecemos o padrão abaixo
        padrao = r'(\d+) — (.*?) \((.*?)\), de (.*?)$'
        # as correspondências aqui são os famosos "matchs" que acontecem quando o regex encontra um padrão.
        matches = re.search(padrao, text, re.MULTILINE)
        '''
            se forem achadas correspondências, adicionamos o título, diretor e ano. Cada uma dessas correspondências
            estão em grupos que definimos usando parênteses (). Se observar o padrão, verá 4 parênteses. O chatGPT
            está usando o grupo 2 (titulo), 4 (diretor) e 3 (ano). O grupo (1) seria o número do filme na lista,
            mas não queremos isso.
        '''
        if matches:
            id = int(matches.group(1))
            titulo = matches.group(2)
            diretor = matches.group(4)
            ano = [int(ano) for ano in matches.group(3).strip().split('/')]
            
            return (id, titulo, diretor, sorted(ano))
        
        # Se não forem achadas correspondẽncias retorne (1, 2, 3, 4) onde deveriam estar o título, diretor e ano.
        # Dessa forma sabemos que tem algo errado
        return (1, 2, 3, 4)
        