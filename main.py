def anagrams(string1, string2): # Функция
    string1 = string1.replace(" ","").lower() # Убирает пробелы первой строки
    string2 = string2.replace(" ","").lower() # Убирает пробелы второй строки
    return sorted(string1) == sorted(string2) # Возвращение полученного результата
string1 = input("Введите первую строку: ") # Ввод первой строки
string2 = input("Введите вторую строку: ") # Ввод второй строки
if anagrams(string1, string2): # Условие (задание функции)
    print("Строки являются анаграммами") # Вывод: Строки являются анаграммами
else: # Если строки не анаграммы
    print("Строки не являются анаграммами") # Вывод: Строки не являются анаграммами