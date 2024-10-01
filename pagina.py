import pandas as pd
import dominate
from dominate.tags import *

dom = dominate.document(title='Eleicao')
doc = open("index.html", "w") 



array = [
    ['home', 'about', 'contact'],
    ["Alfreds Futterkiste",
    "Maria Anders",
    "Germany"],
    ["Centro comercial Moctezuma",
     "Francisco Chang",
    "Mexico"
    ],
]

with dom.head:
    link(rel='stylesheet', href='style.css')
    script(src="https://cdn.tailwindcss.com") 

with dom:
    with body(cls="flex justify-center items-center p-52"):
        with table(cls='table-auto text-center border-collapse'):
            with tr(cls="bg-gray-100"): 
                for head in array[0]:
                    th(head.title(), cls="text-center border-solid border-2 border-gray-300 px-5")
            for linha in array[1:]:
                with tr(cls="text-center"):
                    for palavra in linha:
                        td(palavra, cls="text-center border-solid border-2 border-gray-300 px-5")
        
#     with div():
#         attr(cls='body')
#         p('Lorem ipsum..')

doc.write(str(dom))