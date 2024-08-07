def has_letter(letter, input_word):
    for i in input_word:
        if i == letter:
            return True
    return False


def uper_case(input_word):
    return(input_word.upper())


def lower_case(input_word):
    return(input_word.lower())

def capitalize(input_word):
    return(input_word.capitalize())

def reverse(input_word):
    return(input_word[::-1])

print(reverse("gabriel"))