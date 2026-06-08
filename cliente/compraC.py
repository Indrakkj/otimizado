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


def inserirSaldo(usuario_logado):
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
        numeros = "1234567890"
        dinheiro_valido = True
        dinheiro1 = input("Quanto de saldo deseja por na sua conta? ")
        
        for d in dinheiro1:
            if d not in numeros:
                dinheiro_valido = False
        if dinheiro_valido and dinheiro1 != "":
            dinheiro1 = int(dinheiro1)
            if dinheiro1 >= 0:

                novas_linhas = []
    
                for linha in linhas:
                    if linha.strip() == '':
                        continue
                    nome,senha,saldo = linha.strip().split(",")
                    
                    if nome == usuario_logado:
                        saldo = int(saldo) + int(dinheiro1)
                    novas_linhas.append(f'{nome},{senha},{saldo}\n')
                with open ('logins.txt' ,'w')as arquivos:
    
                    arquivos.writelines(novas_linhas)

                print(f"Saldo atualizado com sucesso! Saldo atual: R$ {saldo}")
            break
        else:
            print("Saldo nao possivel de adicionar.Tente novamente")
    return saldo
def produtoC(produto,usuario_logado):
    
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

                        if dinheiro >= valor_final:
                        

                            dinheiro -= valor_final
                            with open ('logins.txt', 'r', encoding= 'utf -8')as arquivos:
                                linhas = arquivos.readlines()
                            with open ('logins.txt','w' , encoding= 'utf-8')as arquivos:
                                for linha in linhas:
                                    if linha.strip() == '':
                                        continue
                                    nome,senha,saldo = linha.strip().split(',')
                                    if nome == usuario_logado:
                                        saldo=dinheiro
                                    arquivos.write(f"{nome},{senha},{saldo}\n")
                                    return dinheiro
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
                                    break

                        elif dinheiro < valor_final:

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

                    if dinheiro >= valor_final:

                        dinheiro -= valor_final
                        with open ('logins.txt', 'r', encoding= 'utf -8')as arquivos:
                            linhas = arquivos.readlines()
                        with open ('logins.txt','w' , encoding= 'utf-8')as arquivos:
                            for linha in linhas:
                                if linha.strip() == '':
                                    continue
                                nome,senha,saldo = linha.strip().split(',')
                                if nome == usuario_logado:
                                    saldo=dinheiro
                                arquivos.write(f"{nome},{senha},{saldo}\n")
                                return dinheiro
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

                    if dinheiro >= valor_final:

                        dinheiro -= valor_final
                        with open ('logins.txt', 'r', encoding= 'utf -8')as arquivos:
                            linhas = arquivos.readlines()
                        with open ('logins.txt','w' , encoding= 'utf-8')as arquivos:
                            for linha in linhas:
                                if linha.strip() == '':
                                    continue
                                nome,senha,saldo = linha.strip().split(',')
                                if nome == usuario_logado:
                                    saldo=dinheiro
                                arquivos.write(f"{nome},{senha},{saldo}\n")
                                return dinheiro
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
                                break

                    elif dinheiro < valor_final:

                    

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

                    if dinheiro >= valor_final:

                        dinheiro -= valor_final
                        with open ('logins.txt', 'r', encoding= 'utf -8')as arquivos:
                            linhas = arquivos.readlines()
                        with open ('logins.txt','w' , encoding= 'utf-8')as arquivos:
                            for linha in linhas:
                                if linha.strip() == '':
                                    continue
                                nome,senha,saldo = linha.strip().split(',')
                                if nome == usuario_logado:
                                    saldo=dinheiro
                                arquivos.write(f"{nome},{senha},{saldo}\n")
                                return dinheiro
                        

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
                                break
                            

                    elif dinheiro < valor_final:

                        

                        print("Saldo insuficiente.")
                        break

                
                else:
                    print("Forma de pagamento inválida.")
                    break
        else:
            print("Animal não encontrado!")
            break