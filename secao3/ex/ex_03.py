"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
def ex1():
  number = input('Digite um número inteiro: ')

  try:
    number_int = int(number)
    if number_int % 2 == 0:
      print(f'{number} é par')
    else:
      print(f'{number} é ímpar')
  except:
    print(f'{number} não é um num inteiro')

# ex1()


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
def ex2():
  hour = input('Que horas são? (Quero saber apenas as horas inteiras!): ')

  try:
    hour_int = int(hour)
    if hour_int >= 0 and hour_int < 12:
      print('Bom dia!')
    elif hour_int >=12 and hour_int < 18:
      print('Boa tarde!')
    elif hour_int >= 18 and hour_int < 24:
      print('Boa noite!')
    else:
      raise Exception
  except:
    print('Horário inválido!')

# ex2()


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
def ex3():
  name = input('Qual é o seu primeiro nome? ')
  name_length = len(name)

  if name_length:
    if name_length <= 4:
      print('Nome curto')
    elif name_length <= 6:
      print('Nome normal')
    else:
      print('Nome grande')
  else:
    print('Digite algo!!')

ex3()