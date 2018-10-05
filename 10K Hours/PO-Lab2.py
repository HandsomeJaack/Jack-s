class Student:
    def __init__(self, name, surname, theirdname, year, home, fac, kurse):
        self.name = name
        self.surname = surname
        self.theirdname = theirdname
        self.year = year
        self.home = home
        self.fac = fac
        self.kurse = kurse

    def info(self):
        print("ФИО {} {} {}, год рождения {}, адресс {}, факультет {}, курс {}.".format(self.name,
                self.surname, self.theirdname, self.year, self.home, self.fac, self.kurse))


Student1 = Student("Бутаков", "Дмитрий", "Викторович","1999", "Москва", "3-ий", "3-ий")
Student2 = Student("Михайлов", "Егор", "Олегович", "1998","Москва", "3-ий", "3-ий")
Student3 = Student("Гриньков", "Владислав", "Леонидович","1998", "Москва", "3-ий", "3-ий")
data_base = [Student1, Student2, Student3]
while True:
    print("Выберите пункт для работы с базой данных: \n",
          "1 -Показать всех студентов в базе \n",
          "2 - Добавить студента в базу \n",
          "3 - Удалить студента из базы \n",
          "4 - Откорректировать профиль студента \n"
          )
    punkt = input()
    if punkt == '1':
        for index, member in enumerate(data_base):
            print("{}. ".format(index+1), end=""), member.info()
    if punkt == '2':
        print("Введите фамилию студента: ")
        name = input()
        print("Введите имя студента: ")
        surname = input()
        print("Введите отчество студента: ")
        theirdname = input()
        print("Введите год рождения: ")
        year = input()
        print("Введите город проживания: ")
        home = input()
        print("Введите факультет: ")
        fac = input()
        print("Введите курс: ")
        kurse = input()
        stud = Student(name, surname, theirdname, year, home, fac, kurse)
        data_base.append(stud)
        print("Добавлен новый студент! ")
        stud.info()
    if punkt == "3":
        print("Выберете номер студента в списке для удаления: ")
        del_num = int(input())
        del data_base[del_num-1]
        print("Студент удален! Обновленная база: ")
        for index, member in enumerate(data_base):
            print("{}. ".format(index+1), end=""), member.info()
    if punkt == "4":
        print("Выберете номер студента в списке для корректировки: ")
        chek_num = int(input())
        print("Выберете параметр для корректировки: \n",
              "1 - Фамилия \n",
              "2 - Имя \n",
              "3 - Отчество \n",
              "4 - Год рождения \n",
              "5 - Город проживания \n",
              "6 - Факультет \n",
              "7 - Курс \n")
        param = input()
        if param == "1":
            print("Введите новую фамилию:")
            data_base[chek_num-1].name = input()
        if param == "2":
            print("Введите новое имя:")
            data_base[chek_num-1].surname = input()
        if param == "3":
            print("Введите новое отчество:")
            data_base[chek_num-1].theirdname = input()
        if param == "4":
            print("Введите год рождения:")
            data_base[chek_num-1].year = input()
        if param == "5":
            print("Введите город:")
            data_base[chek_num-1].home = input()
        if param == "6":
            print("Введите новый факультет:")
            data_base[chek_num-1].fac = input()
        if param == "7":
            print("Введите новый курс:")
            data_base[chek_num-1].kurse = input()
        print("Изменения успешны!")
        data_base[chek_num-1].info()
    else:
        print("Неверный символ!")
    print("Хотите выйти? Y/N")
    exit = input()
    if exit == 'N':
        pass
    else:
        break
