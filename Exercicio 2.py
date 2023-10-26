# Peça para o usuário digitar três valores de temperatura e respectivos dias. Avalie qual é a maior temperatura e a menor. Mostre o resultado.
temperatura1 = float('-inf')
temperatura2 = float('inf')

for i in range(3):
    dia = input(f"Digite o dia da temperatura {i+1}: ")
    temperatura = float(input(f"Digite a temperatura {i+1}: "))

    if temperatura > temperatura1:
        temperatura1 = temperatura
    if temperatura < temperatura2:
        temperatura2 = temperatura

if temperatura1 != float('-inf'):
    print(f"A maior temperatura registrada foi: {temperatura1} °C")
else:
    print("Nenhuma temperatura registrada.")

if temperatura2 != float('inf'):
    print(f"A menor temperatura registrada foi: {temperatura2} °C")
else:
    print("Nenhuma temperatura registrada.")
