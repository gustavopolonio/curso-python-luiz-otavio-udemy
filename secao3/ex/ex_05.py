# from unidecode import unidecode

phrase = 'aaaoooo'

i = 0
times = 0
most_appeared_letter = ''
phrase_lower = phrase.lower().strip().replace(' ', '').replace('.', '')

while i < len(phrase_lower):
  current_letter = phrase_lower[i]
  times_current_letter = phrase_lower.count(current_letter)

  if times_current_letter > times:
    most_appeared_letter = current_letter
    times = times_current_letter

  i += 1

print(f'A letra que mais apareceu foi: "{most_appeared_letter}", {times}x')