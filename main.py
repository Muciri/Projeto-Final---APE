import pandas as pd
import funcoesPandas #Importa a pagina com as funcoes pandas

#Pagina principal que roda todo o código




df = pd.read_csv('consulta_cand_2024_PB.csv', encoding='latin1', delimiter=';')

funcoesPandas.gerarMenuInterativo(df)



