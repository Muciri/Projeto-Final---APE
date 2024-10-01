import datetime

def pegarIdade(dataNascimento):
    dia, mes, ano = map(int, dataNascimento.split('/'))
    hoje = datetime.date.today()
    idade = hoje.year - ano - ((hoje.month, hoje.day) < (mes, dia))
    return idade

pegarIdade('05/09/2005')




    
    
