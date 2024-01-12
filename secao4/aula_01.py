"""
  Introdução às funções (def)
  Por padrão, funções python retornam None
"""

def imprimir(a, b, c = 10):  # 'a', 'b' e 'c' são parâmetros
  print('Oi', a, b, c)

imprimir(1, 2, 3)  # '1', '2 e '3' são argumentos
imprimir(0, 5)