"""
Loop for
Loop-> Estrutura de repetição
For-> Uma dessas estruturas

Em Python:
for item in interavel:
    //Execução do loop

-Utilizamos loops para iterar sobre sequencia ou valores iteraveis
Exemplos de iteráveis:
    - Strings: nome = "Matheus"
    - Lista
    - Range
"""

nome = "Matheus Fay Soares"
lista = {1, 3, 5, 7, 9}
numeros = range(1,10)

#Exemplo de for 1
#Iterando em uma string
for letra in nome:
    print(letra)

#Exemplo de for 2
#Iterando em uma lista
for numero in lista:
    print(numero)

#Exemplo de for 3
#Iterando em um range
"""
range(valor_inicial, valor_final)
OBS: o valor final não é inclusive, logo não está incluso.
EXEMPLO: range(1,10)
1
2
3
4
5
6
7
8
9
10 - NAO VAI
"""
for num in numeros:
    print(num)

#Exemplo de for 4
for indice,letra in enumerate(nome):
    print(f'{indice} -> {letra}')

#Exemplo de for 5
#Em Python: Quando temos duas variáveis e queremos descartar uma, utilizamos underline (_)
for _,letra in enumerate(nome):
    print(letra.upper())

#Exemplo de for 6
for valor in enumerate(nome):
    print(valor)

#Exemplos de for 7
qtd = int(input("Quantas vezes esse loop deve rodar?"))
for n in range(1,qtd+1):
    print(f'Imprimindo {n}')

#Exemplo de for 8
soma = 0
for n in range(1,qtd+1):
    num = int(input(f'Informe o valor {n} de {qtd} valor: '))
    soma = soma + num
print(f'A soma é {soma}')

#Exemplo de for 9
#Imprimir todos os caracteres na mesma linha
#Por padrão, o print vem com \n. Para alterar, basta alterar o parâmetro end para " "
#help(print)
aux = "Débora"
for x in aux:
    print(x,end=" ")
print("\n")

#Exemplo 10
meu_nome = "Matheus"
print(meu_nome*3) #MatheusMatheusMatheus

#Exemplo 11
#Tabela de emojis unicode: https://apps.timwhitlock.info/emoji/tables/unicode
#Original = U+1F620
#Modificado = U0001F620

for _ in range(3):
    for num in range(1,11):
        print('\U0001F620' *num)
