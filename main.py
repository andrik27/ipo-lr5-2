str1 = input("Введите первую строку: ")
str2 = input("Введите вторую строку: ")

str1 = str1.replace(" ", "").lower()
str2 = str2.replace(" ", "").lower()

are_anagrams = sorted(str1) == sorted(str2)

print("Строки являются анаграммами:", are_anagrams)