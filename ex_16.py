def filter_long_words(list_of_words, n):
    new = []
    for i in list_of_words:
        if len(i) > n:
           new.append(i)
    return new 
    #return [new for new in list_of_words if len(new) > n]
    