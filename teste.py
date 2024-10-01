import pandas as pd

df = pd.read_csv('consulta_cand_2024_PB.csv', encoding='latin1', delimiter=';')


#quantidade por cargos
cargo = df['CD_CARGO']

pref = 0
vpref = 0
ver = 0


for id in cargo:
    if id == 11:
        pref += 1
    elif id == 12:
        vpref += 1
    elif id == 13:
        ver += 1


print(pref, vpref, ver)



#partidos com prefeitos
lista_part = []

part = df["NM_PARTIDO"]

print(part[0], cargo[0])

for i in range(len(df)):
    if cargo[i] == 11 and part[i] not in lista_part:
      lista_part.append(part[i])
    
print(lista_part)
