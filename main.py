import pandas as pd

df = pd.read_csv('consulta_cand_2024_PB.csv', encoding='latin1', delimiter=';')

# exibir lista de candidatos - feito por Mariana Ludmilla
def listar_candidatos(cod_municipio, cod_cargo):  
    try:
        print('Lista de candidatos:')
        # Filtrando a tabela
        candidatos_filtrados = df[(df['SG_UE'] == int(cod_municipio)) & (df['CD_CARGO'] == int(cod_cargo))]
        
        if not candidatos_filtrados.empty:
            resultado = []
            for i, row in candidatos_filtrados.iterrows():
                resultado.append(f'''
                    Nome: {row['NM_CANDIDATO']}
                    Nome na urna: {row['NM_URNA_CANDIDATO']}
                    Número: {row['NR_CANDIDATO']}
                    Partido: {row['NM_PARTIDO']}S
                ''')
            return '\n'.join(resultado)
        else:
            return ('Candidatos não encontrados') #retorna mensagem caso o código da cidade e/ou código do cargo não sejam encontrados
    except:
        return ('Parâmetros inválidos') #retorna mensagem caso seja fornecido um valor inválido

    
#exibir as informações do candidato - feito por Murilo Maciel
def buscar_candidato(num_candidato): 
    try:
        candidato = df[df['SQ_CANDIDATO'] == int(num_candidato)] #filtra o candidato pelo número fornecido
        if not candidato.empty:
            #retorna informações do candidato
            print('informações do candidato:')
            return(f''' 
                Nome: {candidato['NM_CANDIDATO'].values[0]}
                Nome na urna: {candidato['NM_URNA_CANDIDATO'].values[0]}
                número: {candidato['NR_CANDIDATO'].values[0]}
                partido: {candidato['NM_PARTIDO'].values[0]}
                    ''')
        else:
            return('candidato não encontrado') #retorna mensagem caso o número do candidato não seja encontrado
    except:
        return('candidato inválido') #retorna mensagem caso seja fornecido um valor inválido


#interface principal do programa  - feito por Murilo Maciel
print('=-=-=-=-=-=-=-=-=-=-=-ELEIÇÕES 2024=-=-=-=-=-=-=-=-=-=-=-')

while True:
        print('|1| fornecer a lista de candidatos \n|2| exibir as informações: nome, nome na urna, número e partido. \n|3| Gerar página HTML com estatísticas \n|4| sair')
        op = input('o que você deseja fazer? (digite abaixo o número da ação) \n--> ')
        match op:
            case '1':
                cod_municipio = input('digite o código do município: ')
                cod_cargo = input('digite o código do cargo: ')
                print(listar_candidatos(cod_municipio, cod_cargo))
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
