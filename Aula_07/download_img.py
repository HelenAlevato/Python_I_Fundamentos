import os # Importa função do sistema operacional
import requests # Importa biblioteca para fazer requisição HTTP
from bs4 import BeautifulSoup # Importa a classe beautifulsoup
from urllib.parse import urljoin #Importa função para montar url completa

os.system('cls') # Limpa o terminal do windows
url = "https://eventos.sp.senac.br/" # URL do site
os.makedirs("imagens", exist_ok=True) # Cria a pasta imagens caso ela não exista
requisicao = requests.get(url) # Faz requisição para acessar o site
site = BeautifulSoup(requisicao.text, "html.parser") # Interpreta o HTML da página

imagens = site.find_all("img") # Busca todas as tags <img>

for img in imagens: # Percorre todas as imagens encontradas
    caminho = img.get("src") # Obtém o valor do atributo src da imagem
    if caminho: # Verifica se o src existe
        url_imagem = urljoin(url, caminho) # Manda url completa da imagem
        nome = url_imagem.split("/")[-1] # Obtém o nome da imagem pela URL
        nome = nome.split("?")[0] # Remove parâmetros extras da URL
        imagem = requests.get(url_imagem) # Faz dawnload da imagem
        with open(f"imagens/{nome}", "wb") as arquivo: # Cria arquivo em modo binário
            arquivo.write(imagem.content) # Salva os bytes da imagem no arquivo
        print(f"{nome} salva!") # Mostra msg de sucesso