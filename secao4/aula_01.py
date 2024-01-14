"""
  Introdução às funções (def)
  Parâmetro é o nome da "variável" dentro dos parênteses da fç, argumento é o valor passado para o parâmetro no momento da execução da função.
  Por padrão, funções python retornam None
"""

def imprimir(a, b, c = 10):  # 'a', 'b' e 'c' são parâmetros
  print('Oi', a, b, c)

imprimir(1, 2, 3)  # '1', '2 e '3' são argumentos
imprimir(0, 5)


"""
  Como saber ser um parâmetro foi enviado para uma fç ou não:
  Seto o valor padrão desse parâmetro como 'None' e confiro se ele é None
"""
def sum(x, y, z = None):
  if z is None:
    print(x + y)
  else:
    print(f'O valor de z é: {z}')
    print(x + y + z)

sum(2, 10)
sum(2, 10, 0)


"""
  Escopo de funções em Python
  Escopo significa o local onde aquele código pode atingir.
  Existe o escopo global e local.
  O escopo global é o escopo onde todo o código é alcançavel.
  O escopo local é o escopo onde apenas nomes do mesmo local podem ser alcançados.
"""
x = 1

def function_1():
  # global x  # Estou falando que o x abaixo é o global
  # x = 2  # Atualizando o valor do x global
  x = 2

  def function_2():
    y = 3
    # global x  # Também atualiza o valor do x global
    x = 4
    print(x, y)
  
  function_2()
  print(x)

print(x)
function_1()
print(x)
