"""
Escopo de variáveis

Dois casos de escopo de variávies:
1 - Variáveis globais;
    - Seu escopo compreende todo o programa
2 - Variáveis locais
    - São reconhecidas apenas no bloco onde foram declaradas, ou seja, seu escopo está limitado ao
    bloco onde foi declarada

Para declarar variáveis em Python, fazemos:
nome_da_variavel = valor_da_variavel

Python é uma linguagem de tipagem dinâmica. Isso significa que ao declarar uma variável, nós não colocamos
o tipo de dado dela. Esse tipo é inferido ao atribuirmos a mesma.
Exemplo em c: int numero = 42
Exemplo em Python: numero = 42
"""

numero = 42 #Exemplo de variável global
print(numero)
print(type(numero))

numero2 = "Matheus"
print(numero2)
print(type(numero2))

#Exemplo de variável local
#A variável novo está declarada dentro do condicional if, logo é uma variável local
if numero>10:
    novo = numero + 10
    print(novo)