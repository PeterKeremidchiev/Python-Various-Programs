def words_sorting(*args):
    dict_of_words = {}
    for arg in args:
        dict_of_words[arg] = 0
        for ch in arg:
            dict_of_words[arg] += ord(ch)

    sum_of_values = 0

    for value in dict_of_words.values():
        sum_of_values += value
    if sum_of_values % 2 != 0:
        dict_sorted = sorted(dict_of_words.items(), key=lambda x: -x[1])
        return "\n".join(f"{word} - {num}" for word, num in dict_sorted)
    else:
        dict_sorted = sorted(dict_of_words.items(), key=lambda x: x[0])
        return "\n".join(f"{word} - {num}" for word, num in dict_sorted)


print(
 words_sorting(
 'cacophony',
 'accolade'
 ))
