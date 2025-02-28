

lista_de_numeros: list = [10, 20, 80, -20, 70, -80, 5580, -46417, 3312]

def ordenar_lista_de_numeros(numeros: list) -> list:
    nova_lista_de_numeros = numeros.copy()

    for i in range(len(nova_lista_de_numeros)):
        for j in range(i+1, len(nova_lista_de_numeros)):
            if nova_lista_de_numeros[i] > nova_lista_de_numeros[j]:
                nova_lista_de_numeros[i], nova_lista_de_numeros[j] = nova_lista_de_numeros[j],nova_lista_de_numeros[i]

    return nova_lista_de_numeros

nova_lista = ordenar_lista_de_numeros(lista_de_numeros)
print(nova_lista)
