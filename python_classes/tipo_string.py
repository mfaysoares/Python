"""
Tipo String

Em Python, é considerado um tipo string sempre que:
- Estiver entre aspas simples 'x'
- Estiver entre aspas duplas "x"
- Estiver entre aspas simples triplas '''x'''
- Estiver entre aspas duplas triplas
"""

nome, nome2 = 'Matheus Fay', "Soares"
nome3 = "Matheus' Deck Status"
print(nome3)
print(type(nome3))

#Pular uma linha usa-se \n
nome = "Matheus \nFay"
print(nome)
#ou
nome = """Matheus
Fay
Soares"""
print(nome)

aux = 'Matheus Fay Soares'
print(aux.upper()) #Coloca em maiusculo
print(aux.lower()) #Coloca em minusculo
print(aux.split()) #Transforma em uma lista de strings

# Acesso letras da string
# ['M','a','t','h','e','u','s']
# [0, 1, 2, 3, 4, 5, 6]
nome = "Matheus"
print(nome[0]) #M
print(nome[0:6]) #O último digito (6) ele não pega. Slice de string
print(nome[2:7]) #theus

#Split
nome = "Matheus Fay Soares 26 anos"
# ['Matheus', 'Fay', 'Soares', '26', 'anos']
# [0, 1, 2, 3, 4]
print(nome.split()) #['Matheus', 'Fay', 'Soares', '26', 'anos']
print(nome.split()[0]) #Matheus
print(nome.split()[1]) #Fay
print(nome.split()[2]) #Soares
print(nome.split()[3]) #26
print(nome.split()[4]) #anos

#Inverter a escrita
#[::-1] - Começa do primeiro elemento vai até o último e inverte
nome = 'Matheus Fay'
print(nome[::-1]) #yaF suehtaM

#Substituir
print(nome.replace('M','X'))