def translate(pal):
    nova = ''
    for i in pal:
        if i in ('a', 'e', 'i', 'o', 'u') or pal == ' ':
            nova = nova + i
        else:
            nova = nova + i + 'o' + i
    return nova