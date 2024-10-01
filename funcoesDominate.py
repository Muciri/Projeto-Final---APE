import dominate
from dominate.tags import *

#cria a pagina HTMl
def criarPagina(qtdCargos, idadeCandidato):

    dom = dominate.document(title='Eleicao')
    doc = open("index.html", "w") 



    cargos = [ 
        ["Prefeito", "Vice-Prefeito", "Vereador"],
        qtdCargos
    ]


    idade = idadeCandidato

    with dom.head:
        link(rel='stylesheet', href='style.css')
        script(src="https://cdn.tailwindcss.com") 
    with dom:
        with body(cls="p-52"):
            gerarTabela(idade)
    #     with div():
    #         attr(cls='body')
    #         p('Lorem ipsum..')

    doc.write(str(dom))
    

def gerarTabela(array):
        with table(cls='table-auto text-center border-collapse'):
            with tr(cls="bg-gray-100"): 
                for head in array[0]:
                    th(head.title(), cls="text-center border-solid border-2 border-gray-300 px-5")
            for linha in array[1:][:3]:
                with tr(cls="text-center"):
                    for palavra in linha:
                        td(palavra, cls="text-center border-solid border-2 border-gray-300 px-5")



