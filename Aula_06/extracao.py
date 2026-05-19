import requests
from bs4 import BeautifulSoup

url = "http://eventos.sp.senac.br/"

requisicao = requests.get(url)

site = BeautifulSoup(requisicao.text, "html.parser")

print(site.prettify())