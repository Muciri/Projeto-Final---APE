import pandas as pd
import funcoesPandas
import matplotlib.pylab as plt



df = pd.read_csv('consulta_cand_2024_PB.csv', encoding='latin1', delimiter=';')

#funcoesPandas.gerarMenuInterativo(df)

prefeito, vicePrefeito, vereador = funcoesPandas.percentualCandidatos(df)
names  = list(prefeito[0].keys())
values = list(prefeito[0].values())


plt.bar(range(len(prefeito[0])), values, tick_label=names)