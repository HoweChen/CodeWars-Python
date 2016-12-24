def sum_consecutives(s):
    result = []
    last_one = None
    last_sum = s[0]
    for s_itr in s:
        if last_one != s_itr:
            last_one = s_itr
            result.append(last_sum)
            last_sum = 0
        last_sum += s_itr
    result.append(last_sum)
    result.remove(result[0])
    return result

    # better answer
    # prev = None
    # x = []
    # for i in s:
    #     if i == prev:
    #         x[-1] += i
    #     else:
    #         x.append(i)
    #     prev = i
    # return x
print(sum_consecutives([1, 4, 4, 4, 0, 4, 3, 3, 1]))
print(sum_consecutives([1, 1, 7, 7, 3]))
