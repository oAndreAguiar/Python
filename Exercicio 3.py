# 1) Escreva um script Python para receber como entrada de um número de telefone celular e utilize  uma expressão regular que permita o número apenas no seguinte formato:
# (24)9XXXX-XXXX
# Repare que o número de telefone tem parênteses, pontos, traço e inicia com o 9 após o DDD.

import re

def formato(numero):
    
    padrao = r'^\(\[0-9]{2}\)9\[0-9]{4}-\[0-9]{4}$'
   
    if re.match(padrao, numero):
        return "O número de telefone é válido."
    else:
        return "O numero de telefone esta incorreto"


telefone = input("Digite um número de telefone celular no formato (24)9XXXX-XXXX: ")


resultado = formato(telefone)
print(resultado)
