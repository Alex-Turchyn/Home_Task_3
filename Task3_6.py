

# 1)	Пишем функцию, которая попросит ввести число. Пока он не введёт правильно, просите его ввести. Функция возвращает введённое число.
# * Теперь далее для других задач с числами, вы можете пользоваться этой функцией, а не простым input!


def vvedi_chislo ():
    a = int(input("Vvedit chislo"))
    b = int(input('Vvedit sche onde chislo'))
    return a, b

a = vvedi_chislo()

print(a)



#3 Пишем функцию, которая попросит пользователя ввести слово (строка без пробелов в середине, а вначале и в конце пробелы могут быть). Пока он не введёт правильно, просите его ввести. Функция возвращает введённое слово.

def is_year_leap(year):

    if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
        print("usual year")
        return True
    else:
        print("intercalary year")
        return False

is_year_leap(1981)