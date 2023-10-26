# peça para o usuário digitar o nome de uma disciplina, por exemplo PCA, e mais dois valores que representam a nota da AV1 (prova) e AV2.

# a) Calcule a média e apresente o resultado na tela.

materia = input("Digite qual é a materia:")
av1 = int(input("Digite a nota da av1:"))
av2 = int(input("Digite a nota da av2:"))
media= (av1 + av2) / 2
print(f"sua média é:{media}")

