import datetime

#Calcula idade pela data de nascimento
def pegarIdade(dataNascimento):
    dia, mes, ano = map(int, dataNascimento.split('/'))
    hoje = datetime.date.today()
    idade = hoje.year - ano - ((hoje.month, hoje.day) < (mes, dia))
    return idade

#Gera um painel de escolhas
def painelDeEscolhas():
    print('''
        |1| fornecer a lista de candidatos 
        |2| exibir as informações: nome, nome na urna, número e partido. 
        |3| Gerar página HTML com estatísticas 
        |4| sair
        ''')
    op = input('o que você deseja fazer? (digite abaixo o número da ação) \n--> ')
    return op





    
    
