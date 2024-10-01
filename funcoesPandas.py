import funcoesDominate
import pandas as pd
import util

# exibir lista de candidatos - feito por Mariana Ludmila
def listarCandidatos(df, cod_municipio, cod_cargo):  
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
def buscarCandidato(df, num_candidato): 
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
def menuInterativo(df):
    print('=-=-=-=-=-=-=-=-=-=-=-ELEIÇÕES 2024=-=-=-=-=-=-=-=-=-=-=-')

    while True:
            print('|1| fornecer a lista de candidatos \n|2| exibir as informações: nome, nome na urna, número e partido. \n|3| Gerar página HTML com estatísticas \n|4| sair')
            op = input('o que você deseja fazer? (digite abaixo o número da ação) \n--> ')
            match op:
                case '1':
                    cod_municipio = input('digite o código do município: ')
                    cod_cargo = input('digite o código do cargo: ')
                    print(listarCandidatos(df, cod_municipio, cod_cargo))
                case '2':
                    num_candidato = input('digite o número do candidato:')
                    print(buscarCandidato(df, num_candidato))
                case '3':
                    funcoesDominate.criarPagina(qtdCargos(df), pegarCandidatosPorIdade(df))
                case '4':
                    print('fim do programa...')
                    break
                case _:
                    print('opção inválida')


#Feito por Felipe e Melquisedeque
def qtdCargos(df):
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

    return [pref, vpref, ver]


def partidoPrefeito(df):
    lista_part = []
    
    cargo = df['CD_CARGO']
    part = df["NM_PARTIDO"]

    for i in range(len(df)):
        if cargo[i] == 11 and part[i] not in lista_part:
            lista_part.append(part[i])
        
    return lista_part


def pegarCandidatosPorIdade(df):

    idadeAte21 = 0
    idadeEntre22_40  = 0
    idadeEntre41_60 = 0
    idadeAcima60 = 0

    datas = df["DT_NASCIMENTO"]
    

    for nasc in datas:
        idade = util.pegarIdade(nasc)

        if idade <= 21:
            idadeAte21 += 1
        elif idade <= 40:
            idadeEntre22_40 += 1
        elif idade <= 60:
            idadeEntre41_60 += 1
        else:
            idadeAcima60 += 1
            
        
    return [["Até 21 anos", "Entre 22 e 40 anos", "Entre 41 e 60", "Acima de 60"],[idadeAte21, idadeEntre22_40, idadeEntre41_60, idadeAcima60]]




