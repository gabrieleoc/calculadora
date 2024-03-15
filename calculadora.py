"""calculadora com while"""
while True:
    print('Bem vindo a calculadora.')
    n1 = input('Digite o primeiro número:\n')
    n2 = input('Digite o segundo número:\n')
    op = input('O que deseja fazer?\n+ - / *\n')
    
    num_validos = None
    n1_f = 0
    n2_f = 0
    try:
        n1_f = float(n1)
        n2_f = float(n2)
        num_validos = True
    except:
        num_validos = None
        
    if num_validos is None:
        print("Um ou ambos os números são inválidos.")
        continue
    
    op_permitidos = '+-/*'
    
    if op not in op_permitidos:
        print('Operador inválido.')
        continue
    
    if len(op) > 1:
        print('Digite apenas um operador.')
        continue
    
    print('Realizando sua conta. Confira o resultado abaixo.')
    if op == '+':
        print(n1_f + n2_f)
    elif op == '-':
        print(n1_f - n2_f)
    elif op == '/':
        print(n1_f / n2_f)
    elif op == '*':
        print(n1_f * n2_f)
    else:
        print('Nunca deveria chegar aqui.')
        
   
    sair = input('Quer sair? [s]im\n').lower().startswith('s')
    if sair is True:
        break