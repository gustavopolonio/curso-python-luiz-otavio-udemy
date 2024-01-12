"""
  Calculo do primeiro dígito do CPF
  CPF: 746.824.890-70
  Colete a soma dos 9 primeiros dígitos do CPF multiplicando cada um dos valores por uma contagem regressiva começando de 10

  Ex.:  746.824.890-70 (746824890)
    10  9  8  7  6  5  4  3  2
  *  7   4  6  8  2  4  8  9  0
    70  36 48 56 12 20 32 27 0

  Somar todos os resultados: 70+36+48+56+12+20+32+27+0 = 301
  Multiplicar o resultado anterior por 10 => 301 * 10 = 3010
  Obter o resto da divisão da conta anterior por 11 => 3010 % 11 = 7
  Se o resultado anterior for maior que 9:
    resultado é 0
  contrário disso:
    resultado é o valor da conta

  O primeiro dígito do CPF é 7
"""

def calc_first_digit(cpf):
  raw_cpf_str = cpf.replace('.', '').replace('-', '')
  raw_cpf_str_9_digits = raw_cpf_str[:-2]

  digits_sum = 0
  multiplier = 10
  for digit in raw_cpf_str_9_digits:
    digits_sum += multiplier * int(digit)
    multiplier -= 1

  operation = (digits_sum * 10) % 11
  first_digit = operation if operation <= 9 else 0
  return first_digit


"""
  Calculo do segundo dígito do CPF
  CPF: 746.824.890-70
  Colete a soma dos 9 primeiros dígitos do CPF, MAIS O PRIMEIRO DIGITO, multiplicando cada um dos valores por uma contagem regressiva começando de 11

  Ex.:  746.824.890-70 (7468248907)
    11 10  9  8  7  6  5  4  3  2
  *  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
    77 40 54 64 14 24 40 36  0 14

  Somar todos os resultados: 77+40+54+64+14+24+40+36+0+14 = 363
  Multiplicar o resultado anterior por 10 => 363 * 10 = 3630
  Obter o resto da divisão da conta anterior por 11 => 3630 % 11 = 0
  Se o resultado anterior for maior que 9:
      resultado é 0
  contrário disso:
      resultado é o valor da conta

  O segundo dígito do CPF é 0
"""

def calc_second_digit(cpf):
  raw_cpf_str = cpf.replace('.', '').replace('-', '')
  raw_cpf_str_10_digits = raw_cpf_str[:-1]

  digits_sum = 0
  multiplier = 11
  for digit in raw_cpf_str_10_digits:
    digits_sum += multiplier * int(digit)
    multiplier -= 1

  operation = (digits_sum * 10) % 11
  second_digit = operation if operation <= 9 else 0
  return second_digit


def validate_cpf(cpf):
  raw_cpf_str = cpf.replace('.', '').replace('-', '')

  if (raw_cpf_str[0] * len(raw_cpf_str)) == raw_cpf_str:  # Invalidar cpf's do tipo: '000.000.000-00'
    print(f'O CPF {cpf} é inválido')
    return

  first_digit = calc_first_digit(cpf)
  second_digit = calc_second_digit(cpf)

  raw_cpf_str_9_digits = raw_cpf_str[:-2]
  calculated_cpf = raw_cpf_str_9_digits + str(first_digit) + str(second_digit)

  if raw_cpf_str == calculated_cpf:
    print(f'O CPF {cpf} é válido')
  else:
    print(f'O CPF {cpf} é inválido')


validate_cpf('746.824.890-70')
# validate_cpf('000.000.000-00')
# validate_cpf('276.254.310-02')