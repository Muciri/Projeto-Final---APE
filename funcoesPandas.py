import funcoesDominate #importa a pagina com as funcoes dominate
import pandas as pd
import util #importa a pagina util

#Pagina com todas as funções que usam a biblioteca pandas

# exibir lista de candidatos - feito por Mariana Ludmilla
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
                    Partido: {row['NM_PARTIDO']}
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
                    funcoesDominate.criarPagina(qtdCargos(df), partidoPrefeito(df), pegarCandidatosPorIdade(df), percentualCandidatos(df))
                case '4':
                    print('fim do programa...')
                    break
                case _:
                    print('opção inválida')

#region Quatidade Cargos
                    
def qtdCargos(df):
    """
    @desc: Retorna a quantidade de candidatos por cargo
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


    return [["Quantidade de Candidatos por Cargo"],
            ["Prefeitos", "Vice-prefeitos", "Vereadores"],
            [prefeito, vicePrefeito, vereador]]
#region Partido por Prefeito


def partidoPrefeito(df):
    """
    @desc: Retorna  os partidos que tem candidatos a prefeito 
    @author: Melqui
    """
    lista_part = []
    
    cargo = df['CD_CARGO']
    part = df["NM_PARTIDO"]

    for i in range(len(df)):
        if cargo[i] == 11 and part[i] not in lista_part:
            lista_part.append(part[i])
        
    return [["Partidos com Candidatos a Prefeito"],lista_part]

#region Quantidade de candidatos por idade

def pegarCandidatosPorIdade(df):
     
    """
    @desc: Retornar os candidatos em uma faixa de idade
    @author: Felipe
    """

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
    """
    @desc: Retorna dicionarios com o grau de instrucao para cada cargo
    @author: Felipe
    """
    grauDeintrucaoPrefeito = {
        "analfabeto":0,
        "ler_escrever":0,
        "ensinoFundamentalIncompleto":0,
        "ensinoFundamentalCompleto":0,
        "ensinoMedioIncompleto":0,
        "ensinoMedioCompleto":0,
        "superiorIncompleto":0,
        "superiorCompleto":0
    }

    grauDeintrucaoVicePrefeito = {
        "analfabeto":0,
        "ler_escrever":0,
        "ensinoFundamentalIncompleto":0,
        "ensinoFundamentalCompleto":0,
        "ensinoMedioIncompleto":0,
        "ensinoMedioCompleto":0,
        "superiorIncompleto":0,
        "superiorCompleto":0
    }

    grauDeintrucaoVereador = {
        "analfabeto":0,
        "ler_escrever":0,
        "ensinoFundamentalIncompleto":0,
        "ensinoFundamentalCompleto":0,
        "ensinoMedioIncompleto":0,
        "ensinoMedioCompleto":0,
        "superiorIncompleto":0,
        "superiorCompleto":0
    }


    intrucao = df['CD_GRAU_INSTRUCAO']
    cargo = df["CD_CARGO"]

    for id in range(len(df)):
        if cargo[id] == 11:
            if intrucao[id]==1:
                grauDeintrucaoPrefeito['analfabeto']+=1
            elif intrucao[id] == 2:
                grauDeintrucaoPrefeito['ler_escrever']+=1
            elif intrucao[id] == 3:
                grauDeintrucaoPrefeito['ensinoFundamentalIncompleto']+=1
            elif intrucao[id] == 4:
                grauDeintrucaoPrefeito['ensinoFundamentalCompleto']+=1
            elif intrucao[id] == 5:
                grauDeintrucaoPrefeito['ensinoMedioIncompleto']+=1
            elif intrucao[id] == 6:
                grauDeintrucaoPrefeito['ensinoMedioCompleto']+=1
            elif intrucao[id] == 7:
                grauDeintrucaoPrefeito['superiorIncompleto']+=1
            elif intrucao[id] == 8:
                grauDeintrucaoPrefeito['superiorCompleto']+=1
        elif cargo[id] == 12:
            if intrucao[id]==1:
                grauDeintrucaoVicePrefeito['analfabeto']+=1
            elif intrucao[id] == 2:
                grauDeintrucaoVicePrefeito['ler_escrever']+=1
            elif intrucao[id] == 3:
                grauDeintrucaoVicePrefeito['ensinoFundamentalIncompleto']+=1
            elif intrucao[id] == 4:
                grauDeintrucaoVicePrefeito['ensinoFundamentalCompleto']+=1
            elif intrucao[id] == 5:
                grauDeintrucaoVicePrefeito['ensinoMedioIncompleto']+=1
            elif intrucao[id] == 6:
                grauDeintrucaoVicePrefeito['ensinoMedioCompleto']+=1
            elif intrucao[id] == 7:
                grauDeintrucaoVicePrefeito['superiorIncompleto']+=1
            elif intrucao[id] == 8:
                grauDeintrucaoVicePrefeito['superiorCompleto']+=1
        elif cargo[id] == 13:
            if intrucao[id]==1:
                grauDeintrucaoVereador['analfabeto']+=1
            elif intrucao[id] == 2:
                grauDeintrucaoVereador['ler_escrever']+=1
            elif intrucao[id] == 3:
                grauDeintrucaoVereador['ensinoFundamentalIncompleto']+=1
            elif intrucao[id] == 4:
                grauDeintrucaoVereador['ensinoFundamentalCompleto']+=1
            elif intrucao[id] == 5:
                grauDeintrucaoVereador['ensinoMedioIncompleto']+=1
            elif intrucao[id] == 6:
                grauDeintrucaoVereador['ensinoMedioCompleto']+=1
            elif intrucao[id] == 7:
                grauDeintrucaoVereador['superiorIncompleto']+=1
            elif intrucao[id] == 8:
                grauDeintrucaoVereador['superiorCompleto']+=1
        
    return grauDeintrucaoPrefeito, grauDeintrucaoVicePrefeito, grauDeintrucaoVereador
        

def contadorGenero(df):
    """
    @desc: Retorna dicionarios com o total de homens e mulheres para cada cargo
    @author: Felipe
    """

    generoPrefeito = {
        "masculino":0,
        "feminino":0
    }

    generoVicePrefeito = {
        "masculino":0,
        "feminino":0
    }

    generoVereador = {
        "masculino":0,
        "feminino":0
    }
    sexo = df['CD_GENERO']
    cargo = df["CD_CARGO"]

    for id in range(len(df)):
        if cargo[id] == 11:
            if sexo[id] == 2:
                generoPrefeito['masculino']+=1
            elif sexo[id] == 4:
                generoPrefeito['feminino']+=1
        elif cargo[id] == 12:
            if sexo[id] == 2:
                generoVicePrefeito['masculino']+=1
            elif sexo[id] == 4:
                generoVicePrefeito['feminino']+=1
        elif cargo[id] == 13:
            if sexo[id] == 2:
                generoVereador['masculino']+=1
            elif sexo[id] == 4:
                generoVereador['feminino']+=1
    return generoPrefeito, generoVicePrefeito, generoVereador

def contadorEstadoCivil(df):

    """
    @desc: Retorna dicionarios com a condicao do estado civil para cada cargo
    @author: Felipe
    """
    estadoCivilPrefeito = {
        'solteiro':0,
        'casado':0,
        'viuvo':0,
        'separado':0,
        'divorciado':0
    }

    estadoCivilVicePrefeito = {
        'solteiro':0,
        'casado':0,
        'viuvo':0,
        'separado':0,
        'divorciado':0
    }

    estadoCivilVereador = {
        'solteiro':0,
        'casado':0,
        'viuvo':0,
        'separado':0,
        'divorciado':0
    }

    estado = df['CD_ESTADO_CIVIL']
    cargo = df["CD_CARGO"]

    for id in range(len(df)):
        if cargo[id] == 11:
            if estado[id] == 1:
                estadoCivilPrefeito['solteiro']+=1
            elif estado[id] == 3:
                estadoCivilPrefeito['casado']+=1
            elif estado[id] == 5:
                estadoCivilPrefeito['viuvo']+=1
            elif estado[id] == 7:
                estadoCivilPrefeito['separado']+=1
            elif estado[id] == 9:
                estadoCivilPrefeito['divorciado']+=1
        elif cargo[id] == 12:
            if estado[id] == 1:
                estadoCivilVicePrefeito['solteiro']+=1
            elif estado[id] == 3:
                estadoCivilVicePrefeito['casado']+=1
            elif estado[id] == 5:
                estadoCivilVicePrefeito['viuvo']+=1
            elif estado[id] == 7:
                estadoCivilVicePrefeito['separado']+=1
            elif estado[id] == 9:
                estadoCivilVicePrefeito['divorciado']+=1
        elif cargo[id] == 13:
            if estado[id] == 1:
                estadoCivilVereador['solteiro']+=1
            elif estado[id] == 3:
                estadoCivilVereador['casado']+=1
            elif estado[id] == 5:
                estadoCivilVereador['viuvo']+=1
            elif estado[id] == 7:
                estadoCivilVereador['separado']+=1
            elif estado[id] == 9:
                estadoCivilVereador['divorciado']+=1
    return estadoCivilPrefeito, estadoCivilVicePrefeito, estadoCivilVereador


def percentualCandidatos(df):
    """
    @desc: Calcula o percentual de cada cargo para genero, grau de instrucao e estado civil
    @author: Felipe
    """
    cargo = qtdCargos(df)
    prefeitoTotal = cargo[2][0]
    vicePrefeitoTotal = cargo[2][1]
    vereadorTotal = cargo[2][2]
    instrucao = contadorGraudeInstrucao(df)
    genero = contadorGenero(df)
    estadoCivil = contadorEstadoCivil(df)

    prefeito = [{  
                   "analfabeto": (instrucao[0]["analfabeto"]/prefeitoTotal)*100,
                    "ler_escrever": (instrucao[0]["ler_escrever"]/prefeitoTotal)*100,
                    "ensinoFundamentalIncompleto": (instrucao[0]["ensinoFundamentalIncompleto"]/prefeitoTotal)*100,
                    "ensinoFundamentalCompleto": (instrucao[0]["ensinoFundamentalCompleto"]/prefeitoTotal)*100,
                    "ensinoMedioIncompleto": (instrucao[0]["ensinoMedioIncompleto"]/prefeitoTotal)*100,
                    "ensinoMedioCompleto": (instrucao[0]["ensinoMedioCompleto"]/prefeitoTotal)*100,
                    "superiorIncompleto": (instrucao[0]["superiorIncompleto"]/prefeitoTotal)*100,
                    "superiorCompleto": (instrucao[0]["superiorCompleto"]/prefeitoTotal)*100 },
                    {
                        
                        "masculino": (genero[0]["masculino"]/prefeitoTotal)*100,
                        "feminino":(genero[0]["feminino"]/prefeitoTotal)*100
                    },
                    {
                       
                        'solteiro': (estadoCivil[0]["solteiro"]/prefeitoTotal)*100,
                        'casado': (estadoCivil[0]['casado']/prefeitoTotal)*100,
                        'viuvo': (estadoCivil[0]['viuvo']/prefeitoTotal)*100,
                        'separado': (estadoCivil[0]['separado']/prefeitoTotal)*100,
                        'divorciado': (estadoCivil[0]['divorciado']/prefeitoTotal)*100
                    }]
    vicePrefeito = [
                    {
                   "analfabeto": (instrucao[1]["analfabeto"]/vicePrefeitoTotal)*100,
                    "ler_escrever": (instrucao[1]["ler_escrever"]/vicePrefeitoTotal)*100,
                    "ensinoFundamentalIncompleto": (instrucao[1]["ensinoFundamentalIncompleto"]/vicePrefeitoTotal)*100,
                    "ensinoFundamentalCompleto": (instrucao[1]["ensinoFundamentalCompleto"]/vicePrefeitoTotal)*100,
                    "ensinoMedioIncompleto": (instrucao[1]["ensinoMedioIncompleto"]/vicePrefeitoTotal)*100,
                    "ensinoMedioCompleto": (instrucao[1]["ensinoMedioCompleto"]/vicePrefeitoTotal)*100,
                    "superiorIncompleto": (instrucao[1]["superiorIncompleto"]/vicePrefeitoTotal)*100,
                    "superiorCompleto": (instrucao[1]["superiorCompleto"]/vicePrefeitoTotal)*100 },
                    {
                       
                        "masculino": (genero[1]["masculino"]/vicePrefeitoTotal)*100,
                        "feminino":(genero[1]["feminino"]/vicePrefeitoTotal)*100
                    },
                    {
                        'solteiro': (estadoCivil[1]["solteiro"]/vicePrefeitoTotal)*100,
                        'casado': (estadoCivil[1]['casado']/vicePrefeitoTotal)*100,
                        'viuvo': (estadoCivil[1]['viuvo']/vicePrefeitoTotal)*100,
                        'separado': (estadoCivil[1]['separado']/vicePrefeitoTotal)*100,
                        'divorciado': (estadoCivil[1]['divorciado']/vicePrefeitoTotal)*100
                    }
    ]
    vereador = [
            {
                   "analfabeto": (instrucao[2]["analfabeto"]/vereadorTotal)*100,
                    "ler_escrever": (instrucao[2]["ler_escrever"]/vereadorTotal)*100,
                    "ensinoFundamentalIncompleto": (instrucao[2]["ensinoFundamentalIncompleto"]/vereadorTotal)*100,
                    "ensinoFundamentalCompleto": (instrucao[2]["ensinoFundamentalCompleto"]/vereadorTotal)*100,
                    "ensinoMedioIncompleto": (instrucao[2]["ensinoMedioIncompleto"]/vereadorTotal)*100,
                    "ensinoMedioCompleto": (instrucao[2]["ensinoMedioCompleto"]/vereadorTotal)*100,
                    "superiorIncompleto": (instrucao[2]["superiorIncompleto"]/vereadorTotal)*100,
                    "superiorCompleto": (instrucao[2]["superiorCompleto"]/vereadorTotal)*100 },
                    {
                        "masculino": (genero[2]["masculino"]/vereadorTotal)*100,
                        "feminino":(genero[2]["feminino"]/vereadorTotal)*100
                    },
                    {
                        'solteiro': (estadoCivil[2]["solteiro"]/vereadorTotal)*100,
                        'casado': (estadoCivil[2]['casado']/vereadorTotal)*100,
                        'viuvo': (estadoCivil[2]['viuvo']/vereadorTotal)*100,
                        'separado': (estadoCivil[2]['separado']/vereadorTotal)*100,
                        'divorciado': (estadoCivil[2]['divorciado']/vereadorTotal)*100
                    }
    ]

    return prefeito, vereador, vicePrefeito










