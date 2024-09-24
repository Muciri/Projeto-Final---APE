import pandas as pd

df = pd.read_csv('consulta_cand_2024_PB.csv', encoding='latin1', delimiter=';')

def buscar_candidato(num_candidato):
    try:
        candidato = df[df['SQ_CANDIDATO'] == int(num_candidato)]
        if not candidato.empty:
            return(f'''
                Nome: {candidato['NM_CANDIDATO'].values[0]}
                Nome na urna: {candidato['NM_URNA_CANDIDATO'].values[0]}
                número: {candidato['NR_CANDIDATO'].values[0]}
                partido: {candidato['NM_PARTIDO'].values[0]}
                    ''')
        else:
            return('candidato não encontrado')
    except:
        return('candidato inválido')


print('=-=-=-=-=-=-=-=-=-=-=-ELEIÇÕES 2024=-=-=-=-=-=-=-=-=-=-=-')

#interface principal do programa
while True:
        print('|1| fornecer a lista de candidatos \n|2| exibir as informações: nome, nome na urna, número e partido. \n|3| Gerar página HTML com estatísticas \n|4| sair')
        op = input('o que você deseja fazer? (digite abaixo o número da ação) \n--> ')
        match op:
            case '1':
                print('imprimindo lista de candidatos...')
                print('opção ainda não disponível')
            case '2':
                num_candidato = input('digite o número do candidato:')
                print(buscar_candidato(num_candidato))
            case '3':
                print('gerando página HTML...')
                print('opção ainda não disponível')
            case '4':
                print('fim do programa...')
                break
            case _:
                print('opção inválida')