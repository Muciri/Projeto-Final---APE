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
def gerarMenuInterativo(df):
    print('=-=-=-=-=-=-=-=-=-=-=-ELEIÇÕES 2024=-=-=-=-=-=-=-=-=-=-=-')

    while True:
            op = util.painelDeEscolhas()
            match op:
                case '1':
                    cod_municipio = input('digite o código do município: ')
                    cod_cargo = input('digite o código do cargo: ')
                    print(listarCandidatos(df, cod_municipio, cod_cargo))
                case '2':
                    num_candidato = input('digite o número do candidato:')
                    print(buscarCandidato(df, num_candidato))
                case '3':
                    funcoesDominate.criarPagina(qtdCargos(df), partidoPrefeito(df), pegarCandidatosPorIdade(df))

                    funcoesDominate.criarPagina(qtdCargos(df), pegarCandidatosPorIdade(df))
                case '4':
                    print('fim do programa...')
                    break
                case _:
                    print('opção inválida')

#region Quatidade Cargos
                    
def qtdCargos(df):
    """
    @desc: Authenticates user & returns a token
    @author: Melqui
    """
    codCargo = df['CD_CARGO']

    prefeito = 0
    vicePrefeito = 0
    vereador = 0


    for id in codCargo:
        if id == 11:
            prefeito += 1
        elif id == 12:
            vicePrefeito += 1
        elif id == 13:
            vereador += 1

    return [prefeito, vicePrefeito, vereador]

    return [["Quantidade de Candidatos por Cargo"],
            ["Prefeitos", "Vice-prefeitos", "Vereadores"],
            [pref, vpref, ver]]
#region Partido por Prefeito


def partidoPrefeito(df):
    lista_part = []
    
    cargo = df['CD_CARGO']
    part = df["NM_PARTIDO"]

    for i in range(len(df)):
        if cargo[i] == 11 and part[i] not in lista_part:
            lista_part.append(part[i])
        
    return [["Partidos com Candidatos a Prefeito"],lista_part]

#region Quantidade de candidatos por idade

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
            
        
    return [["Candidatos por Idade"],
            ["Ate 21 anos", "Entre 22 e 40 anos", "Entre 41 e 60", "Acima de 60"],
            [idadeAte21, idadeEntre22_40, idadeEntre41_60, idadeAcima60]]

# #Percentual de candidatos por cargo, considerando:
# Grau de instrução; (CD_GRAU_INSTRUCAO)
# Gênero; (CD_GENERO)
# Estado civil. (CD_ESTADO_CIVIL)

def contadorGraudeInstrucao(df):
    grauDeintrucao = {
        "analfabeto":0,
        "ler_escrever":0,
        "ensinoFundamentalIncompleto":0,
        "ensinoFundamentalCompleto":0,
        "ensinoMedioIncompleto":0,
        "ensinoMedioCompleto":0,
        "superiorIncompleto":0,
        "superiorCompleto":0
    }
    intrucao = df['CD_GRAU_INTRUCAO']

    for grau in intrucao:
        if grau == 1:
            grauDeintrucao['analfabeto']+=1
        elif grau == 2:
            grauDeintrucao['ler_escrever']+=1
        elif grau == 3:
            grauDeintrucao['ensinoFundamentalIncompleto']+=1
        elif grau == 4:
            grauDeintrucao['ensinoFundamentalCompleto']+=1
        elif grau == 5:
            grauDeintrucao['ensinoMedioIncompleto']+=1
        elif grau == 6:
            grauDeintrucao['ensinoMedioCompleto']+=1
        elif grau == 7:
            grauDeintrucao['superiorIncompleto']+=1
        elif grau == 8:
            grauDeintrucao['superiorCompleto']+=1
    return grauDeintrucao
        

def contadorGenero(df):
    genero = {
        "masculino":0,
        "feminino":0
    }
    sexo = df['CD_GENERO']

    for genEro in sexo:
        if genEro == 2:
             genero['masculino']+=1
        elif genEro == 4:
             genero['feminino']+=1
    return genero

def contadorEstadoCivil(df):
    estadoCivil = {
        'solteiro':0,
        'casado':0,
        'viuvo':0,
        'separado':0,
        'divorciado':0
    }

    estado = df['CD_ESTADO_CIVIL']

    for civil in estado:
        if civil == 1:
            estadoCivil['solteiro']+=1
        elif civil == 3:
            estadoCivil['casado']+=1
        elif civil == 5:
            estadoCivil['viuvo']+=1
        elif civil == 7:
            estadoCivil['separado']+=1
        elif civil == 9:
            estadoCivil['divorciado']+=1
    return estadoCivil












