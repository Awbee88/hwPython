# 3. Задайте список из n чисел последовательности фибоначи и выведите экран

# n = int(input('Input your number: '))
# def fibonaci(num):
#     a = 0
#     b = 1
#     nums = []
#     for i in range(num):
#         a, b = b, a + b
#         nums.append(a)
#     return nums
# print(fibonaci(n))



### Функция - на вход принимает список, а возвращает словарь, где 5 элементов min max imax i min avr
'''
nums = [1,11,23,45,234]
def elements(spisok):
    my_dict = {}
    largest = 0
    smalest = spisok[0] 
    total = 0
    for i in spisok:
        if i>largest: largest = i
    my_dict['max'] = largest
    for i in spisok:
        if i<smalest: smalest = i
    my_dict['min'] = smalest
    maxi = spisok.index(largest)
    my_dict['maxi'] = maxi
    mini = spisok.index(smalest)
    my_dict['mini'] = mini
    for i in spisok:
        total += i
    avr = total/len(spisok)
    my_dict['avr'] = avr
    return my_dict

print(elements(nums))

file = open('LIB1.txt', 'a')
for key in elements(nums):
    file.write(f'{key} - {elements(nums)[key]}')
    file.write('\n')
    file.close
'''

## Задайте список из N элементов, заполненных числами из промежутка [-N, N]. сохраните список в формате JSON.
import json
num = int(input('Input your num: '))
def n_spisok(n):
    a = []
    for i in range(-num, num+1):
        a.append(i)
    return(a)
bibl = n_spisok(num)
print(bibl)

with open ('data.json', 'w', encoding='utf-8') as jsn:
    jsn.write(json.dumps(bibl, ensure_ascii=False))
print('БД успешно сохранена')