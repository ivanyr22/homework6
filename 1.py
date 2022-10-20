length = int(input('Введите размер массива:'))
list_a = [0] * length
list_b = [0] * length
from random import randint
for i in range(length) :
    list_a[i] = randint(0, 10)
    list_b[i] = randint(0, 10)

print('Первый массив: ', list_a)
print('Второй массив: ', list_b)


def bubble_sort(l):
    for i in range(1, len(l)) :
        for j in range(len(l) - i) :
            if (l[j] > l[j + 1]): l[j], l[j + 1] = l[j + 1], l[j]


def find_intersection(l1, l2):
    intersection = []
    iter1 = 0
    iter2 = 0
    
    while iter1 < length and iter2 < length:
        if (list_a[iter1] > list_b[iter2]) : iter2 += 1
        elif (list_a[iter1] < list_b[iter2]) : iter1 += 1
        else:
            intersection.append(list_b[iter2])
            iter1 += 1
            iter2 += 1
    return intersection

intersection = find_intersection(bubble_sort(list_a), bubble_sort(list_b))

if (len(intersection) == 0):
    print('Общих элементов нет')
else:
    print('Общие элементы: ', intersection)




