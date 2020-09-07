"""
Loop While

Forma geral:
while expressão_booleana:
    //execução do loop

O bloco do while será repetido enquanto a expressão booleana for verdadeira;

Expressões Booleanas são todas as expressão onde o resultado é verdadeiro ou falso.
EXEMPLOS:
    - num = 5
    - num <5 (False)
    - num <10 (True)
"""

#Exemplo 1
#OBS: Em um loop while, é importante que cuidemos dos critérios de parada. Como por exemplo loop infinito.
num = 1
while num<10:
    print(num)
    num += 1

#Exemplo 2
resposta = ' '
while resposta != 'Sim':
    resposta = input('Já acabou Jéssica?')