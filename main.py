import pandas as pd
import funcoesPandas


df = pd.read_csv('consulta_cand_2024_PB.csv', encoding='latin1', delimiter=';')

funcoesPandas.menuInterativo(df)

