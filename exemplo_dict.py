

from typing import Dict, Optional, Any

produto_01: Dict[str, [str]]

import json

lista: Any = ["Sapato", 39, 10.38, True]

produto_01: Dict[str, Any] = {

    "nome" : "televisão",
    "quantidade" : 12,
    "preço" : 279.12,
    "disponibilidade" : True

}
 
produto_02: dict ={

    "nome" : "notebook",
    "quantidade" : 19,
    "preço" : 321.80,
    "disponibilidade" : False

}

produto_03: dict = {

    "nome" : "fogão",
    "quantidade" : 8,
    "preço" : 42.15,
    "disponibilidade" : True

}

carrinho: list = []

carrinho.append(produto_01)
carrinho.append(produto_02)

carrinho_json = json.dumps(carrinho)
print(carrinho_json)
