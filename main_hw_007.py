# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, 
# Вам стоит написать программу. Винни-Пух считает, что ритм есть, 
# если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. 
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. 
# Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры. 
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

# *Пример:*

# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
#     **Вывод:** Парам пам-пам 




# def check_rhythm(poem):
#     lines = poem.split()  # Разделяем стихотворение на строки
    
#     # Проверяем число слогов в первой фразе
#     first_line_syllables = count_syllables(lines[0])
    
#     # Проходим по остальным фразам и проверяем число слогов
#     for line in lines[1:]:
#         syllables = count_syllables(line)
#         if syllables != first_line_syllables:
#             return "Пам парам"  # Ритм нарушен
    
#     return "Парам пам-пам"  # Ритм соблюден

# def count_syllables(line):
#     words = line.split('-')  # Разделяем фразу на слова
#     syllables = 0
#     for word in words:
#         syllables += count_vowels(word)
#     return syllables

# def count_vowels(word):
#     vowels = 'аеёиоуыэюя'  # Список гласных букв
#     count = 0
#     for letter in word:
#         if letter.lower() in vowels:
#             count += 1
#     return count

# # Пример использования
# poem = input("Введите стихотворение Винни-Пуха: ")
# result = check_rhythm(poem)
# print(result)


# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), 
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. 
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны. 
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). 
# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, 
# например, у операции умножения.

# *Пример:*

# **Ввод:** `print_operation_table(lambda x, y: x * y) ` 
# **Вывод:**
# 1 2 3 4 5 6

# 2 4 6 8 10 12
# 3 6 9 12 15 18
# 4 8 12 16 20 24
# 5 10 15 20 25 30
# 6 12 18 24 30 36

def print_operation_table(operation, num_rows=6, num_columns=6):
    for i in range(1, num_rows + 1):
        for j in range(1, num_columns + 1):
            result = operation(i, j)
            print(f"{result:<5}", end="")
        print()

def multiply(x, y):
    return x * y

# print_operation_table(multiply, num_rows=6, num_columns=6)

print_operation_table(lambda x, y: x * y)
