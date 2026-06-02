def opcao1Verestoque(m_primas):
    for m in m_primas:
        print ( f'Nome: {m[0]}\n Quantidade:{m[1]}')
        print ( '-'*50) 

def opcao2Adicionarestoque(m_primas):
    for m in m_primas:
        print ( f'Nome: {m[0]}\n Quantidade:{m[1]}')
        print ( '-'*50)

    pesquisa = input ( 'Qual produto você quer adicionar mais estoque? (Digite o nome do produto corretamente!) ' ) .upper ( )
    for m in m_primas  :
        if m[0] == pesquisa:

            print ( f'Nome: {m[0]}\n Quantidade:{m[1]}')
            print ( '-'*50)
            m[1] += int(input(f'Qual a quantidade de {m[0]} você quer adicionar? '))
            print ( '-'*50)
            print("Estoque atualizado!")
            print ( '-'*50)
            print ( f'Nome: {m[0]}\n Quantidade:{m[1]}')
            print ( '-'*50)

def opcao3Removerestoque(m_primas):
    for m in m_primas:
        print ( f'Nome: {m[0]}\n Quantidade:{m[1]}')
        print ( '-'*50)

    pesquisa = input ( 'Qual produto você quer remover parte do estoque? (Digite o nome do produto corretamente!) ' ) .upper ( )
    for m in m_primas  :
        if m[0] == pesquisa:

            print ( f'Nome: {m[0]}\n Quantidade:{m[1]}')
            print ( '-'*50)
            m[1] -= int(input(f'Qual a quantidade de {m[0]} você quer remover? '))
            print ( '-'*50)
            print("Estoque atualizado!")
            print ( '-'*50)
            print ( f'Nome: {m[0]}\n Quantidade:{m[1]}')
            print ( '-'*50)
        else:
            print ( '-'*50)
            print('Produto inexistênte!')
            print ( '-'*50)    