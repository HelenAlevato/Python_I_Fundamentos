import requests

cep = input("Digite um cep: ")

url = f"https://viacep.com.br/ws/{cep}/json"
requisicao = requests.get(url, verify=False)

dados = requisicao.json()
# print(dados)

for chave, valor in dados.items():
    print(chave, ":", valor)

# print(dados["logradouro"])