def loginUSUARIO():
    nome = input("Digite seu nome: ")
    senha = input("Digite sua senha: ")
    encontrado = False

    with open ('logins.txt' , 'r' , encoding= 'utf-8' ) as arquivos:
        for linha in arquivos:
            dados = linha.strip(). split(',')
            if len(dados) < 2:
                continue
            nome_arquivo = dados [0].strip()
            senha_arquivo = dados [1].strip()
            saldo = dados [2].strip()
            if nome_arquivo  == nome and senha_arquivo == senha:
                encontrado = True
                
                break
    if encontrado:
        print("login encontrado")
        return nome
        
    else:
        print("usuario nao encontrado")
        return False          
