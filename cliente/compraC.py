import requests
import truques.transport_clima as clima
import truques.input as inputt
def salvarSALDO(usuario_logado):
    with open ('logins.txt', 'r', encoding= 'utf -8')as arquivos:
        linhas = arquivos.readlines()
    with open ('logins.txt','a+' , encoding= 'utf-8')as arquivos:
        for linha in linhas:
            if linha.strip() == '':
                continue
            nome,senha,saldo = linha.strip().split(",")
            if nome == usuario_logado:
                
                arquivos.write(f"{nome},{senha},{saldo}\n")
                

def inserirSaldo(usuario_logado,saldo):
    with open('logins.txt','r')as arquivos:
        linhas = arquivos.readlines()
        for linha in linhas:
            if linha.strip() == '':
                continue
            nome,senha,saldo = linha.strip().split(",")
            if nome == usuario_logado:
                print(f"Saldo da conta: R$ ({saldo})")
                break

    while True:
        
        saldo1 = inputt.inputNumeroInt("Quanto de saldo deseja por na sua conta? ")
        
       

        novas_linhas = []

        for linha in linhas:
            if linha.strip() == '':
                continue
            nome,senha,saldo = linha.strip().split(",")
                    
        if nome == usuario_logado:
            saldo = saldo1 + int(saldo)
            novas_linhas.append(f'{nome},{senha},{saldo}\n')
            with open ('logins.txt' ,'r')as arquivos:
                for linha in arquivos:
                    if linha == nome:
                        with open ('logins.txt' ,'w')as arquivos:

                            arquivos.write(novas_linhas)

            print(f"Saldo atualizado com sucesso! Saldo atual: R$ {saldo}")

        else:
            print("Saldo nao possivel de adicionar.Tente novamente")
        return saldo
def produtoC(produto,usuario_logado,saldo):
    
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
            while True:
                desconto = 0.05
                if escolha < 1 or escolha > len(produto):
                    print("Produto não encontrado!")
                    break
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
                        valor_final = int(valor_final)
                        saldo = float(saldo)
                        if saldo >= valor_final:
                        

                            saldo -= valor_final
                            with open ('logins.txt', 'r', encoding= 'utf -8')as arquivos:
                                linhas = arquivos.readlines()
                            with open ('logins.txt','w' , encoding= 'utf-8')as arquivos:
                                for linha in linhas:
                                    if linha.strip() == '':
                                        continue
                                    nome,senha,saldo = linha.strip().split(',')
                                    if nome == usuario_logado:
                                        saldo=saldo
                                    arquivos.write(f"{nome},{senha},{saldo}\n")
                                    return saldo
                            print(f"Sua compra foi realizada com sucesso! Valor final: R$ {valor_final}")

                            print(f"Produto adquirido: {produto_escolha[0]} | Quantidade: {quantidade}")

                            fretes = [89.90, 19.99, 0]
                            fast=8
                            medium=16
                            slow=30
                            print("Escolha a opção de entrega desejada:")
                            print(f"1 - Fast: entrega em até {fast} dias | frete: R$ 89,90")
                            print(f"2 - Medium: entrega em até {medium} dias | frete: R$ 19,99")
                            print(f"3 - Slow: entrega em até {slow} dias | frete grátis")
                            
                            temperatura = clima.climatizacao()
                            
                            while True:

                                transporte = inputt.inputNumeroInt("Escolha sua transportadora: ")
                                
                                if transporte == 1 and temperatura > 29:
                                    fast += 3
                                    print(f'Devido as altas temperaturas ({temperatura}C°), sua entrega chegará em {fast}dias.')
                                    break
                                elif transporte == 2 and temperatura > 29:
                                    medium += 3
                                    print(f'Devido as altas temperaturas ({temperatura}C°), sua entrega chegará em {medium}dias.')
                                    break
                                elif transporte == 3 and temperatura > 29:
                                    slow += 3
                                    print(f'Devido as altas temperaturas ({temperatura}C°), sua entrega chegará em {slow}dias.')
                                    break
                                    
                                if transporte == 1 and saldo >= 89.90:

                                    saldo -= fretes[0]

                                    print("Entrega Fast selecionada. Obrigado pela preferência!")
                                    break

                                elif transporte == 2 and saldo >= 19.99:

                                    saldo -= fretes[1]

                                    print("Entrega Medium selecionada. Obrigado pela preferência!")
                                    break

                                elif transporte == 3:

                                    saldo -= fretes[2]

                                    print("Entrega Slow selecionada. Obrigado pela preferência!")
                                    break

                                else:

                                    print("Transportadora indisponível ou saldo insuficiente.")
                                    break

                        elif saldo < valor_final:

                            p[2] += quantidade

                            print("Saldo insuficiente.")
                            break
                
                    else:

                        print("Estoque insuficiente.")
                        break
                
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

                    if saldo >= valor_final:

                        saldo -= valor_final
                        with open ('logins.txt', 'r', encoding= 'utf -8')as arquivos:
                            linhas = arquivos.readlines()
                        with open ('logins.txt','w' , encoding= 'utf-8')as arquivos:
                            for linha in linhas:
                                if linha.strip() == '':
                                    continue
                                nome,senha,saldo = linha.strip().split(',')
                                if nome == usuario_logado:
                                    saldo=saldo
                                arquivos.write(f"{nome},{senha},{saldo}\n")
                                return saldo
                        print(f"Sua compra foi realizada com sucesso! Valor final: R$ {valor_final}")

                        print(f"Produto adquirido: {produto_escolha[0]} | Quantidade: {quantidade}")

                        print(f"Saldo atual da conta: R$ {saldo}")

                       

                        fretes = [89.90, 19.99, 0]
                        fast=8
                        medium=16
                        slow=30
                        print("Escolha a opção de entrega desejada:")
                        print(f"1 - Fast: entrega em até {fast} dias | frete: R$ 89,90")
                        print(f"2 - Medium: entrega em até {medium} dias | frete: R$ 19,99")
                        print(f"3 - Slow: entrega em até {slow} dias | frete grátis")
                        
                        temperatura = clima.climatizacao()





                        while True:

                            transporte = inputt.inputNumeroInt("Escolha sua transportadora: ")

                            if transporte == 1 and temperatura > 29:
                                fast += 3
                                print(f'Devido as altas temperaturas ({temperatura}C°), sua entrega chegará em {fast}dias.')
                                break
                            elif transporte == 2 and temperatura > 29:
                                medium += 3
                                print(f'Devido as altas temperaturas ({temperatura}C°), sua entrega chegará em {medium}dias.')
                                break
                            elif transporte == 3 and temperatura > 29:
                                slow += 3
                                print(f'Devido as altas temperaturas ({temperatura}C°), sua entrega chegará em {slow}dias.')
                                break

                            else:

                                print("Transportadora indisponível ou saldo insuficiente.")
                                continue

                    elif saldo < valor_final:

                        p[2] += quantidade

                        print("Saldo insuficiente.")
            
                
                else:

                    print("Estoque insuficiente.")
            
        else:
            print("Forma de pagamento inválida.")
    
def animalC(animal,usuario_logado):
    while True:
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

                    if saldo >= valor_final:

                        saldo -= valor_final
                        with open ('logins.txt', 'r', encoding= 'utf -8')as arquivos:
                            linhas = arquivos.readlines()
                        with open ('logins.txt','w' , encoding= 'utf-8')as arquivos:
                            for linha in linhas:
                                if linha.strip() == '':
                                    continue
                                nome,senha,saldo = linha.strip().split(',')
                                if nome == usuario_logado:
                                    saldo=saldo
                                arquivos.write(f"{nome},{senha},{saldo}\n")
                                return saldo
                        print(f"Sua compra foi realizada com sucesso! Valor final: R$ {valor_final}")

                        print(f"Produto adquirido:")
                        print(f"Nome: {animal[i][0]}")
                        print(f"Tipo: {animal[i][1]}")
                        print(f"Identificação: {animal[i][2]}")
                        print(f"Peso: {animal[i][3]}")
                        print(f"Valor: {valor_final}")
                        print("-"*50)

                        
                        fast=8
                        medium=16
                        slow=30
                        print("Escolha a opção de entrega desejada:")
                        print(f"1 - Fast: entrega em até {fast} dias | frete: R$ 89,90")
                        print(f"2 - Medium: entrega em até {medium} dias | frete: R$ 19,99")
                        print(f"3 - Slow: entrega em até {slow} dias | frete grátis")
                        
                        temperatura = clima.climatizacao()

                        while True:

                            transporte = inputt.inputNumeroInt("Escolha sua transportadora: ")

                            if transporte == 1 and temperatura > 29:
                                fast += 3
                                print(f'Devido as altas temperaturas ({temperatura}C°), sua entrega chegará em {fast}dias.')
                                break
                            elif transporte == 2 and temperatura > 29:
                                medium += 3
                                print(f'Devido as altas temperaturas ({temperatura}C°), sua entrega chegará em {medium}dias.')
                                break
                            elif transporte == 3 and temperatura > 29:
                                slow += 3
                                print(f'Devido as altas temperaturas ({temperatura}C°), sua entrega chegará em {slow}dias.')
                                break

                            else:

                                print("Transportadora indisponível ou saldo insuficiente.")
                                break

                    elif saldo < valor_final:

                    

                        print("Saldo insuficiente.")
                        break

                

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
                            break

                

                    nome = animal[i][0]
                    preco = animal[i][4]

                    valor_total = preco 
                    valor_desc = valor_total * desconto
                    valor_final = valor_total - valor_desc

                    if saldo >= valor_final:

                        saldo -= valor_final
                        with open ('logins.txt', 'r', encoding= 'utf -8')as arquivos:
                            linhas = arquivos.readlines()
                        with open ('logins.txt','w' , encoding= 'utf-8')as arquivos:
                            for linha in linhas:
                                if linha.strip() == '':
                                    continue
                                nome,senha,saldo = linha.strip().split(',')
                                if nome == usuario_logado:
                                    saldo=saldo
                                arquivos.write(f"{nome},{senha},{saldo}\n")
                                return saldo
                        

                        print(f"Sua compra foi realizada com sucesso! Valor final: R$ {valor_final}")

                        print(f"Produto adquirido:")
                        print(f"Nome: {animal[i][0]}")
                        print(f"Tipo: {animal[i][1]}")
                        print(f"Identificação: {animal[i][2]}")
                        print(f"Peso: {animal[i][3]}")
                        print(f"Valor: {valor_final}")
                        print("-"*50)

                        print(f"Saldo atual da conta: R$ {saldo}")

                        
                        fast=8
                        medium=16
                        slow=30
                        print("Escolha a opção de entrega desejada:")
                        print(f"1 - Fast: entrega em até {fast} dias | frete: R$ 89,90")
                        print(f"2 - Medium: entrega em até {medium} dias | frete: R$ 19,99")
                        print(f"3 - Slow: entrega em até {slow} dias | frete grátis")
                        
                        temperatura = clima.climatizacao()

                        while True:

                            transporte = inputt.inputNumeroInt("Escolha sua transportadora: ")

                            if transporte == 1 and temperatura > 29:
                                fast += 3
                                print(f'Devido as altas temperaturas ({temperatura}C°), sua entrega chegará em {fast}dias.')
                                break
                            elif transporte == 2 and temperatura > 29:
                                medium += 3
                                print(f'Devido as altas temperaturas ({temperatura}C°), sua entrega chegará em {medium}dias.')
                                break
                            elif transporte == 3 and temperatura > 29:
                                slow += 3
                                print(f'Devido as altas temperaturas ({temperatura}C°), sua entrega chegará em {slow}dias.')
                                break


                            else:

                                print("Transportadora indisponível ou saldo insuficiente.")
                                break
                            

                    elif saldo < valor_final:

                        

                        print("Saldo insuficiente.")
                        break

                
                else:
                    print("Forma de pagamento inválida.")
                    break
        else:
            print("Animal não encontrado!")
            break