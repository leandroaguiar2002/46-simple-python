def len_of_word(words):
    #['apple', 'banana'] => [5, 6]
    nums = []
    for i in words:
        nums.append(len(i))
    return nums
    #return [len(word) for word in words]
    