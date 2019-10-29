def checkio(first, second):
    first_set = set(first.split(','))
    second_list = second.split(',')
    common_words = []
    for word in second_list:
        if word in first_set:
            common_words.append(word)
    return ','.join(sorted(common_words))


print(checkio("hello,world", "hello,earth") == "hello")
print(checkio("one,two,three", "four,five,six") == "")
print(checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two")
print(checkio("one,two,three", "four,five,one,two,six,three"))
print(checkio('', ''))
