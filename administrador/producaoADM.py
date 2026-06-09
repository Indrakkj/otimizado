import truques.input as inputt
m_primas = []
ver_p = []
def opcao1Producao(p_producao,m_primas,ver_p,material):
    achou = False
    achou2 = False
    produto_p = input('Qual produto você quer produzir (queijo, mel, sucos, etc.)? ').upper()
    item = input('Qual é o principal item para produção (leite, sal, açucar, etc.)? ').upper()
    if p_producao != []:
        for p in range ( len ( m_primas )  ) :
            if m_primas[p][0] == item:
                achou = True
                break
                
        if achou:    
            inputt.inputNumeroInt(f'Qual a quantidade de {item} para fazer 1 {produto_p}? ')
            pr = inputt.inputNumeroInt(f'Qual a quantidade de {produto_p} você quer fazer? ')
            calculo =  c * pr
            achou = False
            
            if calculo > m_primas[p][1]:
                print(f'Quantidade de {item} insuficiente!')
                print(f'Adicione mais {item}, ou diminua a produção de {produto_p}!')
            else:
                subtracao = m_primas[p][1] - calculo
                print('-'*50)
                print(f'Produto: {produto_p}\n Quantidade:{pr}\n Item necessário: {item}\n Quantidade de {item}: {m_primas[p][1]}\n Você usou {calculo} de {item} para fazer {pr} {produto_p}\n Você agora tem {subtracao} {item}\n')
                print('-'*50)
                m_primas[p] = [item,subtracao,c,produto_p]
                p_producao.append([produto_p,pr])
                ver_p.append(f'Produto: {produto_p} --- Item: {item} --- Estoque de {item}: {subtracao}')
                pergunta = input('Quer colocar outro item (sim ou não)? ').lower
                
            while pergunta == 'sim':
                item = input('Qual é o outro item para produção (leite, sal, açucar, etc.)? ').upper()
                for i in range ( len ( m_primas )  ) :
                    print(m_primas[i][0])
                    if m_primas[i][0] == item:
                        achou2 = True
                        break
                        
                if achou2:
                    c = inputt.inputNumeroInt(f'Qual a quantidade de {item} para fazer 1 {produto_p}? ')
                        
                    calculo =  c * pr
                    achou2 = False

                    if calculo > m_primas[i][1]:
                        print(f'Quantidade de {item} insuficiente!')
                        print(f'Adicione mais {item}, ou diminua a produção de {produto_p}!')
                        


                    else:
                        subtracao = m_primas[i][1] - calculo
                        print('-'*50)
                        print(f'Outro Item: {item}\n Quantidade de {item}: {m_primas[i][1]}\n Você usou {calculo} de {item} para fazer {pr} {produto_p}\n Você agora tem {subtracao} {item}\n')
                        print('-'*50)
                        m_primas.append([item,subtracao,c,produto_p])
                        ver_p.append(f'Outro item: {item} --- Estoque de {item}: {subtracao}')
                        pergunta = input('Quer colocar outro item (sim ou não)? ')

                else:
                    p_item = inputt.inputNumeroInt(f'Qual a quantidade de {item} você tem em seu estoque? ')
                    c = inputt.inputNumeroInt(f'Qual a quantidade de {item} para fazer 1 {produto_p}? ')
                    pr = inputt.inputNumeroInt(f'Qual a quantidade de {produto_p} você quer fazer? ') 
                    calculo =  c * pr

                    if calculo > p_item:
                        print(f'Quantidade de {item} insuficiente!')
                        print(f'Adicione mais {item}, ou diminua a produção de {produto_p}!')
                    else:
                        subtracao = p_item - calculo
                        print('-'*50)
                        print(f'Outro item: {item}\n Quantidade de {item}: {p_item}\n Você usou {calculo} de {item} para fazer {p} {produto_p}\n Você agora tem {subtracao} {item}\n')
                        print('-'*50)
                        p_producao.append([produto_p,pr])
                        m_primas.append([item,subtracao,c,produto_p])
                        ver_p.append(f'Outro item: {item} --- Estoque de {item}: {subtracao}')
                        pergunta = input('Quer colocar outro item (sim ou não)? ')
                        
        else:
            p_item = inputt.inputNumeroInt(f'Qual a quantidade de {item} você tem em seu estoque? ')
            c = inputt.inputNumeroInt(f'Qual a quantidade de {item} para fazer 1 {produto_p}? ')
            pr = inputt.inputNumeroInt(f'Qual a quantidade de {produto_p} você quer fazer? ') 
            calculo =  c * pr

            if calculo > p_item:
                print(f'Quantidade de {item} insuficiente!')
                print(f'Adicione mais {item}, ou diminua a produção de {produto_p}!')
            else:
                subtracao = p_item - calculo
                print('-'*50)
                print(f'Outro item: {item}\n Quantidade de {item}: {p_item}\n Você usou {calculo} de {item} para fazer {p} {produto_p}\n Você agora tem {subtracao} {item}\n')
                print('-'*50)
                p_producao.append([produto_p,pr])
                m_primas.append([item,subtracao,c,produto_p])
                ver_p.append(f'Outro item: {item} --- Estoque de {item}: {subtracao}')
                pergunta = input('Quer colocar outro item (sim ou não)? ')
        while pergunta == 'sim':
                item = input('Qual é o outro item para produção (leite, sal, açucar, etc.)? ').upper()
                for i in range ( len ( m_primas )  ) :
                    if m_primas[i][0] == item:
                        achou2 = True
                        break 

                if achou2:
                    c = inputt.inputNumeroInt(f'Qual a quantidade de {item} para fazer 1 {produto_p}? ')
                        
                    calculo =  c * pr
                    achou2 = False

                    if calculo > m_primas[i][1]:
                        print(f'Quantidade de {item} insuficiente!')
                        print(f'Adicione mais {item}, ou diminua a produção de {produto_p}!')
                        


                    else:
                        subtracao = m_primas[i][1] - calculo
                        print('-'*50)
                        print(f'Outro Item: {item}\n Quantidade de {item}: {m_primas[i][1]}\n Você usou {calculo} de {item} para fazer {pr} {produto_p}\n Você agora tem {subtracao} {item}\n')
                        print('-'*50)
                        m_primas.append([item,subtracao,c,produto_p])
                        ver_p.append(f'Outro item: {item} --- Estoque de {item}: {subtracao}')
                        pergunta = input('Quer colocar outro item (sim ou não)? ')

                else:
                    p_item = inputt.inputNumeroInt(f'Qual a quantidade de {item} você tem em seu estoque? ')
                    c = inputt.inputNumeroInt(f'Qual a quantidade de {item} para fazer 1 {produto_p}? ')
                    pr = inputt.inputNumeroInt(f'Qual a quantidade de {produto_p} você quer fazer? ') 
                    calculo =  c * pr

                    if calculo > p_item:
                        print(f'Quantidade de {item} insuficiente!')
                        print(f'Adicione mais {item}, ou diminua a produção de {produto_p}!')
                    else:
                        subtracao = p_item - calculo
                        print('-'*50)
                        print(f'Outro item: {item}\n Quantidade de {item}: {p_item}\n Você usou {calculo} de {item} para fazer {pr} {produto_p}\n Você agora tem {subtracao} {item}\n')
                        print('-'*50)
                        m_primas.append([item,subtracao,c,produto_p])
                        ver_p.append(f'Outro item: {item} --- Estoque de {item}: {subtracao}')
                        pergunta = input('Quer colocar outro item (sim ou não)? ')       
    elif p_producao == []:
        p_item = inputt.inputNumeroInt(f'Qual a quantidade de {item} você tem em seu estoque? ')
        c = inputt.inputNumeroInt(f'Qual a quantidade de {item} para fazer 1 {produto_p}? ')
        pr = inputt.inputNumeroInt(f'Qual a quantidade de {produto_p} você quer fazer? ') 
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
            p_item = inputt.inputNumeroInt(f'Qual a quantidade de {item} você tem em seu estoque? ')
            c = inputt.inputNumeroInt(f'Qual a quantidade de {item} para fazer 1 {produto_p}? ')
            
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
    for p in p_producao:
        nome = p[0]
        qtd_p = p[1]
        material.update({"Nome do Produto":nome,"Quantidade do Produto": qtd_p})
    for m in m_primas:
        nome_mp = m[0]
        qtd = m[1]
        qtd_por_p = m[2]
        material.update({"Matéria Prima":nome_mp,"Quantidade de Matéria Prima": qtd, "Quantidade por Produto": qtd_por_p})
    print(f'MTERIAL{material}')
def opcao2Verproducao(p_producao):
    for p in p_producao:
        print ( f'Nome: {p[0]}\n Quantidade:{p[1]}')
        print ( '-'*50)

def opcao3Editarproducao(p_producao,material):
    for p in p_producao:
        print ( f'Nome: {p[0]}\n Quantidade:{p[1]}')
        print ( '-'*50)

    pesquisa = input ( 'Qual produção você quer editar? (Digite o nome do produto corretamente!) ' ) .upper ( )
    achou = False
    for d in p_producao :
        if d[0] == pesquisa:
            achou = True
    if achou:
        opcao1Producao(p_producao,m_primas,ver_p,material)
        print('Produção atualizada!')

        for p in p_producao:
            if p[0] == pesquisa:
                p_producao.remove(p)
        for m in material:
            if m["Nome do Produto"] == pesquisa:
                del material[m]
                break
            
    else:
        print("Produto não existe!")
    

def opcao4Removerproducao(p_producao,material):
    for p in p_producao:
        print ( f'Nome: {p[0]}\n Quantidade:{p[1]}')
        print ( '-'*50)

    pesquisa = input ( 'Qual produção você quer remover? (Digite o nome do produto corretamente!) ' ) .upper ( )
    for p in p_producao:
        if p[0] == pesquisa:
            for m in material :
                del material[m]
            p_producao.remove(p)
            print ( '-'*50)
            print(f'Produto {pesquisa} removido.')
            print ( '-'*50)
            break
        else:
            print ( '-'*50)
            print('Produto inexistênte!')
            print ( '-'*50)
def opcao5Produzir(p_producao,material):
    for p in p_producao:
        print ( f'Nome: {p[0]}\n Quantidade:{p[1]}')
        print ( '-'*50)

    pesquisa = input ( 'Qual produto você quer produzir? (Digite o nome do produto corretamente!) ' ) .upper ( )
    for m in material :
        if m["Nome do Produto"] == pesquisa:
            pr = int(input(f'Qual a quantidade de {pesquisa} você quer produzir? '))
            m["Quantidade do Produto"] += pr
            print ( f'Nome: {m["Nome do Produto"]}\n Quantidade:{m["Quantidade do Produto"]}')
            print ( '-'*50)
            break
    for m in material:
        if m["Matéria Prima"] == pesquisa:
            calculo = m["Quantidade por Produto"] * pr
            if calculo > m["Quantidade de Matéria Prima"]:
                print(f'Quantidade de {m["Quantidade de Matéria Prima"]} insuficiente!')
            else:
                m["Quantidade de Matéria Prima"] -= calculo
                print('-'*50)

