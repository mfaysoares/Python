"""
Tipo Booleano

Algebra Booleana, criada por George Boole
2 constantes, verdadeiro ou falso

Em Python:
True: Verdadeiro
False: Falso

OBS: True e False sempre com as iniciais maiúsculas
"""

ativo = True
print(ativo)

"""
Operações básicas
"""

#Negação (not):
"""
Fazendo a negação, se o valor for verdadeiro o resultado será falso,
se for falso será verdadeiro
"""
print(not ativo)

#Ou (or):
"""
É uma operação binária, ou seja, depende de dois valores. Um ou o
outro deve ser verdadeiro

True or True: True
True or False: True
False or True: True
False or False: False
"""
logado = False
print(ativo or logado)

#E (and):
"""
Também é uma operação binária, ou seja, depende de dois valores. Ambos os
valores devem ser verdadeiro.

True and True: True
True an False: False
False and True: False
False and False: True
"""
print(logado and ativo)