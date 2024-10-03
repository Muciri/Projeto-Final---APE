import dominate
from dominate.tags import *

#Pagina com todas as funções que usam a biblioteca dominate

#cria a pagina HTMl
def criarPagina(qtdCargos,partidoPrefeito, idadeCandidato, cargoPercentual):
    """
    @desc: Cria a pagina HTML
    @author: Melquisedeque
    """
    dom = dominate.document(title='Eleicao')
    doc = open("index.html", "w", encoding="utf8") 



    cargos = qtdCargos

    partido = partidoPrefeito

    idade = idadeCandidato

    prefeito = cargoPercentual[0]

    vicePrefeito = cargoPercentual[1]

    vereador = cargoPercentual[2]

    with dom.head:
        meta(charset="UTF-8")
        link(rel='stylesheet')
        script(src="https://cdn.tailwindcss.com") 
    with dom:
        with div(cls="flex flex-col gap-14 p-52"):
            gerarTabela(cargos)
            gerarGrade(partido)
            gerarTabela(idade)
            div("Percentual Por Cargos", cls="text-center text-6xl font-bold")
            gerarPercentual(prefeito, "Prefeito")
            gerarPercentual(vicePrefeito, "Vice Prefeito")
            gerarPercentual(vereador, "Vereador")


    doc.write(str(dom))
    doc.close()
    

def gerarTabela(array):
        """
        @desc: Gera uma tabela html
        @author: Melquisedeque
        """
        h2(array[0], cls='text-center font-bold text-4xl')
        with table(cls='table-auto text-center border-collapse'):
            with tr(cls="bg-gray-100"): 
                for head in array[1]:
                    th(head.title(), cls="text-center border-solid border-2 border-gray-300 px-5")
            for linha in array[2:]:
                with tr(cls="text-center"):
                    for palavra in linha:
                        td(palavra, cls="text-center border-solid border-2 border-gray-300 px-5")




def gerarGrade(array):
    """
    @desc: Gera um grid html
    @author: Melquisedeque
    """
    with div(cls="grid grid-cols-2 grid-rows-auto"):
        div(array[0], cls="col-span-2 bg-gray-200 text-center font-bold text-4xl")
        for partido in array[1]:
            div(partido.title(), cls="border-2 border-gray-500 text-center text-xl")


def gerarPercentual(array, nome):
    """
    @desc: Gera as informações de percentual
    @author: Melquisedeque
    """
    
    h2(nome, cls="text-center text-4xl font-bold")
    h3("Instrucao", cls="text-center text-2xl")
    with div(cls="grid grid-row-auto grid-cols-2"):
        with div(cls=""):
            for key in array[0].keys():
                div(key.title(), cls="border-2 border-gray-500 text-center text-xl")
        with div(cls=""):
            for value in array[0].values():
                div(f"{value:.2f}%", cls="border-2 border-gray-500 text-center text-xl")


    h3("Genero", cls="text-center text-2xl ")
    with div(cls="grid grid-row-auto grid-cols-2"):
        with div(cls=""):
            for key in array[1].keys():
                div(key.title(), cls="border-2 border-gray-500 text-center text-xl")
        with div(cls=""):
            for value in array[1].values():
                div(f"{value:.2f}%", cls="border-2 border-gray-500 text-center text-xl")


    h3("Estado Civil", cls="text-center text-2xl ")
    with div(cls="grid grid-row-auto grid-cols-2"):
        with div(cls=""):
            for key in array[2].keys():
                div(key.title(), cls="border-2 border-gray-500 text-center text-xl")
        with div(cls=""):
            for value in array[2].values():
                div(f"{value:.2f}%", cls="border-2 border-gray-500 text-center text-xl")
