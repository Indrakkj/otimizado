import completo

def opcao1Producao(p_producao,m_primas,ver_p):
    achou = False
    achou2 = False
    produto_p = input('Qual produto você quer produzir (queijo, mel, sucos, etc.)? ').upper()
    item = input('Qual é o principal item para produção (leite, sal, açucar, etc.)? ').upper()
    if p_producao != []:
        completo.cadastrarProducao()        
    elif p_producao == []:
        p_item = float(input(f'Qual a quantidade de {item} você tem em seu estoque? '))
        c = float(input(f'Qual a quantidade de {item} para fazer 1 {produto_p}? '))
        pr = float(input(f'Qual a quantidade de {produto_p} você quer fazer? ')) 
        calculo =  c * pr

        if calculo > p_item:
            print(f'Quantidade de {item} insuficiente!')
            print(f'Adicione mais {item}, ou diminua a produção de {produto_p}!')
        else:
            subtracao = p_item - calculo
            print('-'*50)
            print(f'Produto: {produto_p}\n Quantidade:{pr}\n Item necessário: {item}\n Quantidade de {item}: {p_item}\n Você usou {calculo} de {item} para fazer {pr} {produto_p}\n Você agora tem {subtracao} {item}\n')
            print('-'*50)
            m_primas.append([item,subtracao,c,produto_p])
            p_producao.append([produto_p,pr])
            ver_p.append(f'Produto: {produto_p}\n Item: {item}\n Estoque de {item}: {subtracao}\n Quantidade necessária por {produto_p}:{calculo}')
            pergunta = input('Quer colocar outro item (sim ou não)? ')
        while pergunta == 'sim':
            item = input('Qual é o outro item para produção (leite, sal, açucar, etc.)? ').upper()
            p_item = float(input(f'Qual a quantidade de {item} você tem em seu estoque? '))
            c = float(input(f'Qual a quantidade de {item} para fazer 1 {produto_p}? '))
            
            calculo =  c * pr

            if calculo > p_item:
                print(f'Quantidade de {item} insuficiente!')
            else:
                subtracao = p_item - calculo
                print('-'*50)
                print(f'Item necessário: {item}\n Quantidade de {item}: {p_item}\n Você usou {calculo} de {item} para fazer {pr} {produto_p}\n Você agora tem {subtracao} {item}\n')
                print('-'*50)
                m_primas.append([item,subtracao,c,produto_p])
                ver_p.append(f'Outro item: {item} --- Estoque de {item}: {subtracao}')
                pergunta = input('Quer colocar outro item (sim ou não)? ')

def opcao2Verproducao(p_producao):
    for p in p_producao:
        print ( f'Nome: {p[0]}\n Quantidade:{p[1]}')
        print ( '-'*50)

def opcao3Editarproduca(p_producao,):
    for p in p_producao:
        print ( f'Nome: {p[0]}\n Quantidade:{p[1]}')
        print ( '-'*50)

    pesquisa = input ( 'Qual produção você quer editar? (Digite o nome do produto corretamente!) ' ) .upper ( )
    for d in p_producao :
        if d[0] == pesquisa:
            achou = False
    achou2 = False
    produto_p = input('Qual produto você quer produzir (queijo, mel, sucos, etc.)? ').upper()
    item = input('Qual é o principal item para produção (leite, sal, açucar, etc.)? ').upper()
    if p_producao != []:
        completo.cadastrarProducao()
        print('Produção atualizada!')

    for p in p_producao:
        if p[0] == pesquisa:
            p_producao.remove(p)
            break
            
        else:
            print("Produto não existe!")

def opcao4Removerproducao(p_producao):
    for p in p_producao:
        print ( f'Nome: {p[0]}\n Quantidade:{p[1]}')
        print ( '-'*50)

    pesquisa = input ( 'Qual produção você quer remover? (Digite o nome do produto corretamente!) ' ) .upper ( )
    for p in p_producao:
        if p[0] == pesquisa:
            p_producao.remove(p)
            print ( '-'*50)
            print(f'Produto {pesquisa} removido.')
            print ( '-'*50)
            break
        else:
            print ( '-'*50)
            print('Produto inexistênte!')
            print ( '-'*50)
def opcao5Produzir(p_producao,m_primas):
    for p in p_producao:
        print ( f'Nome: {p[0]}\n Quantidade:{p[1]}')
        print ( '-'*50)

    pesquisa = input ( 'Qual produto você quer produzir? (Digite o nome do produto corretamente!) ' ) .upper ( )
    for p in range( len ( p_producao )  ) :
        if p_producao[p][0] == pesquisa:
            pr = int(input(f'Qual a quantidade de {pesquisa} você quer produzir? '))
            p_producao[p][1] += pr
            print ( f'Nome: {p_producao[p][0]}\n Quantidade:{p_producao[p][1]}')
            print ( '-'*50)
            break
    for m in range( len ( m_primas )  ) :
        if m_primas[m][3] == pesquisa:
            calculo = m_primas[m][2] * pr
            if calculo > m_primas[m][1]:
                print(f'Quantidade de {m_primas[m][1]} insuficiente!')
            else:
                m_primas[m][1] -= calculo
                print('-'*50)