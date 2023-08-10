def generate_n_chars(n, c):
    palavra = ''
    for _ in range(n):
        palavra = palavra + c
    return palavra

def histogram(list_of_int):
    for i in list_of_int:
        print (generate_n_chars(i, '*'))  