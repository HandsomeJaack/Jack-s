import string, re


def exclude_extra(text):
    regex = re.compile('[%s]' % re.escape(string.punctuation))
    text_without_punctuation = regex.sub('', text)
    text_without_spaces = text_without_punctuation.replace(" ", "")
    just_string = text_without_spaces.lower()
    return just_string


def reverse(text):
    just_string = exclude_extra(text)
    return just_string[::-1]


def is_palindrome(text):
    just_string = exclude_extra(text)
    return just_string == reverse(text)


something = input("Введите текст: ")
print(reverse(something))
if is_palindrome(something):
    print("Да, это полиндром")
else:
    print("Нет, это не полиндром ")