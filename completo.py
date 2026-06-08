import administrador.producaoADM as producaoADM
import administrador.produtoADM as produtoADM
import administrador.estoqueADM as estoqueADM
import cliente.compraC as clienteC
import cliente.loginC as loginCLIENTE
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
                saldo = 0
                with open ('logins.txt' , 'a' , encoding= 'utf-8') as escolhaADMouC:
                    escolhaADMouC.write(f'{nome},{senha},{saldo}\n')
                    print("Cadastro concluído com sucesso!")
                    escolhaADMouC.close
                    acesso = True
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
        usuario_logado = None
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
                usuario_logado=loginCLIENTE.loginUSUARIO()

            elif aba == "0":
                print("Até mais!")
                quit()

            else:
                print("Digite uma das opções acima.")
                continue
            dinheiro = 0
            if usuario_logado or aba == "1":
                
                while True:
                        voltar_comprar = input("Deseja ir para a aba de compras? ").lower()   
                        if voltar_comprar == "sim":
                            dinheiro = clienteC.inserirSaldo(usuario_logado)               
                            animalOUproduto= input("Deseja comprar produto ou animal: ")

                            if animalOUproduto == "produto":
                                clienteC.produtoC(produto,usuario_logado)
                            elif animalOUproduto == "animal":
                                clienteC.animalC(animal,usuario_logado)
                                
                            else:
                                print('Opção inválida!')
                                break
                        
                            print(f"Saldo da conta: R$ {dinheiro}")
                        else:
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
                                        loginCLIENTE.loginUSUARIO()
                                    

                                    elif aba == "0":
                                        print("Até mais!")
                                        quit()

                                    else:
                                        print("Digite uma das opções acima.")
                                        continue
                                    dinheiro = 0
                                    while True:
                                            
                                            dinheiro = clienteC.inserirSaldo(dinheiro)               
                                            animalOUproduto= input("Deseja comprar produto ou animal: ")

                                            if animalOUproduto == "produto":
                                                clienteC.produtoC(produto)
                                            elif animalOUproduto == "animal":
                                                clienteC.animalC(animal)
                                            else:
                                                break
                                    print(f"Saldo da conta: R$ {dinheiro}")                                              
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
                adm_logado = loginCLIENTE.loginUSUARIO()
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
                                        produtoADM.opcao3(produto,animal,achou)
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