def validar_alfanumericamente(cadena_texto):
    
    """
    Evalua cada letra de la cadena de texto, si en esta se encuentra algun caracter
    que no sea una letra o un numero, retorna 'False', en caso contrario retorna
    'True'.
    """

    caracteres_validos = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "a", "b", "c", "d",
    "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
    "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F",
    "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
    "U", "V", "W", "X", "Y", "Z"]

    valor_a_retornar = False

    for letra in cadena_texto:

        if letra in caracteres_validos:
            valor_a_retornar = True
        else:
            valor_a_retornar = False
            break

    return valor_a_retornar
