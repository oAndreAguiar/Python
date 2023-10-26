# 1) Crie uma versão do código de exemplo SISTEMA DE CONTROLE DE PRODUTOS que receba os dados preenchendo os vetores e ainda salve as informações em arquivo conforme apresentado na aula 05. 
# O arquivo deve ser aberto em modo leitura ('r') ou escrita ('a'), de acordo com a operação.
# Pesquise no Google sobre "manipulação de arquivos em Python".
# Uma opção para ler os dados é utilizar a função readlines.
# Observação:
# Salve em uma linha o nome do produto e o preço. Exemplo:
# PROD1 5.99
# PROD2 2.50
# PROD3 19.80 
# Toda vez que o programa for executado, os dados no arquivo devem ser lidos e copiados para o vetor.


produtos = ['a']
comando = 0

while comando != 5:
    print('''
            [1] Listar produtos
            [2] Cadastrar produtos
            [3] Remover produto
            [4] Exportar lista
            [5] Sair
            '''
            )
    comando = int(input('Escolha uma opção:'))

    if comando == 1:
        for c, p in enumerate(produtos):
          print(f'Item {c}: {p}')

    elif comando == 2:
        print("O produto deve ser cadastrado no formato:\n"
              'Produto - Valor')
        produtos.append(input('Digite o produto a ser cadastrado\n'))

    elif comando == 3:
         produtos.pop(int(input('Digite o numero do produto que deseja REMOVER')))

    elif comando == 4:
          print("4")  
      # lista ="/home/runner/Atividade-6/pasta/lista.txt"
      # with open(lista) as p:   
      #   for l in produtos:
      #        p.write(str(l)+'\n')     
           
    elif comando == 5:
        break

    else: print("Escolha uma opção válida")

  
