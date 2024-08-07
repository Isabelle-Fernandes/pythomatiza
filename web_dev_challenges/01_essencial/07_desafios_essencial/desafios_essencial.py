import math

def mega_combinations():
    return(math.comb(60,6))

def word_len(word):
    return(int(len(word)))

def full_name(first_name, last_name):
    return(first_name.capitalize() + " " + last_name.capitalize())

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

def calculator(first_number, second_number, operation):
    if operation == "soma":
        return first_number + second_number
    elif operation == "multiplicação":
        return first_number * second_number
    elif operation == "subtração":
        return first_number - second_number
    elif operation == "divisão":
        return first_number / second_number
    else:
        return 0