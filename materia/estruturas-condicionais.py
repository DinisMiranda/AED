# Estruturas Condicionais em Python

# Exemplo com if
numero = 10
if numero > 5:
    print("O número é maior que 5")

# Exemplo com if-else
numero = 3
if numero > 5:
    print("O número é maior que 5")
else:
    print("O número é menor ou igual a 5")

# Exemplo com if-elif-else
numero = 7
if numero > 10:
    print("O número é maior que 10")
elif numero > 5:
    print("O número está entre 6 e 10")
else:
    print("O número é 5 ou menor")

# Exemplo com match-case
# Disponível a partir do Python 3.10
dia = "segunda"
match dia:
    case "segunda":
        print("Hoje é segunda-feira")
    case "terça":
        print("Hoje é terça-feira")
    case "quarta" | "quinta":
        print("Hoje é meio da semana")
    case _:
        print("Outro dia qualquer")
