def pig_it(text):
    # your code here
    text_list = text.split(' ')
    result = ''
    for item in text_list:
        if len(item) == 1:
            item = item + 'ay'
        else:
            item = item[1:] + item[0] + 'ay'
        result += item + ' '
    return result[:-1]

print(pig_it('Pig latin is cool'))
print(pig_it('This is my string'))
print(pig_it('?'))
print(pig_it('uisQay ustodietcay psosiay ustodescay ?'))
