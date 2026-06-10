import administrador.producaoADM as producaoADM
import administrador.produtoADM as produtoADM
import administrador.estoqueADM as estoqueADM
import cliente.compraC as clienteC
import cliente.loginC as loginCLIENTE
import truques.input as inputt
import requests
import truques.transport_clima as clima
administrador = [['henrique','henrique114'],['pedro','pedro2245']]
material = {}
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

def acessoUsuario(escolhaADMouC):
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
                    usuario_logado = nome
                    return usuario_logado


        


while True:
    print('Bem vindo ao sistema Mais Pecuárea!')
    print('-'*50)
    print('Essas são as opções:')
    print('1 Cliente')
    print('2 Administrador')
    print('-'*50)
    opcao = inputt.inputNumeroInt("Qual opção você quer? ")
    if opcao == 1:
        usuario_logado = ''
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

               usuario_logado= acessoUsuario(cliente)
               
            elif aba == "2":
                usuario_logado=loginCLIENTE.loginUSUARIO()

            elif aba == "0":
                print("Até mais!")
                quit()

            else:
                print("Digite uma das opções acima.")
                continue
            saldo = 0
            if usuario_logado or aba == "1":
                
                while True:
                        voltar_comprar = input("Deseja ir para a aba de compras? ").lower()   
                        if voltar_comprar == "sim":
                            saldo = clienteC.inserirSaldo(usuario_logado,saldo)               
                            animalOUproduto= input("Deseja comprar produto ou animal: ")
                            
                            if animalOUproduto == "produto":
                               saldo=clienteC.produtoC(produto,usuario_logado,saldo)
                               break
                            elif animalOUproduto == "animal":
                                clienteC.animalC(animal,usuario_logado)
                                break
                            else:
                                print('Opção inválida!')
                                break
                        
                            print(f"Saldo da conta: R$ {saldo}")
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
                                    saldo = 0
                                    while True:
                                            
                                            saldo = clienteC.inserirSaldo(usuario_logado,saldo)               
                                            animalOUproduto= input("Deseja comprar produto ou animal: ")

                                            if animalOUproduto == "produto":
                                                clienteC.produtoC(produto)
                                            elif animalOUproduto == "animal":
                                                clienteC.animalC(animal)
                                            else:
                                                break
                                    print(f"Saldo da conta: R$ {saldo}")                                              
                                else:
                                    print("Escolha uma das opções acima.")
                                    continue 

    elif opcao == 2:
        while True:
            produtoADM.interfaceADMinicio()
            opcao = inputt.inputNumeroInt("Qual opção você quer? ")

            if opcao == 1:
               acessoUsuario(administrador)
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
                            opcao = inputt.inputNumeroInt( 'Qual opção você quer? ' )
                            
                            
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
                                    opcao = inputt.inputNumeroInt( 'Qual opção você quer? ' )
                                    if opcao == 1:
                                        produtoADM.cadastrarProduto(animal,produto)
                                    
                                    elif opcao == 2:
                                        produtoADM.opcao2(produto,animal)
                                    
                                    elif opcao == 3:
                                        produtoADM.opcao3(produto,animal,achou)
                                        if achou:
                                            produtoADM.cadastrarProduto(animal,produto)
                                            

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
                                    opcao = inputt.inputNumeroInt( 'Qual opção você quer? ' ) 
                                    if opcao == 1:
                                        producaoADM.opcao1Producao(p_producao,m_primas,ver_p,material)
                                    elif opcao == 2:
                                        producaoADM.opcao2Verproducao(p_producao)
                                    elif opcao == 3:
                                        producaoADM.opcao3Editarproducao(p_producao,material)  
                                    elif opcao == 4:
                                       producaoADM.opcao4Removerproducao(p_producao,material)         
                                    elif opcao == 5:
                                        producaoADM.opcao5Produzir(p_producao,material)
    
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
                                    opcao = inputt.inputNumeroInt( 'Qual opção você quer? ' )
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