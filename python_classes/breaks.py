"""
Saindo de Loops com breaks
Funciona da mesma forma que das linguagens C e Java

Utilizamos breaks para sair de loops de maneira projetada (forçada)
"""

#Exemplo 1 - For
for numero in range(1,11):
    if numero == 6:
        break
    else:
        print(numero)
print("Saiu do Loop")

#Exemplo 2 - While
while True:
    comando = input("Digite S para Sair:")
    if comando == "S":
        break
print("Sai do While")
