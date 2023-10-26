# Escreva um script Python para alterar a entrada de um número de CPF o seguinte formato:
# XXX,XXX.XXX-XX
# Repare que o número CPF tem pontos e traço.

# Pesquise sobre funções de manipulação de strings em Python e crie uma nova variável para receber o mesmo número de CPF porém sem os pontos e os traços.

cpf = input('insira seu cpf\n')
cpf = cpf.replace('.', '',).replace('-', '')
print(cpf)