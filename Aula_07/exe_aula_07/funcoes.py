import requests
from bs4 import BeautifulSoup
import os

# 1
def cadastrar_alunos(nome, nota1, nota2, nota3, nota4):
    media = (nota1 + nota2 + nota3 + nota4) / 4
    situacao = "Aprovado" if media >= 7 else "Reprovado"
    aluno = (nome, media, situacao)
    return aluno

# 2
def adicionar_item(lista, item):
    try:
        if item not in lista:
            lista.append(item)
            lista.sort()
        else:
            print("Esse item já existe na lista")
    except Exception as erro:
        print(f"Erro - {erro}")

def remover_item(lista, item):
    try:
        if item in lista:
            lista.remove(item)
    except Exception as erro:
        print(f"Erro - {erro}")

def listar_itens(lista):
    try:
        if len(lista) > 0:
            for i in lista:
                print(i)
        else:
            print("A lista está vazia")
    except Exception as erro:
        print(f"Erro - {erro}")

# 3
def maiornumero(lista):
    try:
        # return max(lista) isso traz o número maior da lista tbm
        maior = lista[0]
        for n in lista:
            if n > maior:
                maior = n
        return maior
    except Exception as erro:
        print(erro)

def menornumero(lista):
    try:
        return min(lista)
    except Exception as erro:
        print(erro)

def medianumeros(lista):
    try:
        return sum(lista) / len(lista)
    except Exception as erro:
        print(erro)

def numerospares(lista):
    try:
        pares = []
        for n in lista:
            if n % 2 == 0:
                pares.append(n)
        return pares
    except Exception as erro:
        print(erro)

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

def extrair_titulos(url):
    try:
        site = acessar_site(url)
        tituloshtml = site.select("h2.post_title")
        titulos = []

        for t in titulos:
            if t:
                titulos.append(t.text.strip())
            print("titulo")
        for titulo in titulos:
            print(titulo)
    except Exception as erro:
        print(erro)

# 5
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

def extrair_links(url, seletor):
    try:
        site = acessar_site(url)
        linkshtml = site.select(seletor)
        links = []

        for l in linkshtml:
            if l:
                links.append(l.get("href"))
        for link in links:
            print(link)
        return len(links)
    except Exception as erro:
        print(erro)

# 6