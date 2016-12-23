def array_diff(a, b):
    if len(a) == 0 or len(b) == 0:
        pass
    else:
        for b_itr in b:
            while b_itr in a:
                a.remove(b_itr)
    return a

    # good answer
    # return [x for x in a if x not in b]

print(array_diff([1, 2, 2], [2]))
print(array_diff([-12, -20], [-6, -18]))
