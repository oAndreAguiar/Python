# 1) No seu computador, encontre um diretório que contenham arquivos de imagens (extensões .jpg, .bmp etc).
# Após, encontre diretório com documentos de texto, por exemplo, extensões .txt ou .doc.
# Crie um script em Python que faça a contagem de arquivos por extensão.
# O usuário informa o diretório e a extensão dos arquivos para contagem e o script apresenta na tela o resultado.
# Exemplo:
# txt == 9

import os

def contar_arquivos_por_extensao(diretorio, extensao):
    contador = 0
    for raiz, diretorios, arquivos in os.walk(diretorio):
        for arquivo in arquivos:
            if arquivo.endswith(extensao):
                contador += 1
    return contador

diretorio = input("Digite o caminho do diretório: ")
extensao = input("Digite a extensão dos arquivos (por exemplo, .txt, .jpg): ")

quantidade = contar_arquivos_por_extensao(diretorio, extensao)
print(f"{extensao} == {quantidade}")
