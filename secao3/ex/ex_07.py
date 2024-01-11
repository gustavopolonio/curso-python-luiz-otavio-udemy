"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""

def list_items_from_list():
  print('\nA lista atual tem os seguintes items:\n')
  if len(my_list) == 0:
    print('Lista vazia :(')
    return
  for index, list_item in enumerate(my_list):
    print(f'{index}: {list_item}')

my_list = []

def handle_list():
  user_action = input('\n[i]nserir [a]pagar [l]istar [s]air: ')

  if user_action == 'i':
    new_value = input('Valor: ')
    my_list.append(new_value)
    handle_list()
  elif user_action == 'a':
    delete_at_index = input('Escolha o índice para apagar: ')

    try:
      delete_at_index_int = int(delete_at_index)
      removed_item = my_list.pop(delete_at_index_int)
      print(f'\nO item "{removed_item}" foi removido da lista!')
      list_items_from_list()
    except IndexError:
      print('Índice inválido')
    except ValueError:
      print('Por favor, digite um num. inteiro')
    except Exception:
      print('Erro desconhecido')

    handle_list()
  elif user_action == 'l':
    list_items_from_list()
    handle_list()
  elif user_action == 's':
    print('Saindo do programa...')
  else:
    print('Escolha uma opção válida')
    handle_list()

handle_list()
list_items_from_list()