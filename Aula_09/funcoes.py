import requests
from bs4 import BeautifulSoup
import os

# 4
def acessar_site(url):
    try:
        if url:
            requisicao = requests.get(url)
            return BeautifulSoup(requisicao.text, "html.parser")
        else:
            print("Informe site válido!!!")
        requisicao = requests.get(url)
        return BeautifulSoup(requisicao.text, "html.parser")
    except Exception as erro:
        print(erro)

def extrair_titulos(url,seletor):
    try:
        site = acessar_site(url)
        tituloshtml = site.select(seletor)
        titulos = []

        for t in tituloshtml:
            if t:
                titulos.append( {"Titulos": t.text.strip()} )
        for titulo in titulos:
            print(titulo)
            
        return titulos
    except Exception as erro:
        print(erro)

