def unique_in_order(iterable):
    result = []
    if iterable:
        index = 0
        temp_char = iterable[0]
        while index < len(iterable):
            # print(iterable[index])
            if iterable[index] != temp_char:
                result.append(temp_char)
                temp_char = iterable[index]
            index += 1
        result.append(iterable[-1])
    return result

    # Better answer
    # result = []
    # prev = None
    # for char in iterable[0:]:
    #     if char != prev:
    #         result.append(char)
    #         prev = char
    # return result

print(unique_in_order('AAAABBBCCDAABBB'))
print(unique_in_order('ABBCcAD'))
print(unique_in_order([1, 2, 2, 3, 3]))
print(unique_in_order([]))


# Implement the function unique_in_order which takes as argument a
# sequence and returns a list of items without any elements with the same
# value next to each other and preserving the original order of elements.

# For example:

# unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
# unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
# unique_in_order([1,2,2,3,3])       == [1,2,3]
