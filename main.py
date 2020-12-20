import requests
import csv
from bs4 import BeautifulSoup
from config import URL, URL_BASE

# criar o arquivo que será usado para salvar os dados
arquivo_csv = csv.writer(open('nomes_artistas_z.csv', 'w', newline='\n'))

# criar cabeçalho (colunas) dos dados no arquivo
arquivo_csv.writerow(['Nomes Artistas', 'URL Artistas'])

# criando uma lista de paginas que pegaremos os dados
paginas = []
for num_page in range(1, 5):
    paginas.append(f"https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ{num_page}.htm")


for url_por_pagina in paginas:
    pagina = requests.get(url_por_pagina)
    soup = BeautifulSoup(pagina.text, 'html.parser')

    # remover ultimos links
    ultimos_links = soup.find(class_='AlphaNav')
    ultimos_links.decompose()

    # pegar o conteúdo de todos os body text
    bloco_nome_artista = soup.find(class_='BodyText')

    # filtrando somente a tag a
    lista_nomes_artistas = bloco_nome_artista.find_all('a')

    # iterando os nomes na lista de nomes e colocando o conteudo nas variaveis
    for nome_artista in lista_nomes_artistas:
        nomes = nome_artista.contents[0]
        links = f"{URL_BASE}{nome_artista.get('href')}"
        print(nomes)
        print(links)
        # escrevendo os dados no arquivo
        arquivo_csv.writerow([nomes, links])


# é só um exemplo de código, acabou não sendo usado no exemplo
# usando o prettify para melhorar a apresentacao
# for nome_artista in lista_nomes_artistas:
#    print(nome_artista.prettify())
