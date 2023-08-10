def longest_word(words):
    nums = []
    for i in words:
        nums.append(len(i))
    return max(nums)