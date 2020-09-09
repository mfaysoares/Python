"""
Listas

Listas em Python funcionam como vetores/matrizes (arrays) em outras linguagens, com a diferença
de serem DINÂMICOS e também podemos trabalhar com QUALQUER tipo de dado.

Linguages C/Java: Arrays
    -Possuem tamanho e tipo de dado fixo;
    Ou seja, nestas linguagens se você criar um array do tipo int e com tamanho 5, este array será
    SEMPRE do tipo inteiro e poderá ter SEMPRE no máximo 5 valores.

Já em Python:
-Dinâmico: Não possui tamanho fixo; ou seja, podemos criar a lista e simplesmente ir adicionando elementos;
Enquanto houver memória disponível vai adicionando elementos;
-Qualquer tipo de dado: Não possuem tipo de dado fixo; ou seja, podemos colocar qualquer tipo de dado;

As listas em Python são representadas por colchetes: []
"""

type([])

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

lista2 = ['M', 'a', 't', 'h', 'e', 'u', 's', ' ', 'F', 'a', 'y']

lista3 = []

lista4 = list(range(11))

lista5 = list("Matheus Fay")

#Podemos facilmente checar se determinado valor está contido na lista
num = 88
if num in lista4:
    print(f"I've found the number {num}")
else:
    print(f"I haven't found the number {num}")

letra = 'M'
if letra in lista2:
    print(f"I've found character {letra}")
else:
    print(f"I haven't found the character {letra}")

#Podemos facilmente ordenar uma lista
print(dir(lista1))
lista1.sort()
print(lista1)

#Podemos facilmente contar o número de ocorrências de um valor em uma lista
#Conta quantos '1' tem na lista
print(lista1.count(1))
#Conta quantos 'a' tem na lista
print(lista2.count('a'))

#Adicionar elementos em listas
"""
Para adicionar elementos/valores em listas, utilizamos a função append()
OBS: com append nós só conseguimos adicionar 1 elemento por vez
"""
lista1.append(42)
print(lista1) #Adiciona 42 no final

#Lista dentro de outra lista
lista1.append(lista2) #Coloca a lista como elemento único (sublista)
print(lista1)
if lista2 in lista1:
    print("I've found the list")
else:
    print("I haven't found the list")

lista1.extend([123,44,67]) #Coloca cada elemento como valor adicional a lista
print(lista1)

#Podemos inserir um novo elemento na lista informando a posição do índice
#OBS: Não substitui o valor, somente é deslocado para direita
lista1.insert(2,'Novo valor')
print(lista1)

#Podemos facilmente juntar duas listas
lista6 = lista4 + lista5
print(lista6)

#Imprimindo a lista inversa
lista2.reverse()
print(lista2) #Forma1
print(lista4[::-1]) #Forma2

#Copiar uma lista
lista7 = lista2.copy()
print(lista7)

#Tamanho de uma lista
print(len(lista7))

#Podemos remover facilmente o último elemento de uma lista
#OBS: podemos fornecer a posição que queremos remover
#OBS: o pop não somente remove mas também o retorna
print(lista5)
lista5.pop()
print(lista5)
lista5.pop(5)
print(lista5)

#Converter string para ums lista
#Exemplo 1
curso = 'Programação em Python'
print(curso)
curso = curso.split()
print(curso)
#OBS: por padrão o split separa os elementos da lista pelo espaço entre elas

#Exemplo2
#Podemos informar qual é o separador
curso2 = "Programação,em,Python"
print(curso2)
curso2 = curso2.split(",")
print(curso2)

#Convertendo uma lista em string
curso3 = ['Matheus','Débora','Kátia','Jairo']
print(curso3)
curso3 = ' '.join(curso3) #Pega a lista curso3 coloca espaço e transforma em uma string
print(curso3)

curso4 = ['Matheus', 'Fay', 'Soares', '26 anos']
print(curso4)
curso4 = '*'.join(curso4) #Pega a lista curso4 coloca * e transforma em uma string
print(curso4)

#Podemos colocar qualquer tipo de dado em uma lista, inclusive misturando os dados
lista_mix = [1, 2.56, 'Olá', [26, 56, 32]]
print(lista_mix)

#Iterando sobre Listas
#Exemplo 1 - Utilizando for
lista_aux = [1, 6, 28, 44, 639]
for elemento in lista_aux:
    print(elemento)

#Exemplo2 - Utilizando while
carrinho = []
produto = " "
while produto != 'sair':
    print("Adicione um produto no carrinho ou digite sair para sair:")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)
for produto in carrinho:
    print(produto)

#Utilizando variáveis em lista
numeros = [1,2,3,4,5]
num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5
numeros = [num1, num2,num3,num4,num5]
print(numeros)

#Em listas, fazemos acesso aos elementos de forma indexada
#         0        1        2        3
cores = ['red', 'green', 'blue', 'yellow']
print(cores[0]) #red
print(cores[1]) #green
print(cores[2]) #blue
print(cores[3]) #yellow

for cor in cores:
    print(cor)

indice = 0
while indice<len(cores):
    print(f'[{indice}] -> {cores[indice]}')
    indice += 1

#Gerar índice em um for
for indice,cor in enumerate(cores):
    print(indice,cor)

#Listas aceitam repetição
lista8 = []
lista8.append(42)
lista8.append(42)
lista8.append(33)
lista8.append(33)
lista8.append(10)
print(lista8)

#Métodos não tão importante mas úteis
#Encontrar índice de um elemento em uma lista
lista_matheus = list('Matheus')
aux = 0
for ind in lista_matheus:
    print(f'[{aux}] : {ind}')
    if ind == 'u':
        break
    else:
        aux += 1
print(aux)

#Em qual índice da lista está o valor 6?
#OBS: Caso não tenha o elemento na lista, será apresentado erro
numeros2 = [5,6,7,8,9,10]
print(numeros2.index(6))

#Em qual índice da lista está o valor 9?
#OBS: Caso não tenha o elemento na lista, será apresentado erro
print(numeros2.index(9))

#Elementos repetidos
#OBS: retorna o indice do primeiro elemento encontrado
numeros3 = [5,6,7,8,9,10,5]
print(numeros3.index(5))

#Podemos fazer busca dentro de um range, ou seja, qual índice começar a buscar
print(numeros3.index(5,2)) #Procura o valor 5 a partir do indice 2
print(numeros3.index(5,3)) #Procura o valor 5 a partir do indice 3
print(numeros3.index(5,4)) #Procura o valor 5 a partir do indice 4

#Podemos fazer busca dentro de um range, com ínicio e fim
lista9 = [1, 2, 3, 4, 5, 6, 7, 3, 9, 12]
print(lista9.index(3,5,10))

#Revisão do slicing
#lista[inicio:fim:passo]
#Trabalhando com slice de lista com parâmetro 'início'
lista10 = [1,2,3,4]
print(lista10[1:]) #Começa no índice 1 e vai pegando todos os elementos restantes

#Trabalhando com slice de lista com parâmetro 'início' e 'final'
print(lista10[1:3]) #Começa no indice 1 e pega até o indice 2, indice 3 não vai

#Trabalhando com slice de lista com parâmetro 'início', 'final' e 'passo'
print(lista10[1::2]) #Começa no indice 1, percorre todos (:) com passo de 2
print(lista10[::2]) #Começa no indice 0, percorre todos (:) com passo de 2

#Soma, Valor Máximo* e Valor Mínimo*
#Se os valores forem todos inteiros ou reais
lista11 = [1,2,3,4,5,6]
print(sum(lista11)) #Soma
print(max(lista11)) #Valor Máximo
print(min(lista11)) #Valor Mínimo
print(len(lista11)) #Tamanho
print(sum(lista11)/len(lista11)) #Média

#Transforma uma lista em tupla
print(lista11)
print(type(lista11))
tupla = tuple(lista11)
print(tupla)
print(type(tupla))

#Desempacotamento de Listas
#OBS: Deve ter o mesmo número de variaveis e o mesmo numero de elementos
lista12 = [1,2,3]
num1,num2,num3 = lista12
print(num1)
print(num2)
print(num3)

#Copiando uma lista para outra
#Forma 1
lista = [1,2,3]
print(lista)
nova = lista.copy() #Copia a lista
nova.append(4) #Add 4 na lista copiada
print(nova)

#Forma 2
#Shallow Copy
#OBS: as alterações realizadas na nova acaba alterando a lista original
lista = [1,2,3]
nova = lista
nova.append(10) #Também altera a list lista
print(lista)
print(nova)