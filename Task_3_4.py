

# 1. Напишите цикл, который выводит на экран и удаляет с начала элементы списка, пока он не останется пустым

l = [3,4,5,6,7,8,1,2]

length = len(l)

while True:
    print(l.pop(0), sep=' ', end=' ')
    length = len(l)
#    print(l)
    if length > 0:
        pass
    if length == 0:
        break
print('List is empty')

# 3. Напишите цикл, который выводит на экран и удаляет элементы списка от самого маленького до самого большого, пока он не останется пустым.


list1 = [3, 4, 555, 6, 7, 3345, 234, 532, 23453, 343]

b = sorted(list1, key=None, reverse=False)

while True:
    print(b.pop(0), sep=' ', end=' ')
    length = len(b)
#    print(b)
    if length > 0:
        pass
    if length == 0:
        break
print('List is empty')

print(b)





