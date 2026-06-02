import administrador.producaoADM as producaoADM
import administrador.produtoADM as produtoADM
import administrador.estoqueADM as estoqueADM
administrador = [['henrique','henrique114'],['pedro','pedro2245']]
produto = []
nome_p = ''
animal = []
p_producao = []
m_primas = []
qtd_item = []
ver_p = []
cliente = []
encontrado = False
acesso = False
achou = False

def acessoUsuario(escolhaADMouC,acesso):
    while True:

        nome = input("Digite um nome de usuário válido: ")
        nome_existe=False
        for r in range(len(escolhaADMouC)):
            if escolhaADMouC[r][0] == nome: 
                
                nome_existe = True
                break
        if nome_existe:
                print('Esse nome ja pertence a outro usuário!')

        else:
            senha = input("Digite sua senha: ")
            confirm_senha = input("Confirme sua senha: ")
        

            if senha != confirm_senha:
                print("Senha inválida.")

            else:
                escolhaADMouC.append([nome, senha])
                print("Cadastro concluído com sucesso!")
                acesso = True
                return acesso 

def entrar(escolhaADMouC,acesso):
        while True:
            print ( '-'*50)
            print('Login do administrador:')
            print('(0 para Sair)')
            print ( '-'*50)
            nome = input('Usuário: ')
            if nome == "0":
                    print('Ok!')
                    break
            else:
                print ( '-'*50)
                senha = input('Senha: ')
                acesso = False
                print ( '-'*50)
                for i in escolhaADMouC:
                    if nome == i[0] and senha == i[1]:
                        acesso = True
                        return acesso
                        
                if not acesso:
                    print('Senha ou usuário inválido!')
                return acesso

def cadastrarProduto():
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
                
                peso_a = float ( input ( 'Qual é o peso do seu animal em quilogramas? ' ) )
                valor_a = float ( input ( 'Qual o valor por quilo em R$? ' ) )
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
            valor = float ( input ( "Qual o valor do produto em R$? " ) )
            estoque = float ( input ( "Qual a quantia do estoque do produto? " ) )
            produto.append ( [nome_p,valor,estoque])

            print ( '-'*50)
            print ( f'Produto:{nome_p}') 
            print ( f'Valor: R${valor}')
            print ( f'Em estoque:{estoque}')
            print ( '-'*50)
            print ( 'Produto atualizado!')
            produto.pop(p)
            animal.pop(a)
            
    else:
        print('Produto não encontrado')

def cadastrarProducao(produto_p):
        
    for p in range ( len ( m_primas )  ) :
        if m_primas[p][0] == item:
            achou = True
            break
            
    if achou:    
        c = float(input(f'Qual a quantidade de {item} para fazer 1 {produto_p}? '))
        pr = float(input(f'Qual a quantidade de {produto_p} você quer fazer? ')) 
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
                c = int(input(f'Qual a quantidade de {item} para fazer 1 {produto_p}? '))
                    
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
                    print(f'Outro item: {item}\n Quantidade de {item}: {p_item}\n Você usou {calculo} de {item} para fazer {p} {produto_p}\n Você agora tem {subtracao} {item}\n')
                    print('-'*50)
                    p_producao.append([produto_p,pr])
                    m_primas.append([item,subtracao,c,produto_p])
                    ver_p.append(f'Outro item: {item} --- Estoque de {item}: {subtracao}')
                    pergunta = input('Quer colocar outro item (sim ou não)? ')
                    
    else:
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
                c = int(input(f'Qual a quantidade de {item} para fazer 1 {produto_p}? '))
                    
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
                    print(f'Outro item: {item}\n Quantidade de {item}: {p_item}\n Você usou {calculo} de {item} para fazer {p} {produto_p}\n Você agora tem {subtracao} {item}\n')
                    print('-'*50)
                    m_primas.append([item,subtracao,c,produto_p])
                    ver_p.append(f'Outro item: {item} --- Estoque de {item}: {subtracao}')
                    pergunta = input('Quer colocar outro item (sim ou não)? ')

while True:
    print('Bem vindo ao sistema Mais Pecuárea!')
    print('-'*50)
    print('Essas são as opções:')
    print('1 Cliente')
    print('2 Administrador')
    print('-'*50)
    opcao = int(input("Qual opção você quer? "))
    if opcao == 1:
        while True:
            print("Olá, cliente! Bem-vindo ao site + Pecoaria.")
            print("-" * 50)
            print("--- ABA DE LOGIN ---")
            print("1 - Cadastrar")
            print("2 - Login")
            print("0 - Sair")
            print("-" * 50)

            aba = input("Escolha uma opção para prosseguir: ")

            if aba == "1":

                acessoUsuario(cliente,acesso)

            elif aba == "2":
                while True:
                    print ( '-'*50)
                    print('Login do cliente:')
                    print('(0 para Sair)')
                    print ( '-'*50)
                    nome = input('Usuário: ')
                    if nome == "0":
                            print('Ok!')
                            break
                    else:
                        entrar(cliente)

            elif aba == "0":
                print("Até mais!")
                quit()

            else:
                print("Digite uma das opções acima.")
                continue
            dinheiro = 0

            while True:

                voltar_comprar = input("Deseja ir para a aba de compras? ").lower()

                if voltar_comprar == "sim":

                    print(f"Saldo da conta: R$ {dinheiro}")

                    while True:
                        numeros = "1234567890"
                        dinheiro_valido = True
                        dinheiro1 = input("Quanto de saldo deseja por na sua conta? ")
                        for d in dinheiro1:
                            if d not in numeros:
                                dinheiro_valido = False
                        if dinheiro_valido and dinheiro1 != "":
                            dinheiro1 = int(dinheiro1)
                            if dinheiro1 >=0:
                                dinheiro+= dinheiro1
                                print(f"Saldo atualizado com sucesso! Saldo atual: R$ {dinheiro}")
                                break
                        else:
                            print("Saldo nao possivel de adicionar.Tente novamente")
                            
                    
                    animalOUproduto= input("Deseja comprar produto ou animal: ")

                    if animalOUproduto == "produto":
                        print("Itens disponíveis:")

                        for i, p in enumerate(produto, start=1):

                            print(f"{i} - {p[0]} | preço: R$ {p[1]}| estoque: {p[2]} ")

                        escolha = int(input("Qual produto deseja comprar? (1 , 2...): "))

                        quantidade = int(input("Quantidade da compra: "))

                        print("Antes de efetuar o pagamento, confira as formas de pagamento:")
                        print("1 - Pix: desconto de 5%")
                        print("2 - Cartão: desconto de 10%")

                        desconto = 0
                       

                        tipo_de_pagamento = input("Escolha uma opção de pagamento: ")

                        if tipo_de_pagamento == "1":

                                desconto = 0.05
                                if escolha < 1 or escolha > len(produto):
                                    print("produto nao encontrado")
                                elif produto != []:
                                    produto_escolha = produto[escolha - 1]
                                    nome = produto_escolha[0]
                                    estoque = produto_escolha[2]
                                    preco = produto_escolha[1]

                                    if quantidade <= estoque:

                                        estoque -= quantidade
                                        produto_escolha[2] -= quantidade

                                        valor_total = preco * quantidade
                                        valor_desc = valor_total * desconto
                                        valor_final = valor_total - valor_desc

                                        if dinheiro >= valor_final:

                                            dinheiro -= valor_final

                                            print(f"Sua compra foi realizada com sucesso! Valor final: R$ {valor_final}")

                                            print(f"Produto adquirido: {produto_escolha[0]} | Quantidade: {quantidade}")

                                            fretes = [89.90, 19.99, 0]

                                            print("Escolha a opção de entrega desejada:")
                                            print("1 - Fast: entrega em até 8 dias | frete: R$ 89,90")
                                            print("2 - Medium: entrega em até 16 dias | frete: R$ 19,99")
                                            print("3 - Slow: entrega em até 30 dias | frete grátis")

                                            while True:

                                                transporte = int(input("Escolha sua transportadora: "))

                                                if transporte == 1 and dinheiro >= 89.90:

                                                    dinheiro -= fretes[0]

                                                    print("Entrega Fast selecionada. Obrigado pela preferência!")
                                                    break

                                                elif transporte == 2 and dinheiro >= 19.99:

                                                    dinheiro -= fretes[1]

                                                    print("Entrega Medium selecionada. Obrigado pela preferência!")
                                                    break

                                                elif transporte == 3:

                                                    dinheiro -= fretes[2]

                                                    print("Entrega Slow selecionada. Obrigado pela preferência!")
                                                    break

                                                else:

                                                    print("Transportadora indisponível ou saldo insuficiente.")
                                                    continue

                                        elif dinheiro < valor_final:

                                            p[2] += quantidade

                                            print("Saldo insuficiente.")
                                            continue
                                
                                    else:

                                        print("Estoque insuficiente.")
                                        continue
                                
                        elif tipo_de_pagamento == "2":

                            while True:

                                valido = True

                                cartao = input("Adicione os dados do cartão: ")

                                cartao_sem_espaco = cartao.replace(" ", "")

                                for i in cartao_sem_espaco:

                                    if i not in "0123456789":
                                        valido = False

                                if len(cartao_sem_espaco) == 16 and valido == True:

                                    desconto = 0.1

                                    print("Cartão adicionado com sucesso!")
                                    break

                                else:
                                    print("Cartão inválido.")
                                    continue
                            if escolha < 1 or escolha > len(produto):
                                print("produto nao encontrado")
                            elif produto != []:
                                produto_escolha = produto[escolha - 1]
                                nome = produto_escolha[0]
                                estoque = produto_escolha[2]
                                preco = produto_escolha[1]

                                if quantidade <= estoque:

                                    estoque -= quantidade

                                    produto_escolha[2] -= quantidade

                                    valor_total = preco * quantidade
                                    valor_desc = valor_total * desconto
                                    valor_final = valor_total - valor_desc

                                    if dinheiro >= valor_final:

                                        dinheiro -= valor_final

                                        print(f"Sua compra foi realizada com sucesso! Valor final: R$ {valor_final}")

                                        print(f"Produto adquirido: {produto_escolha[0]} | Quantidade: {quantidade}")

                                        print(f"Saldo atual da conta: R$ {dinheiro}")

                                        fretes = [89.90, 19.99, 0]

                                        print("Escolha a opção de entrega desejada:")
                                        print("1 - Fast: entrega em até 8 dias | frete: R$ 89,90")
                                        print("2 - Medium: entrega em até 16 dias | frete: R$ 19,99")
                                        print("3 - Slow: entrega em até 30 dias | frete grátis")

                                        while True:

                                            transporte = int(input("Escolha sua transportadora: "))

                                            if transporte == 1 and dinheiro >= 89.90:

                                                dinheiro -= fretes[0]

                                                print("Entrega Fast selecionada. Obrigado pela preferência!")
                                                break

                                            elif transporte == 2 and dinheiro >= 19.99:

                                                dinheiro -= fretes[1]

                                                print("Entrega Medium selecionada. Obrigado pela preferência!")
                                                break

                                            elif transporte == 3:

                                                dinheiro -= fretes[2]

                                                print("Entrega Slow selecionada. Obrigado pela preferência!")
                                                break

                                            else:

                                                print("Transportadora indisponível ou saldo insuficiente.")
                                                continue

                                    elif dinheiro < valor_final:

                                        p[2] += quantidade

                                        print("Saldo insuficiente.")
                            
                                
                                else:

                                    print("Estoque insuficiente.")
                           
                        else:
                            print("Forma de pagamento inválida.")
                    elif animalOUproduto == "animal":
                        achou=False
                        for a in animal:
                            print(f"Nome: {a[0]}")
                            print(f"Tipo: {a[1]}")
                            print(f"Identificação: {a[2]}")
                            print(f"Peso: {a[3]}")
                            print(f"Valor: {a[4]}")
                            print("-"*50)
                        pesquisa = input("Qual animal você quer comprar (Digite a identificação)? ")
                        for i in range(len(animal)):
                            if animal[i][2]==pesquisa:
                                achou=True
                                break
                        if achou:
                            print(f"Nome: {animal[i][0]}")
                            print(f"Tipo: {animal[i][1]}")
                            print(f"Identificação: {animal[i][2]}")
                            print(f"Peso: {animal[i][3]}")
                            print(f"Valor: {animal[i][4]}")
                            print("-"*50)
                            pesquisa = input("Deseja compra esse animal? ").lower()
                            if pesquisa == "sim":
                                print("Antes de efetuar o pagamento, confira as formas de pagamento:")
                                print("1 - Pix: desconto de 5%")
                                print("2 - Cartão: desconto de 10%")

                                desconto = 0

                                tipo_de_pagamento = input("Escolha uma opção de pagamento: ")
                                if tipo_de_pagamento == "1":

                                    desconto = 0.05

                                    nome = animal[i][0]
                                    preco = animal[i][4]

                                    valor_total = preco 
                                    valor_desc = valor_total * desconto
                                    valor_final = valor_total - valor_desc

                                    if dinheiro >= valor_final:

                                        dinheiro -= valor_final

                                        print(f"Sua compra foi realizada com sucesso! Valor final: R$ {valor_final}")

                                        print(f"Produto adquirido:")
                                        print(f"Nome: {animal[i][0]}")
                                        print(f"Tipo: {animal[i][1]}")
                                        print(f"Identificação: {animal[i][2]}")
                                        print(f"Peso: {animal[i][3]}")
                                        print(f"Valor: {valor_final}")
                                        print("-"*50)

                                        fretes = [89.90, 19.99, 0]

                                        print("Escolha a opção de entrega desejada:")
                                        print("1 - Fast: entrega em até 8 dias | frete: R$ 89,90")
                                        print("2 - Medium: entrega em até 16 dias | frete: R$ 19,99")
                                        print("3 - Slow: entrega em até 30 dias | frete grátis")

                                        while True:

                                            transporte = int(input("Escolha sua transportadora: "))

                                            if transporte == 1 and dinheiro >= 89.90:

                                                dinheiro -= fretes[0]

                                                print("Entrega Fast selecionada. Obrigado pela preferência!")
                                                animal.remove(animal[i])
                                                break

                                            elif transporte == 2 and dinheiro >= 19.99:

                                                dinheiro -= fretes[1]

                                                print("Entrega Medium selecionada. Obrigado pela preferência!")
                                                animal.remove(animal[i])
                                                break

                                            elif transporte == 3:

                                                dinheiro -= fretes[2]

                                                print("Entrega Slow selecionada. Obrigado pela preferência!")
                                                animal.remove(animal[i])
                                                break

                                            else:

                                                print("Transportadora indisponível ou saldo insuficiente.")
                                                continue

                                    elif dinheiro < valor_final:

                                    

                                        print("Saldo insuficiente.")
                                        continue

                                

                                elif tipo_de_pagamento == "2":

                                    while True:

                                        valido = True

                                        cartao = input("Adicione os dados do cartão: ")

                                        cartao_sem_espaco = cartao.replace(" ", "")

                                        for numero in cartao_sem_espaco:

                                            if numero not in "0123456789":
                                                valido = False

                                        if len(cartao_sem_espaco) == 16 and valido == True:

                                            desconto = 0.1

                                            print("Cartão adicionado com sucesso!")
                                            break

                                        else:
                                            print("Cartão inválido.")
                                            continue

                                

                                    nome = animal[i][0]
                                    preco = animal[i][4]

                                    valor_total = preco 
                                    valor_desc = valor_total * desconto
                                    valor_final = valor_total - valor_desc

                                    if dinheiro >= valor_final:

                                        dinheiro -= valor_final

                                        print(f"Sua compra foi realizada com sucesso! Valor final: R$ {valor_final}")

                                        print(f"Produto adquirido:")
                                        print(f"Nome: {animal[i][0]}")
                                        print(f"Tipo: {animal[i][1]}")
                                        print(f"Identificação: {animal[i][2]}")
                                        print(f"Peso: {animal[i][3]}")
                                        print(f"Valor: {valor_final}")
                                        print("-"*50)

                                        print(f"Saldo atual da conta: R$ {dinheiro}")

                                        fretes = [89.90, 19.99, 0]

                                        print("Escolha a opção de entrega desejada:")
                                        print("1 - Fast: entrega em até 8 dias | frete: R$ 89,90")
                                        print("2 - Medium: entrega em até 16 dias | frete: R$ 19,99")
                                        print("3 - Slow: entrega em até 30 dias | frete grátis")

                                        while True:

                                            transporte = int(input("Escolha sua transportadora: "))

                                            if transporte == 1 and dinheiro >= 89.90:

                                                dinheiro -= fretes[0]

                                                print("Entrega Fast selecionada. Obrigado pela preferência!")
                                                animal.remove(animal[i])
                                                break

                                            elif transporte == 2 and dinheiro >= 19.99:

                                                dinheiro -= fretes[1]

                                                print("Entrega Medium selecionada. Obrigado pela preferência!")
                                                animal.remove(animal[i])
                                                break

                                            elif transporte == 3:

                                                dinheiro -= fretes[2]

                                                print("Entrega Slow selecionada. Obrigado pela preferência!")
                                                animal.remove(animal[i])
                                                break

                                            else:

                                                print("Transportadora indisponível ou saldo insuficiente.")
                                                continue
                                            

                                    elif dinheiro < valor_final:

                                        

                                        print("Saldo insuficiente.")

                                
                                else:
                                    print("Forma de pagamento inválida.")
                        else:
                            print("Animal não encontrado!")
                        




                else:
                    break

            print(f"Saldo da conta: R$ {dinheiro}")

            while True:

                voltar_inicio = input("""
            Deseja sair ou voltar para a aba de login?
            1 - Sair
            2 - Voltar para a aba de login
            """)

                if voltar_inicio == "1":
                    print("Obrigado por acessar nosso site!")
                    quit()
                    break
                    

                elif voltar_inicio == "2":   
                    while True:
                        print("Olá, cliente! Bem-vindo ao site + Pecoaria.")
                        print("-" * 50)
                        print("--- ABA DE LOGIN ---")
                        print("1 - Cadastrar")
                        print("2 - Login")
                        print("0 - Sair")
                        print("-" * 50)

                        aba = input("Escolha uma opção para prosseguir: ")

                        if aba == "1":

                            while True:

                                nome = input("Digite um nome de usuário válido: ")
                                nome_existe=False
                                for r in range(len(cliente)):
                                    if cliente[r][0] == nome: 
                                    
                                        nome_existe = True
                                        break
                                if nome_existe:
                                    print('Esse nome ja pertence a outro usuário!')

                                else:
                                    senha = input("Digite sua senha: ")
                                    confirm_senha = input("Confirme sua senha: ")
                                

                                    if senha != confirm_senha:
                                        print("Senha inválida.")

                                    else:
                                        cliente.append([nome, senha])
                                        print("Cadastro concluído com sucesso!")
                                        acesso = True
                                        break

                        elif aba == "2":

                            if cliente == []:
                                print("Nenhum usuário encontrado.")
                                encontrado = False
                                continue
                            else:
                                while True:

                                    print("Bem-vindo de volta!")

                                    nome = input("Digite seu nome: ")
                                    senha = input("Digite sua senha: ")

                                    encontrado = False

                                    for usuario in cliente:

                                        if usuario[0] == nome and usuario[1] == senha:

                                            print("Olá,", nome, "! Bem-vindo de volta.")
                                            acesso = True
                                            encontrado = True
                                            break

                                    if encontrado == True:
                                        break

                                    else:
                                        print("Usuário não encontrado.")

                        elif aba == "0":
                            print("Até mais!")
                            quit()

                        else:
                            print("Digite uma das opções acima.")
                            continue
                        dinheiro = 0

                        while True:

                            voltar_comprar = input("Deseja ir para a aba de compras? ")

                            if voltar_comprar == "sim":

                                print(f"Saldo da conta: R$ {dinheiro}")

                              
                                while True:
                                    numeros = "1234567890"
                                    dinheiro_valido = True
                                    dinheiro1 = input("Quanto de saldo deseja por na sua conta? ")
                                    for d in dinheiro1:
                                        if d not in numeros:
                                            dinheiro_valido = False
                                    if dinheiro_valido and dinheiro1 != "":
                                        dinheiro1 = int(dinheiro1)
                                        if dinheiro1 >=0:
                                            dinheiro+= dinheiro1
                                            print(f"Saldo atualizado com sucesso! Saldo atual: R$ {dinheiro}")
                                            break
                                    else:
                                        print("Saldo não possivel de adicionar.Tente novamente")
                                animalOUproduto= input("Deseja comprar produto ou animal: ")

                                if animalOUproduto == "produto":
                                    print("Itens disponíveis:")

                                    for i, p in enumerate(produto, start=1):

                                        print(f"{i} - {p[0]} | preço: R$ {p[1]}| estoque: {p[2]} ")

                                    escolha = int(input("Qual produto deseja comprar? (1 ou 2): "))

                                    quantidade = int(input("Quantidade da compra: "))

                                    print("Antes de efetuar o pagamento, confira as formas de pagamento:")
                                    print("1 - Pix: desconto de 5%")
                                    print("2 - Cartão: desconto de 10%")

                                    desconto = 0

                                    tipo_de_pagamento = input("Escolha uma opção de pagamento: ")

                                    if tipo_de_pagamento == "1":
                                    
                                            desconto = 0.05
                                            if escolha < 1 or escolha > len(produto):
                                                print("produto nao encontrado")
                                            elif produto != []:
                                                produto_escolha = produto[escolha - 1]
                                                nome = produto_escolha[0]
                                                estoque = produto_escolha[2]
                                                preco = produto_escolha[1]

                                                if quantidade <= estoque:

                                                    estoque -= quantidade
                                                    produto_escolha[2] -= quantidade

                                                    valor_total = preco * quantidade
                                                    valor_desc = valor_total * desconto
                                                    valor_final = valor_total - valor_desc

                                                    if dinheiro >= valor_final:

                                                        dinheiro -= valor_final

                                                        print(f"Sua compra foi realizada com sucesso! Valor final: R$ {valor_final}")

                                                        print(f"Produto adquirido: {produto_escolha[0]} | Quantidade: {quantidade}")

                                                        fretes = [89.90, 19.99, 0]

                                                        print("Escolha a opção de entrega desejada:")
                                                        print("1 - Fast: entrega em até 8 dias | frete: R$ 89,90")
                                                        print("2 - Medium: entrega em até 16 dias | frete: R$ 19,99")
                                                        print("3 - Slow: entrega em até 30 dias | frete grátis")

                                                        while True:

                                                            transporte = int(input("Escolha sua transportadora: "))

                                                            if transporte == 1 and dinheiro >= 89.90:

                                                                dinheiro -= fretes[0]

                                                                print("Entrega Fast selecionada. Obrigado pela preferência!")
                                                                break

                                                            elif transporte == 2 and dinheiro >= 19.99:

                                                                dinheiro -= fretes[1]

                                                                print("Entrega Medium selecionada. Obrigado pela preferência!")
                                                                break

                                                            elif transporte == 3:

                                                                dinheiro -= fretes[2]

                                                                print("Entrega Slow selecionada. Obrigado pela preferência!")
                                                                break

                                                            else:

                                                                print("Transportadora indisponível ou saldo insuficiente.")
                                                                continue

                                                    elif dinheiro < valor_final:

                                                        p[2] += quantidade

                                                        print("Saldo insuficiente.")
                                                        continue
                                            
                                                else:

                                                    print("Estoque insuficiente.")
                                                    continue
                                           
                                    elif tipo_de_pagamento == "2":

                                        while True:

                                            valido = True

                                            cartao = input("Adicione os dados do cartão: ")

                                            cartao_sem_espaco = cartao.replace(" ", "")

                                            for i in cartao_sem_espaco:

                                                if i not in "0123456789":
                                                    valido = False

                                            if len(cartao_sem_espaco) == 16 and valido == True:

                                                desconto = 0.1

                                                print("Cartão adicionado com sucesso!")
                                                break

                                            else:
                                                print("Cartão inválido.")
                                                continue
                                        if escolha < 1 or escolha > len(produto):
                                            print("produto nao encontrado")
                                        elif produto != []:
                                            produto_escolha = produto[escolha - 1]
                                            nome = produto_escolha[0]
                                            estoque = produto_escolha[2]
                                            preco = produto_escolha[1]

                                            if quantidade <= estoque:

                                                estoque -= quantidade

                                                produto_escolha[2] -= quantidade

                                                valor_total = preco * quantidade
                                                valor_desc = valor_total * desconto
                                                valor_final = valor_total - valor_desc

                                                if dinheiro >= valor_final:

                                                    dinheiro -= valor_final

                                                    print(f"Sua compra foi realizada com sucesso! Valor final: R$ {valor_final}")

                                                    print(f"Produto adquirido: {produto_escolha[0]} | Quantidade: {quantidade}")

                                                    print(f"Saldo atual da conta: R$ {dinheiro}")

                                                    fretes = [89.90, 19.99, 0]

                                                    print("Escolha a opção de entrega desejada:")
                                                    print("1 - Fast: entrega em até 8 dias | frete: R$ 89,90")
                                                    print("2 - Medium: entrega em até 16 dias | frete: R$ 19,99")
                                                    print("3 - Slow: entrega em até 30 dias | frete grátis")

                                                    while True:

                                                        transporte = int(input("Escolha sua transportadora: "))

                                                        if transporte == 1 and dinheiro >= 89.90:

                                                            dinheiro -= fretes[0]

                                                            print("Entrega Fast selecionada. Obrigado pela preferência!")
                                                            break

                                                        elif transporte == 2 and dinheiro >= 19.99:

                                                            dinheiro -= fretes[1]

                                                            print("Entrega Medium selecionada. Obrigado pela preferência!")
                                                            break

                                                        elif transporte == 3:

                                                            dinheiro -= fretes[2]

                                                            print("Entrega Slow selecionada. Obrigado pela preferência!")
                                                            break

                                                        else:

                                                            print("Transportadora indisponível ou saldo insuficiente.")
                                                            continue

                                                elif dinheiro < valor_final:

                                                    p[2] += quantidade

                                                    print("Saldo insuficiente.")
                                        
                                            
                                            else:

                                                print("Estoque insuficiente.")
                                       
                                    else:
                                        print("Forma de pagamento inválida.")
                                elif animalOUproduto == "animal":
                                    achou=False
                                    for a in animal:
                                        print(f"Nome: {a[0]}")
                                        print(f"Tipo: {a[1]}")
                                        print(f"Identificação: {a[2]}")
                                        print(f"Peso: {a[3]}")
                                        print(f"Valor: {a[4]}")
                                        print("-"*50)
                                    pesquisa = input("Qual animal você quer comprar (Digite a identificação)? ")
                                    for i in range(len(animal)):
                                        if animal[i][2]==pesquisa:
                                            achou=True
                                            break
                                    if achou:
                                        print(f"Nome: {animal[i][0]}")
                                        print(f"Tipo: {animal[i][1]}")
                                        print(f"Identificação: {animal[i][2]}")
                                        print(f"Peso: {animal[i][3]}")
                                        print(f"Valor: {animal[i][4]}")
                                        print("-"*50)
                                        pesquisa = input("Deseja compra esse animal? ").lower()
                                        if pesquisa == "sim":
                                            print("Antes de efetuar o pagamento, confira as formas de pagamento:")
                                            print("1 - Pix: desconto de 5%")
                                            print("2 - Cartão: desconto de 10%")

                                            desconto = 0

                                            tipo_de_pagamento = input("Escolha uma opção de pagamento: ")
                                            if tipo_de_pagamento == "1":

                                                desconto = 0.05

                                                nome = animal[i][0]
                                                preco = animal[i][4]

                                                valor_total = preco 
                                                valor_desc = valor_total * desconto
                                                valor_final = valor_total - valor_desc

                                                if dinheiro >= valor_final:

                                                    dinheiro -= valor_final

                                                    print(f"Sua compra foi realizada com sucesso! Valor final: R$ {valor_final}")

                                                    print(f"Produto adquirido:")
                                                    print(f"Nome: {animal[i][0]}")
                                                    print(f"Tipo: {animal[i][1]}")
                                                    print(f"Identificação: {animal[i][2]}")
                                                    print(f"Peso: {animal[i][3]}")
                                                    print(f"Valor: {valor_final}")
                                                    print("-"*50)

                                                    fretes = [89.90, 19.99, 0]

                                                    print("Escolha a opção de entrega desejada:")
                                                    print("1 - Fast: entrega em até 8 dias | frete: R$ 89,90")
                                                    print("2 - Medium: entrega em até 16 dias | frete: R$ 19,99")
                                                    print("3 - Slow: entrega em até 30 dias | frete grátis")

                                                    while True:

                                                        transporte = int(input("Escolha sua transportadora: "))

                                                        if transporte == 1 and dinheiro >= 89.90:

                                                            dinheiro -= fretes[0]

                                                            print("Entrega Fast selecionada. Obrigado pela preferência!")
                                                            animal.remove(animal[i])
                                                            break

                                                        elif transporte == 2 and dinheiro >= 19.99:

                                                            dinheiro -= fretes[1]

                                                            print("Entrega Medium selecionada. Obrigado pela preferência!")
                                                            animal.remove(animal[i])
                                                            break

                                                        elif transporte == 3:

                                                            dinheiro -= fretes[2]

                                                            print("Entrega Slow selecionada. Obrigado pela preferência!")
                                                            animal.remove(animal[i])
                                                            break

                                                        else:

                                                            print("Transportadora indisponível ou saldo insuficiente.")
                                                            continue

                                                elif dinheiro < valor_final:

                                                

                                                    print("Saldo insuficiente.")
                                                    continue

                                            

                                            elif tipo_de_pagamento == "2":

                                                while True:

                                                    valido = True

                                                    cartao = input("Adicione os dados do cartão: ")

                                                    cartao_sem_espaco = cartao.replace(" ", "")

                                                    for numero in cartao_sem_espaco:

                                                        if numero not in "0123456789":
                                                            valido = False

                                                    if len(cartao_sem_espaco) == 16 and valido == True:

                                                        desconto = 0.1

                                                        print("Cartão adicionado com sucesso!")
                                                        break

                                                    else:
                                                        print("Cartão inválido.")
                                                        continue

                                            

                                                nome = animal[i][0]
                                                preco = animal[i][4]

                                                valor_total = preco 
                                                valor_desc = valor_total * desconto
                                                valor_final = valor_total - valor_desc

                                                if dinheiro >= valor_final:

                                                    dinheiro -= valor_final

                                                    print(f"Sua compra foi realizada com sucesso! Valor final: R$ {valor_final}")

                                                    print(f"Produto adquirido:")
                                                    print(f"Nome: {animal[i][0]}")
                                                    print(f"Tipo: {animal[i][1]}")
                                                    print(f"Identificação: {animal[i][2]}")
                                                    print(f"Peso: {animal[i][3]}")
                                                    print(f"Valor: {valor_final}")
                                                    print("-"*50)

                                                    print(f"Saldo atual da conta: R$ {dinheiro}")

                                                    fretes = [89.90, 19.99, 0]

                                                    print("Escolha a opção de entrega desejada:")
                                                    print("1 - Fast: entrega em até 8 dias | frete: R$ 89,90")
                                                    print("2 - Medium: entrega em até 16 dias | frete: R$ 19,99")
                                                    print("3 - Slow: entrega em até 30 dias | frete grátis")

                                                    while True:

                                                        transporte = int(input("Escolha sua transportadora: "))

                                                        if transporte == 1 and dinheiro >= 89.90:

                                                            dinheiro -= fretes[0]

                                                            print("Entrega Fast selecionada. Obrigado pela preferência!")
                                                            animal.remove(animal[i])
                                                            break

                                                        elif transporte == 2 and dinheiro >= 19.99:

                                                            dinheiro -= fretes[1]

                                                            print("Entrega Medium selecionada. Obrigado pela preferência!")
                                                            animal.remove(animal[i])
                                                            break

                                                        elif transporte == 3:

                                                            dinheiro -= fretes[2]

                                                            print("Entrega Slow selecionada. Obrigado pela preferência!")
                                                            animal.remove(animal[i])
                                                            break

                                                        else:

                                                            print("Transportadora indisponível ou saldo insuficiente.")
                                                            continue
                                                        

                                                elif dinheiro < valor_final:

                                                    

                                                    print("Saldo insuficiente.")

                                            
                                            else:
                                                print("Forma de pagamento inválida.")
                                    else:
                                        print("Animal não encontrado!")
                            else:
                                break             
                                


                                            
                
                else:

                    print("Escolha uma das opções acima.")
                    continue 












    elif opcao == 2:
        while True:
            produtoADM.interfaceADMinicio()
            opcao = int(input("Qual opção você quer? "))

            if opcao == 1:
               acessoUsuario(administrador,acesso)
            elif opcao == 2:
                
                    # acesso = True
                if entrar(administrador,acesso):
                    acesso = False
                    print ( '-'*50)
                    print ( 'Olá administrador!')
                    print ( '-'*50)
                    while True:
                            
                            print ( 'Essas são as opções:')
                            print ( '-'*50)
                            print ( '1 Produtos')
                            print ( '2 Produções')
                            print ( '3 Estoque')
                            print ( '0 Sair')
                            print ( '-'*50)
                            opcao = int ( input ( 'Qual opção você quer? ' ) )
                            
                            
                            if opcao == 0:
                                print ( 'Ok!')
                                break
                            elif opcao == 1:
                                while True:
                                    print ( '-'*50)
                                    print ( 'Essas são as opções de produto:')
                                    print ( '-'*50)
                                    print ( '1 Cadastrar produto')
                                    print ( '2 Ver produtos')
                                    print ( '3 Editar produto')
                                    print ( '4 Remover produto')
                                    print ( '0 Sair')
                                    print ( '-'*50)
                                    opcao = int ( input ( 'Qual opção você quer? ' ) )
                                    if opcao == 1:
                                        cadastrarProduto()
                                    
                                    elif opcao == 2:
                                        produtoADM.opcao2(produto,animal)
                                    
                                    elif opcao == 3:
                                        produtoADM.opcao3(produto,animal)
                                        if achou:
                                            cadastrarProduto()
                                            

                                    elif opcao == 4:
                                        produtoADM.opcao4(produto,animal)
                                    elif opcao == 0:
                                        print('Ok!')
                                        break
                                    else:
                                        print("Opção inválida!")
                                        
                            elif opcao == 2:
                                while True:
                                    print ( '-'*50)
                                    print ( 'Essas são as opções de produção:')
                                    print ( '-'*50)
                                    print ( '1 Cadastrar produção')
                                    print ( '2 Ver produções')
                                    print ( '3 Editar produção')
                                    print ( '4 Remover produção')
                                    print ( '5 Produzir')
                                    print ( '0 Sair')
                                    print ( '-'*50)
                                    opcao = int ( input ( 'Qual opção você quer? ' ) )
                                    if opcao == 1:
                                        producaoADM.opcao1Producao(p_producao,m_primas,ver_p)
                                    elif opcao == 2:
                                        producaoADM.opcao2Verproducao(p_producao)
                                    elif opcao == 3:
                                        producaoADM.opcao3Editarproduca(p_producao)  
                                    elif opcao == 4:
                                       producaoADM.opcao4Removerproducao(p_producao)         
                                    elif opcao == 5:
                                        producaoADM.opcao5Produzir(p_producao,m_primas)
    
                                    elif opcao == 0:
                                        print('Ok!')
                                        break

                                    else:
                                        print("Opção inválida!")

                            elif opcao == 3:
                                while True:
                                    print ( '-'*50)
                                    print ( 'Essas são as opções de estoque:')
                                    print ( '-'*50)
                                    print ( '1 Ver estoque')
                                    print ( '2 Adicionar mais estoque')
                                    print ( '3 Remover do estoque')
                                    print ( '0 Sair')
                                    print ( '-'*50)
                                    opcao = int ( input ( 'Qual opção você quer? ' ) )
                                    if opcao == 1:
                                        estoqueADM.opcao1Verestoque(m_primas)
                                    elif opcao == 2:
                                        estoqueADM.opcao2Adicionarestoque(m_primas)
                                    elif opcao == 3:
                                        estoqueADM.opcao3Removerestoque(m_primas)
                                    elif opcao == 0:
                                        print('Ok!')
                                        break
                                    else:
                                        print("Opção inválida!")
                            else:
                                print("Opção inválida!")

                else:
                    print('Usuário ou senha incorretos!')

            elif opcao == 0:
                print('Ok!')
                break               
                    

            else:
                print('-'*50)
                print('Opção inválida!')
                print('-'*50)