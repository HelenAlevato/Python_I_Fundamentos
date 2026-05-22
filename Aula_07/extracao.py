import requests
from bs4 import BeautifulSoup
import os

os.system('cls')
url = "https://eventos.sp.senac.br/"
requisicao = requests.get(url)
site = BeautifulSoup(requisicao.text, "html.parser") # Transforma o texto em html

# print(site.prettify()) # Organiza o texto html

titulos = site.find_all("ul", class_="event_date")
dataT = site.find_all("time")
# print(titulos[5].text)
for data in dataT:
    print(data.text)