import requests
from bs4 import BeautifulSoup
import os

os.system('cls')
url = "https://www.cnnbrasil.com.br/"
requisicao = requests.get(url)
site = BeautifulSoup(requisicao.text, "html.parser") # Transforma o texto em html

# print(site.prettify()) # Organiza o texto html

titulos = site.select("h2 a")
for t in titulos:
    print(t.get("href"))