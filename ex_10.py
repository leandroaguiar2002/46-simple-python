def overlapping(list_a, list_b):
    for i in list_a:
        for j in list_b:
            if i == j:
                return True
    return False