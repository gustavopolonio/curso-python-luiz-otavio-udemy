# Calculadora com while

while True:
  num_1 = input('Primeiro número: ')
  num_2 = input('Segundo número: ')
  operator = input('Qual operação (+-/*)? ')

  try:
    num_1_float = float(num_1)
    num_2_float = float(num_2)

    if operator == '+':
      print(f'{num_1_float} {operator} {num_2_float} = {num_1_float + num_2_float}')
    elif operator == '-':
      print(f'{num_1_float} {operator} {num_2_float} = {num_1_float - num_2_float}')
    elif operator == '/':
      print(f'{num_1_float} {operator} {num_2_float} = {num_1_float / num_2_float}')
    elif operator == '*':
      print(f'{num_1_float} {operator} {num_2_float} = {num_1_float * num_2_float}')
    else:
      raise Exception('invalid_operator')

  except Exception as error:
    print(error.args)
    print('Erro')
    break


  sair = input('Digite S para sair da calculadora ou qualquer outra coisa para continuar: ')
  if sair.lower() == 's':
    break

print('CALCULADORA ENCERRADA!')