"""
Recebendo dados do usuário
Em Python, tudo recebido pelo usuário é no formato string.

Em Python, uma string é tudo que estiver entre:
- Aspas simples;
- Aspas duplas;
- Aspas simples triplas;
- Aspas duplas triplas;
"""

#Exemplos de print antigo
#Entrada de dados
print("Qual seu nome? ")
nome = input()
print("Qual sua idade %s ?" % nome)
idade = input()
print("Qual seu destino?")
city = input()

#Saída de Dados
print("Bem vindo a %s" % city)
print("O %s tem %s anos!" % (nome, idade)) #Quando tem mais de uma variável exige parenteses

#Exemplos de print moderno
print('Seja bem-vindo {0}'.format(nome))

#Exemplo de print mais atual
print(f'Seja bem-vindo {nome}')
print(f'O {nome} tem {idade} anos e mora em {city}\n'
      f'Nasceu no ano de {2020 - int(idade)}')
#int(idade)->cast
#Cast é a conversão de um tipo de dado para outro

nome2 = input("QUAL SEU APELIDO: ");
print(f'O apelido do {nome} é {nome2}')
idade2 = int(input("QUAL SUA IDADE MESMO: "))
print(f'O {nome2} nasceu em {2020 - idade2}')