def vowel_filter(function):
    VOWELS = "aeiou"
    def wrapper():
        vowel = [v for v in function() if v in VOWELS]
        return vowel
    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]
print(get_letters())