import pandas as pd

df = pd.read_csv('consulta_cand_2024_PB.csv', encoding='latin1', delimiter=';')

print(df.head()) 

# Exibe as primeiras linhas do DataFrame
print(df.head()) 

# Acessa uma coluna específica (por exemplo, 'nome')
print(df['NM_CANDIDATO'])  



