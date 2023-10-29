import random
# import secrets
import string

def valid_number(prompt: str):
    while True:
        try:
            n = int(input(prompt))
            if n <= 0:
                raise Exception
        except Exception:
            print('Invalid Input !')
        else:
            return n

def print_opt(options_dict: dict):
    print()
    c = 1
    print('Configure Password Options:')
    for key, value in options_dict.items():
        print('{}. {}: {}'.format(c, key, value))
        c += 1
    print('{}. {}'.format(c, 'Generate Password'))
    print()

def toggle_opt(options_dict: dict, options_name: str):
    options_dict[options_name] = not options_dict[options_name]
    print_opt(options_dict)

options = {'letters_lower': True,
           'letters_upper': True,
           'digits': True,
           'special_chars': True}

def check_opt(options_dict: dict):
    if not (options_dict['letters_lower'] or options_dict['letters_upper']):
        print('Atleast One Of letters_lower Or letters_upper Must Be Toggled True !')
        return False
    else:
        return True

letters_lower = string.ascii_lowercase
letters_upper = string.ascii_uppercase
digits = string.digits
special_chars = string.punctuation

print_opt(options)
while(True):
    choice = valid_number('Enter option to toggle: ')
    if choice == 1:
        toggle_opt(options, 'letters_lower')
    elif choice == 2:
        toggle_opt(options, 'letters_upper')
    elif choice == 3:
        toggle_opt(options, 'digits')
    elif choice == 4:
        toggle_opt(options, 'special_chars')
    elif choice == 5:
        if check_opt(options):
            break
    else:
        print('Invalid Choice !')

letters = alphabet = prompt = ''
min_digits = min_special = 0
pwd_length = valid_number('Enter Password Length: ')

for key in options.keys():
    if options[key]:
        if 'letters' in key:
            letters += eval(key)
        alphabet += eval(key)

while True:
    if options['digits']:
        min_digits = valid_number('Enter Minimum Digits: ')
    if options['special_chars']:
        min_digits = valid_number('Enter Minimum Special Characters: ')
    if min_digits + min_special >= pwd_length:
        print('Total Number Of special_chars + digits Cannot Be >= Password Length')
    else:
        break

while True:
    pwd = ''
    # pwd += ''.join(secrets.choice(alphabet) for _ in range(pwd_length))
    pwd += ''.join(random.choice(alphabet) for _ in range(pwd_length))

    if (any(char in letters for char in pwd) and
        sum(char in digits for char in pwd) >= min_digits and 
        sum(char in special_chars for char in pwd) >= min_special):
            break

print('Generated Password:', pwd)
