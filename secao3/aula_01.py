print('Printar na tela')

"""
  DOCSTRING
"""

# Comentário

print(12, 34)
print(12, 34, sep='-')
print(12, 34, sep='-', end=' ##\n')


# A classe type mostra o tipo que o Python inferiu ao valor
print(type('Oi'))
print(type(8.0))


# Conversão de tipo (coerção, type convertion, typecasting, coercion) => é o ato de converter um tipo em outro
# Tipos imutáveis e primitivos: str, int, float, bool
# print('1' + 1) # Erro pois o python é uma linguagem de tipagem forte (não pode concatenar tipos diferentes de dados)
print(int('1') + 1)
print(bool(0))
print(bool(''))
print(str(11.0) + 'Hi')


# PEP 8 - Guia de estilos python (https://peps.python.org/pep-0008/)

# Variáveis
# PEP8: iniciar variáveis com letra minúscula. Pode usar números e _ no nome
# O snake case é muito utilizado no python (nome_completo)


imc = ... # Ellipsis
print(imc)


# Formatação de strings (f-strings)
name = 'Gustavo'
height = 1.80
ans = f'{name} tem {height:.2f} de altura'
print(ans)


# Função input
# name = input("What's your name?")  # input sempre retorna tipo str
# print(f'Your name is {name}')
# print(f'Your name is {name=}')  # debugando variável

# n1 = int(input('Type a number: '))  # Não fazer a coerção de tipo diretamente na declaração da variável, pois se o user digitar uma str vai dar erro e quebrar o programa


#  Operações condicionais (if / elif / else)
# entrada = input('Você quer "entrar" ou "sair"? ')
entrada = 'sair'

if entrada == 'entrar':
  print('Você entrou!')
elif entrada == 'sair':
  print('Você saiu!')
else:
  print('Você é indeciso?!')


"""
  Operadores de comparação (relacionais)
  OP        Significado         Exemplo (todos são True)
  >           maior               2 > 1
  >=          maior ou igual      2 >= 2
  <           menor               1 < 1
  <=          menor ou igual      2 <= 2
  ==          igual               'a' == 'a'
  !=          diferente           'a' != 'b'
"""


"""
  Operadores lógicos
  and (e)  |  or (ou)  |  not (não)

  São valores falsy:  0  |  0.0  |  ''  |  False

  O tipo None é usado para representar um não valor
"""

# entrada = input('[E]nter [L]ogout: ')
entrada = 'E'
# password = input('Your password... ')
password = '123456'

correct_password = '123456'
expirated = False
if (entrada == 'E' or entrada == 'e') and password == correct_password and not expirated:
  print('Enter')
else:
  print('Logout')

print(bool(0))
print(bool(0.0))
print(bool(''))
print(bool(' '))
print(bool(False))