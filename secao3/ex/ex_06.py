"""
Faça um jogo para o usuário adivinhar qual a palavra secreta.
  - Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
  - Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu usuário.
"""

import os


def play_words(secret_word):
  user_current_word = '*' * len(secret_word)
  counter = 0

  while secret_word != user_current_word:
    input_letter = input('Digite uma letra: ')
    counter += 1

    if len(input_letter) > 1:
      print('Digite apenas uma letra')
      continue
  
    if input_letter in secret_word:
      for i in range(len(secret_word)):
        if input_letter == secret_word[i]:
          user_current_word = user_current_word[:i] + input_letter + user_current_word[i + 1:]

    print(user_current_word)
  
  os.system('clear')
  print(f'Você ganhou, palavra: {secret_word}. Você usou {counter} tentativas. ')


play_words('futebol')