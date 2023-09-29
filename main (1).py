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

  