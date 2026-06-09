import truques.input as inputt
def cadastrarProduto(animal,produto):
    nome_p = input ( "Qual o nome do produto? " ) .upper ( )
    pergunta_a = input ( 'Seu produto é um animal? ' ) .lower ( )

    if pergunta_a == 'sim':
        pergunta_a == 'não'
        tipo_a = input ( 'Qual o tipo do animal (bovino, caprino, suino, etc.)? ' ) .upper ( )
        identificacao_a = input ( 'Qual a identificação (brinco, marcação,etc.)? (Não coloque a indetificação igual a de outro animal!) ' ) .upper ( )
        achou = False
        for i in range ( len ( animal )  ) :
            if animal[i][2] == identificacao_a:
                print ( 'Animal já registrado!')
                print ( 'Apague o animal registrado ou use outra identificação!')
                achou = True
                break
        if not achou:
                
                peso_a = inputt.inputNumeroInt( 'Qual é o peso do seu animal em quilogramas? ' ) 
                valor_a = inputt.inputNumeroInt( 'Qual o valor por quilo em R$? ' ) 
                valorTotal = valor_a * peso_a
                animal.append ( [nome_p,tipo_a,identificacao_a,peso_a,valorTotal])
                
                print ( f'Animal: {nome_p}')
                print ( f'Tipo: {tipo_a}')
                print ( f'Indentificação: {identificacao_a}')
                print ( f'Peso: {peso_a}')
                print ( f'Valor: R$ {valorTotal}')
        else:
            achou = False 
            
    
    elif pergunta_a != 'sim':
            valor = inputt.inputNumeroInt( "Qual o valor do produto em R$? " )
            estoque = inputt.inputNumeroInt( "Qual a quantia do estoque do produto? " )
            produto.append ( [nome_p,valor,estoque])

            print ( '-'*50)
            print ( f'Produto:{nome_p}') 
            print ( f'Valor: R${valor}')
            print ( f'Em estoque:{estoque}')
            print ( '-'*50)
def interfaceADMinicio():
        print('-'*50)
        print('Aba do administrador')
        print('-'*50)
        print('Essas são as opções:')
        print('-'*50)
        print('1 Cadastrar administrador')
        print('2 Entrar')
        print('0 Sair')
        print('-'*50)
        

def interfaceADMacesso():   
        print ( 'Essas são as opções:')
        print ( '-'*50)
        print ( '1 Produtos')
        print ( '2 Produções')
        print ( '3 Estoque')
        print ( '0 Sair')
        print ( '-'*50)

def opcao1():
    print ( '-'*50)
    print ( 'Essas são as opções de produto:')
    print ( '-'*50)
    print ( '1 Cadastrar produto')
    print ( '2 Ver produtos')
    print ( '3 Editar produto')
    print ( '4 Remover produto')
    print ( '0 Sair')
    print ( '-'*50)

def opcao2(produto,animal):
    for p in produto:
        print ( f'Nome: {p[0]}\n Valor : R${p[1]}\n Em Estoque: {p[2]}')
        print ( '-'*50)

    for i in animal:
        print ( f'Nome: {i[0]}\n Tipo: {i[1]}\n Identificação: {i[2]}\n Peso: {i[3]}\n Valor: {i[4]}')
        print ( '-'*50)

def opcao3(produto,animal,achou):
    achou = False
    for p in produto:
        print ( f'Nome: {p[0]}\n Valor : R${p[1]}\n Em Estoque: {p[2]}')
        print ( '-'*50)

    for i in animal:
        print ( f'Nome: {i[0]}\n Tipo: {i[1]}\n Identificação: {i[2]}\n Peso: {i[3]}\n Valor: {i[4]}')
        print ( '-'*50)
    pesquisa = input ( 'Qual produto você quer editar? (Digite o nome se for PRODUTO e indentificação se for ANIMAL!) ' ) .upper ( )
    
    for p in range ( len ( produto )  ) :
        if produto[p][0] == pesquisa:
            produto.pop(p)
            achou = True
    for a in range ( len ( animal )  ) :
        if animal[a][2] == pesquisa:
            animal.pop(a)
            achou = True
    if achou:
        cadastrarProduto(animal,produto)
        

            

def opcao4(produto,animal):
    for p in produto:
        print ( f'Nome: {p[0]}\n Valor : R${p[1]}\n Em Estoque: {p[2]}')
        print ( '-'*50)

    for i in animal:
        print ( f'Nome: {i[0]}\n Tipo: {i[1]}\n Identificação: {i[2]}\n Peso: {i[3]}\n Valor: {i[4]}')
        print ( '-'*50)
    pesquisa = input ( 'Qual produto você quer apagar? (Digite o nome do produto corretamente!) ' ) .upper ( )
    
    for p in range ( len ( produto )  ) :
        if produto[p][0] == pesquisa:
            break
    for a in range ( len ( animal )  ) :
        if animal[a][2] == pesquisa:
            break

    if produto[p][0] == pesquisa:
        produto.pop(p)
        print ( '-'*50)
        print(f'Produto {pesquisa} removido.')
    elif animal[a][2] == pesquisa:
        animal.pop(a)
        print ( '-'*50)
        print(f'Animal {pesquisa} removido.')
    else:
        print('Produto inexistente ou digitado incorretamente!')