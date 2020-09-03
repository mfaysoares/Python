"""
Tipo Float
Tipo real, decimal
Casas decimais

OBS: o separador de casas decimais na programação é ponto e não a vírgula
"""

#Errado do ponto de vista do float, mas gera um tupla
valor = 1,44
print(valor)
print(type(valor))

#Correto do ponto de vista do float
valor = 1.44
print(valor)
print(type(valor))

#É possível fazer dupla atribuição
valor1, valor2 = 1,44
print(valor1)
print(valor2)
print(f'Valor 1 é {valor1} e Valor 2 é {valor2}')

#Podemos converter float para inteiro
"""
OBS: Ao converter os valor float para int, perde-se precisão
"""
valor = 2.56
valor2 = int(valor)
print(f'O {valor} em inteiro é {valor2}!')

#Arredondamento
print(dir(valor))
help(valor.__round__())
arredondamento = valor.__round__()
print(arredondamento)

#Podemos trabalhar com números complexos
x = 2 + 5j
print(type(x)) #retorna <class 'complex'>
