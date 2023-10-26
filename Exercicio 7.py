#Crie um script que peca para o usuário inserir 10 números inteiros. Armazene estes números em um vetor.
#Depois, armazene em um dicionário o dobro do valor de cada posição no vetor. Use o índice do vetor como chave para o dicionário.  

valor = []

for i in range(2):
  numero = int(input(f"Insira {i+1}º valores inteiros:"))
  valor.append(numero)

dict = {}

for i in range(len(valor)):
  chave = i
  dobro = valor[i]*2
  dict[chave]= dobro

print("Estes são os dobros dos seus numeros")
print(dict)
