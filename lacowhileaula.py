
""""
while em python - AULA 7
utilizado para realizar ações enquanto 
uma condição for verdadeira 

requisitos: entender condições e operadores
"""""
#while True:   #loop infinito
    #nome= input("Qual o seu nome?")
    #print(f'olá {nome}!')


#print('nao sera executada.')

#x=0
#while x <10:  #loop de 0 a 100
    #if x==3:
      #  x = x + 1
        #continue cai na condição e o numero 3 nao aparece em tela no exemplo
       # break acaba quando cai na condição

  #  print(x)
   # x = x + 1


#print('acabou')

#x=0
#while x <10:
    #y=0

    #while y < 5:
      #  print(f' ({x} , {y})')
       # y+= 1

    #x+= 1
#print('acabou!')




while True:

    print()
    num_1 = input('digite um numero ou digite sair para encerrar:')

    if num_1 == 'sair':  # tentando encerrar o laço apos digitar sair
        sair = input('deseja sair? [s]im ou [n]ão: ')
        if sair == 's':
            break

    num_2 = input('digite outro numero ou digite sair para encerrar:')
    if num_2 == 'sair':
        sair = input('deseja sair? [s]im ou [n]ão: ')
        if sair == 's':
            break

    operador = input('digite um operador ou digite sair para encerrar: ')

    if operador == 'sair':
        sair = input('deseja sair? [s]im ou [n]ão: ')
        if sair == 's':
            break

    print()
    num_1 = input('digite um numero ou digite sair para encerrar:')

    if num_1 == 'sair':  # tentando encerrar o laço apos digitar sair
        sair = input('deseja sair? [s]im ou [n]ão: ')
        if sair == 'n':
            continue

    num_2 = input('digite outro numero ou digite sair para encerrar:')
    if num_2 == 'sair':
        sair = input('deseja sair? [s]im ou [n]ão: ')
        if sair == 'n':
           continue

    operador = input('digite um operador ou digite sair para encerrar: ')

    if operador == 'sair':
        sair = input('deseja sair? [s]im ou [n]ão: ')
        if sair == 'n':
            continue

    if not num_1.isnumeric() or not num_2.isnumeric():
        print('voce precisa digitar um numero ou ')
        continue
    num_1 = int(num_1)
    num_2 = int(num_2)

    if operador=='+':
        print(num_1+num_2)
    elif operador == '-':
        print(num_1-num_2)
    elif operador == '/':
        print(num_1/num_2)
    elif operador == '*':
        print(num_1*num_2)

    else:
        print ('operador invalido')

