# Escreva um script Python ler dois números inteiros e exibir o resto da divisão do primeiro pelo segundo. Se o usuário quiser dividir um número por zero, faça a verificação de divisão por zero e informe que não é possível esta operação. 

try:
  num1 = int(input("Digite o primeiro número inteiro: "))
  num2 = int(input("Digite o segundo número inteiro: "))

  if num2 == 0:
      print("Não é possível dividir por zero.")
  else:
      resto = num1 % num2
      print(f"O resto da divisão de {num1} por {num2} é {resto}")

except ValueError:
  print("Por favor, digite números inteiros válidos.")

