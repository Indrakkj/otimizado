def inputNumeroInt(mensagem):
    validador = True
    
    while validador:
        variavel = input(mensagem)
        if not variavel:
            print('Digite apenas números ou valores positívos, por favor, Professor Guilherme!')
            continue
        numero = True
        ponto = 0
        for v in variavel:
            if v == '.':
                ponto += 1
                if ponto> 1:
                    print('Número inválido!')
                    numero = False
                    break
            elif not v.isdigit():    
               print('Digite apenas números ou valores positívos, por favor, Professor Guilherme!') 
               numero = False
               break 
        if numero:
            variavel = float(variavel)
            validador = False
        else:
            print('Digite apenas números ou valores positívos, por favor, Professor Guilherme!')
        
                            
        
    return variavel
# c = inputNumeroInt('digite um n: ')
# print(c)
        