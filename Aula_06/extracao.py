import requests
from bs4 import BeautifulSoup

url = "http://eventos.sp.senac.br/"

requisicao = requests.get(url)

site = BeautifulSoup(requisicao.text, "html.parser")

titulos = site.find_all("h3")
for t in titulos:
    print(t.text)

# print(site.prettify())