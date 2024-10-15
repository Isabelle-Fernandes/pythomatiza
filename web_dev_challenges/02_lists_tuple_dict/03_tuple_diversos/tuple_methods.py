def tuple_sum():
    my_tuple = 1, 2, 3, 4, 5
    soma = 0

    for i in range(len(my_tuple)):
        soma += my_tuple[i]
    
    return(soma)


def find_second_element():
    # TODO: Retorne o segundo elemento da tupla 'my_tuple'
    my_tuple = 1, 2, 3, 4, 5
    return(my_tuple[1])


def find_out_typle_error():
    # TODO: Encontrar o erro no código abaixo
    # TODO: my_tuple não deverá ser modificada
    my_tuple = 1, 2, 3, 4, 5
    x = list(my_tuple)
    x.remove(1)
    x = tuple(x)
    return my_tuple
