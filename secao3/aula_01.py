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


"""
  Operadores in e not in
  Strings são iteráveis no python

  0 1 2 3 4 5 6  (índices)
  G u s t á v o
  -7-6-5-4-3-2-1  (índices negativos)
"""
name = 'Gustávo'
print(name[4])
print('á' in name)
print('Gust' in name)
print(10*'-')


"""
  Interpolação básica de strings (faz a mesma coisa que as f-strings)
  s - string
  d e i - int
  f - float
  x e X - hexadecimal (ABCDEF0123456789)
"""
name = 'Gustavo'
value = 1000.988732
text = '%s, o preço é de %.2f' % (name, value)
print(text)
print('O hexadecimal de %d é: %X' % (15, 15))
# Usando f-strings
print(f'O hexadecimal de 1500 é: {1500:08x}')


"""
  Fatiamento de strings
  0123456789
  Hello world
 - (indices negativos)

  Fatiamento [i:f:p] [::]   i=início f=final p=passo
  Função len => quantidade
"""
text = 'Hello World'
print(text[2:10])
print(text[2:])
print(text[:8])
print(text[0:len(text):1])
print(text[::])


"""
  Introdução ao try/except
  try => tentar executar o código
  except => ocorreu algum erro ao tentar executar o código
"""
# number_str = input('Vou dobrar o número que você digitar: ')
number_str = 2

try:
  number_float = float(number_str)
  print(f'O dobro de {number_float} é {number_float * 2:.2f}')
except:
  print('Isso não é um número')


"""
  Variáveis constantes => defino em letra maiúscula
"""

"""
  Tipos imutáveis de dados = str, int, float, bool
"""
name = 'Gustavo'
# name[2] = 'A'  # Erro, pois str é um tipo imutável


"""
  Repteições: while
"""
aux = True
counter = 0

while aux:
  counter += 1
  # name = input('Qual o nome? ')

  if name == 'Gus':
    continue

  print(name)

  if name == 'sair' or counter == 5:
    break

print(f'Saiu do while e fez {counter} laços')

name = 'Gustavo Polonio'
i = 0
ans = ''
while i < len(name):
  # ans += '*' + name[i]
  ans += f'*{name[i]}'
  i += 1

print(ans)


"""
  Repetições: for / in
"""
text = 'Gustavo'
for letter in text:
  print(letter)


"""
  For + Range
  range => range(start, stop, step)
"""
numbers = range(10)  # start defaults to 0
numbers = range(5, 10)
numbers = range(1, 10, 2)

print(numbers)

for number in numbers:
  print(number)


"""
  Listas em Python - Equivalente a Arrays em Javascript
  Tipo list => é um tipo mutável
  Métodos úteis: append, insert, pop, del, clear, extend
"""
my_list = [10, 'Gust', True, []]
print(type(my_list))

my_list[2] = 'Polonio'  # list é mutável
print(my_list)

del my_list[2]  # Não é performático para listas grandes. Sempre tentar trabalhar com os últimos elementos de uma lista
print(my_list)

my_list.append(1200)
print(my_list)

my_list.clear()
print(my_list)

list_a = [1, 2, 3]
list_b = [4, 5, 6]
list_c = list_a + list_b
print(list_c)

list_b.extend(list_a)
print(list_b)


"""
  Cuidados com dados mutáveis
  =  => copia o valor (em tipos imutáveis)
  =  => aponta para o mesmo valor na memória (em tipos mutáveis)
"""
names_1 = ['Zé', 'Luiz']
names_2 = names_1  # names_2 e names_1 apontam para o mesmo valor em memória
names_1[1] = 'Gustavo'
print(names_2)

name1 = 'Gus'
name2 = name1  # Tipo imutável, apenas copia
name1 = 'Sasá'
print(name2)


"""
  Introdução ao desempacotamento
"""
name_1, name_2, name_3 = ['Gustavo', 'Sabrina', 'Erick']
print(name_1, name_2, name_3)

# name_1, name_2 = ['Gustavo', 'Sabrina', 'Erick']  # Erro!
# name_1, name_2, name_3 = ['Gustavo', 'Sabrina']  # Erro!

name_1, *rest = ['Gustavo', 'Sabrina', 'Erick']
print(name_1)
print(rest)


"""
  Tipo tupla - É uma lista imutável
"""
names = ('Zé', 'Luiz')  # Posso criar a tupla assim também
names = 'Zé', 'Luiz'
print(names)
print(names[1])
# names[0] = 'Gustavo'  # Erro


"""
  enumerate - enumera iteráveis (índices)
"""
names = ['Gustavo', 'Sasá', 'Alex']

# for item in enumerate(names):
#   print(item)  # Retorna uma tupla
#   index, name = item
#   print(f'{index=}, {name=}')

for index, name in enumerate(names):  # Faz a mesma coisa do for-in com enumerate acima
  print(f'{index=}, {name=}')


"""
  Imprecisão de ponto flutuante
  Double-precision floating-point format IEEE 754
  https://en.wikipedia.org/wiki/Double-precision_floating-point_format
  https://docs.python.org/pt-br/3/tutorial/floatingpoint.html
"""
num_1 = 0.1
num_2 = 0.7
num_3 = num_1 + num_2
print(num_3)
print(f'{num_3:.2f}')
print(round(num_3, 2))


"""
  Desempacotamento em chamadas de métodos e funções
"""
string = 'ABCD'
lista = ['Maria', 'Gu', 'Zé', 1]
tupla = 'Python', 'Javscript', 'Go'
print(*lista)  # É a mesma coisa que: print('Maria', 'Gu', 'Zé', 1)
print(*string)
print(*tupla)

salas = [
  ['Maria', 'Helena'],
  ['Jorge'],
  ['Ney']
]
print(*salas)


"""
  Operação ternária (condicional de uma linha)
  <valor> if <condição> else <outro_valor>
"""
condition = 5 > 3
isBigger = 'Maior' if condition else 'Menor'
print(isBigger)