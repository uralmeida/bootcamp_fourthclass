

produto_01: dict = {

    "nome" : "televisão",
    "quantidade" : 12,
    "preço" : 279.12,
    "disponibilidade" : True

}
 
produto_02: dict = {

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

print(carrinho)