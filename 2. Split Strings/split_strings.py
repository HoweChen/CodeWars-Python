def solution(s):
    if len(s) == 0:
        return []
    else:
        count = 0
        empty_str = ''
        result = []
        for s_itr in s:
            if count == 2:
                result.append(empty_str)
                count = 0
                empty_str = ''
            count += 1
            empty_str += s_itr
        result.append(empty_str)
        if len(result[-1]) == 1:
            result[-1] += '_'
        return result

    # good answer
    # if len(s) % 2 != 0: s = s + "_"
    # cadena = []
    # for (x, y) in zip(s[0::2], s[1::2]):
    #     cadena.append(x + y)
    # return cadena

print(solution('abcdefg'))
print(solution(''))

# Complete the solution so that it splits the string into pairs of two
# characters. If the string contains an odd number of characters then it
# should replace the missing second character of the final pair with an
# underscore ('_').

# Examples:

# solution('abc') # should return ['ab', 'c_']
# solution('abcdef') # should return ['ab', 'cd', 'ef']
