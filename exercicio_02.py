### Exercícios de Listas e Dicionários

#1. Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.
#2. Dada a lista `["Python", "Java", "C++", "JavaScript"]`, remova o item "C++" e adicione "Ruby".
#3. Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.

from typing import Dict, Any

livro: Dict[str, Any] = {

    "Título" : "Livro Python",
    "Autor" : "Jeferson",
    "Ano Publicado" : 2020
    
    }

        #print(livro)

lista_de_livros_usando_dict:dict = {

    "Livro 01" : {
    "Título" : "Livro Python",
    "Autor" : "Jeferson",
    "Ano Publicado" : 2020},

    "Livro 02" : {
    "Título" : "Livro SQL",
    "Autor" : "Almeida",
    "Ano Publicado" : 2019}

}

print(lista_de_livros_usando_dict["Livro 02"]["Título"])


#4. Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.




#5. Dada a lista `["maçã", "banana", "cereja"]` e o dicionário `{"maçã": 0.45, "banana": 0.30, "cereja": 0.65}`, calcule o preço total da lista de compras.