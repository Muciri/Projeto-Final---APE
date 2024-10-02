import dominate
from dominate.tags import *

def gerarTabela(array):
        with table(cls='table-auto text-center border-collapse'):
            with tr(cls="bg-gray-100"): 
                for head in array[0]:
                    th(head.title(), cls="text-center border-solid border-2 border-gray-300 px-5")
            for linha in array[1:][:3]:
                with tr(cls="text-center"):
                    for palavra in linha:
                        td(palavra, cls="text-center border-solid border-2 border-gray-300 px-5")
#cria a pagina HTMl
def criarPagina(qtdCargos,partidoPrefeito, idadeCandidato):

    dom = dominate.document(title='Eleicao')
    doc = open("index.html", "w") 



    cargos = qtdCargos

    partido = partidoPrefeito

    idade = idadeCandidato

    with dom.head:
        meta(charset="UTF-8")
        link(rel='stylesheet')
        script(src="https://cdn.tailwindcss.com") 
    with dom:
        with div(cls="flex flex-col gap-14 p-52"):
            gerarTabela(cargos)
            gerarGrade(partido)
            gerarTabela(idade)

    doc.write(str(dom))
    

def gerarTabela(array):
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
    with div(cls="grid grid-cols-2 grid-rows-auto"):
        div(array[0], cls="col-span-2 bg-gray-200 text-center font-bold text-4xl")
        for partido in array[1]:
            div(partido.title(), cls="border-2 border-gray-500 text-center text-xl")