import random

lower = 'abcdefghijklmnopqrstuvwxyz'
capital = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
special = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`}{|~'

#print(lower + '\n' + capital + '\n' + num + '\n' + special)

def split_string(word):
    return [char for char in word]

lower = split_string(lower)
capital = split_string(capital)
special = split_string(special)

def get_lower_char():
  return lower[random.randint(0, len(lower) - 1)]

def get_capital_char():
  return capital[random.randint(0, len(capital) - 1)]

def get_num():
  return str(random.randint(0, 9))

def get_special_char():
  return special[random.randint(0, len(special) - 1)]


def passd_generator(lenght, lower=True, capital=True, num=True, special=True):
    passd = ''
    for i in range(lenght):
        if lower == True and len(passd) < lenght:
            passd = passd + get_lower_char()
        if capital == True and len(passd) < lenght:
            passd = passd + get_capital_char()
        if num == True and len(passd) < lenght:
            passd = passd + get_num()
        if special == True and len(passd) < lenght:
            passd = passd + get_special_char()
    passd = ''.join(random.sample(passd, len(passd)))
    
    return passd
