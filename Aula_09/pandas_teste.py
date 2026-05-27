import os
import pandas as pd
from funcoes import*


titulos = extrair_titulos("https://www.globo.com/", "h2.post__title")

# Criação do DataFrame
df = pd.DataFrame(titulos)

# Salvando em CSV
df.to_csv("dados.csv", index=False)

# Salvando em JSON
df.to_json("dados.json", orient="records", indent=4, force_ascii=False)

print("Arquivos CSV e JSON criados com sucesso!")
