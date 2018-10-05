class ShortInputException(Exception):
    def __init__(self, lenght, atleast):
        self.lenght = lenght
        self.atleast = atleast


try:
    text = input("Введите что-нибудь --> ")
    if len(text) < 3:
        raise ShortInputException(len(text), 3)
except EOFError:
    print("Лол, конец файла.")
except ShortInputException as ex:
    print("ShortInputException: Длина введенной строки -- {}; \
            ожидалось минимум {}".format(ex.lenght, ex.atleast))
else:
    print("ИСключений не было")