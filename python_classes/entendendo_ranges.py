"""
Ranges

- Precisamos conhecer os loops para utilizar o range;
- Precisamos conhecer o range para trabalhar melhor com o loop for;

Ranges são utilizados para gerar sequências de forma não aleatória, mas de forme especificada.

Forma geral:

#Forma 1
range(valor_de parada)
OBS: valor_de_parada não inclusive (início padrão é 0, passo de 1 em 1)

#Forma 2
range(valor_de_inicio, valor_de_parada)
OBS: início especificado pelo usuário

#Forma 3
range(valor_de_inicio, valor_de_parada, passo)
OBS: passo especificado pelo usuário

#Forma 4 (inversa)
range(valor_de_inicio, valor_de_parada, -passo)
"""

#Forma 1
for i in range(11):
    print(i)
print("\n")

#Forma 2
for j in range(1,11):
    print(j)
print("\n")

#Forma 3
for x in range(2,21,2):
    print(x)
print("\n")

#Forma 4
for y in range(10,1,-1):
    print(y)
print("\n")