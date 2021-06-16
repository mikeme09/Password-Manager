import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8, 10)
nr_numbers = random.randint(2, 4)
nr_symbols = random.randint(2, 4)


def generate_random_password():
    password = []

    for n in range(nr_letters):
        rand_letters = random.randrange(len(letters))
        password.extend(letters[rand_letters])

    for n in range(nr_numbers):
        rand_numbers = random.randrange(len(numbers))
        password.extend(numbers[rand_numbers])

    for n in range(nr_symbols):
        rand_symbols = random.randrange(len(symbols))
        password.extend(symbols[rand_symbols])

    password_list = ""
    random.shuffle(password)

    for n in password:
        password_list += n
    return password_list
