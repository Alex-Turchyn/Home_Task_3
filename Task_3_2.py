

a = str(input("please enter the line sybmols: "))
b = len(a)

if b % 2 == 0:
    c = len(a) // 2
    print(a[0:c], a[c:], sep=' ')
elif b % 2 != 0:
    perv_dlinna = len(a) // 2 + 1
    vtor_dlinna = len(a) //2 + 1
    print(a[vtor_dlinna::], " ", a[0:perv_dlinna])