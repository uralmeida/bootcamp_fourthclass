# bootcamp_dados
## O objetivo principal, é a consulta de dados para criação de projetos.
###### . Repositório modificado por IA.
---

###### . Referência de materiais ao final do documento.

---
## 1. Type Hint e Tipagem de Dados
O uso de Type Hint melhora a legibilidade e segurança do código, especificando os tipos de dados esperados em funções e variáveis. Na análise de dados, isso auxilia na prevenção de erros e melhora a compreensão do código por outros desenvolvedores.

### Exemplo sem Type Hint:
```python
idade = 30
altura = 1.75
nome = "Alice"
estudante = True
```

### Exemplo com Type Hint:
```python
idade: int = 30
altura: float = 1.75
nome: str = "Alice"
estudante: bool = True
```

## 2. Listas e Dicionários
Listas e dicionários são fundamentais para manipulação de dados, permitindo organizar e acessar informações de forma eficiente.

### Exemplo de dicionário em Python:
```python
cliente = {
    "nome": "João",
    "idade": 35,
    "cidade": "São Paulo"
}
print(cliente["nome"])  # Saída: João
```

## 3. Leitura de Arquivos
A leitura de arquivos é essencial para qualquer profissional que trabalha com dados. Abaixo, um exemplo de como ler um arquivo CSV em Python:

```python
import pandas as pd

df = pd.read_csv('dados.csv')
print(df.head())
```

## 4. Funções em Python para Dados
Funções ajudam na modularização do código e permitem reutilizar lógicas complexas de forma organizada.

### Exemplo de função para limpeza de dados:
```python
def limpar_texto(texto: str) -> str:
    return texto.strip().lower()

nomes = [" Alice ", "BOB", "Carlos"]
nomes_limpos = [limpar_texto(nome) for nome in nomes]
print(nomes_limpos)  # Saída: ['alice', 'bob', 'carlos']
```
## Referências
- [Material de Referência sobre Engenharia de Dados](https://github.com/lvgalvao/data-engineering-roadmap)

Este repositório é um ambiente de aprendizado e experimentação para melhorar habilidades em manipulação e análise de dados. Qualquer sugestão ou contribuição é bem-vinda!