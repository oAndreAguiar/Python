# Crie um script que obtenha as informações de nome e matrícula de uma turma com 10 alunos.

# As informações de cada aluno devem estar em um dicionário. Crie um vetor que armazene todos os dicionários.

turma = []

for i in range(2):
  nome = input(f"Digite o nome do aluno {i+1}:")
  mat = input(f"Digite a matricula do aluno {i+1}:")

  aluno = {"Nome":nome, "Matricula":mat}
  turma.append(aluno)

for aluno in turma:
  print(f"Nome: {aluno['Nome']}, Matrícula: {aluno['Matricula']}")

