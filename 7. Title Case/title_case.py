def title_case(title, minor_words=''):
    if not title:
        return ''
    else:

        title = title.title()
        if not minor_words:
            pass
        else:
            minor_words = minor_words.title()
            title = title.split(' ')
            minor_words = minor_words.split(' ')
            for index, value in enumerate(title):
                if value in minor_words:
                    title[index] = value.lower()
            title[0] = title[0].title()
            title = ' '.join(title)
    return title

print(title_case('', ''))
print(title_case('a clash of KINGS', 'a an the of'))
print(title_case('aBC deF Ghi', ''))
