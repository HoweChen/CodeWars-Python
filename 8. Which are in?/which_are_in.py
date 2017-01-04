def in_array(array1, array2):
    # your code
    result = []
    for item_1 in array1:
        for item_2 in array2:
            if item_1 in item_2 and item_1 not in result:
                result.append(item_1)
    result = sorted(result)
    return result

a1 = ["live", "arp", "strong"]
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
r = ['arp', 'live', 'strong']
print(in_array(a1, a2))
