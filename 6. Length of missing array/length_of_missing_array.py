def get_length_of_missing_array(array_of_arrays):

    if not array_of_arrays:
        return 0
    else:
        result = []
        for itr in array_of_arrays:
            if not itr:
                return 0
            else:
                result.append(len(itr))
        result.sort()
        return sorted(set(range(result[0], result[-1] + 1)).difference(result))[0]

print(get_length_of_missing_array(
    [[1, 2], [4, 5, 1, 1], [1], [5, 6, 7, 8, 9]]))
