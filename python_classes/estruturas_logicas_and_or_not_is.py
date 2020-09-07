"""
Estruturas Lógicas: and(e), or(ou), not(não), is(é)

Operadores unários:
    - not;
Operadores binários:
    - or;
    - and;
    - is;

Para o and, ambos os valores precisam ser True
Para o or, um ou outro valor precisa ser True
Para o not, o valor do Booleano é invertido
"""

ativo = False
logado = True

if ativo and logado:
    print("Bem vindo usuário!")
else:
    print("Você precisa ativar sua conta, por favor cheque seu e-mail!")

if ativo or logado:
    print("Bem vindo usuário! [OR]")
else:
    print("Você precisa ativar sua conta, por favor cheque seu e-mail! [OR]")

if not ativo:
    print("Você precisa ativar sua conta![NOT]")
else:
    print("Bem-vindo usuário!")

if ativo is True:
    print("Bem-vindo usuário!")
else:
    print("Você precisa checar sua conta! [IS]")