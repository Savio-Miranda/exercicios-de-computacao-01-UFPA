from locadora import Locadora


# Essa é a nossa URL base. O link do site que queremos fazer nosso webscrap
url_base = r'https://www.revistabula.com/7073-2-lista-definitiva-dos-100-melhores-filmes-de-todos-os-tempos/'

minha_locadora = Locadora(url_base)
minha_locadora.catalogo()
#minha_locadora.filmes_anteriores(2002)
#minha_locadora.filmes_posteriores(2000)
