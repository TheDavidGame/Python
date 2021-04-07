def f21(arr):
    if arr[0] == 'smt':
        return 13
    elif arr[0] == 'nim':
        if arr[3] == 'php':
            if arr[1] == 'sqf':
                return 8
            elif arr[1] == 'php':
                return 9
            elif arr[1] == 'grace':
                return 10
        elif arr[3] == 'mako':
            return 11
        elif arr[3] == 'hсl':
            return 12
        return 12
    elif arr[0] == 'ebnf':
        if arr[3] == 'hcl':
            if arr[1] == "sqf":
                return 5
            elif arr[1] == 'php':
                return 6
            elif arr[1] == 'grace':
                return 7
        elif arr[3] == 'mako':
            if arr[2] == 'tex':
                return 3
            elif arr[2] == 'shen':
                return 4
        elif arr[3] == 'php':
            if arr[1] == 'sqf':
                return 0
            elif arr[1] == 'php':
                return 1
            elif arr[1] == 'grace':
                return 2


print(f21(['nim', 'php', 'shen', 'hcl']))


def f22(number):
    a = number & 0b00000000000000000000000011111111
    b = number & 0b00000000000000000011111100000000
    c = number & 0b00001111111111111100000000000000
    d = number & 0b00010000000000000000000000000000
    e = number & 0b11100000000000000000000000000000

    b = b >> 8
    c = c >> 14
    d = d >> 28
    e = e >> 29
    numb = a | (b << 22) | (c << 8) | (d << 28) | (e << 29)
    return numb


# arr = [['0.00', '28.04.2000', '+7 483 689-0661'],
#        ['0.39', '20.09.2000', '+7 722 908-0854'],
#        ['0.50', '11.06.2003', '+7 350 895-8121']]
#


def f23(arr):
    for i, elem in enumerate(arr):
        for j, elem2 in enumerate(arr[i]):
            if j % 3 == 0:
                arr[i][j] = float(elem2)
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if j == 0:
                arr[i][j] = str(round(arr[i][j], 1))

            elif j == 1:
                arr1 = arr[i][j].split('.')
                arr[i][j] = str(arr1[2]) + '.' + str(arr1[1]) + '.' + str(arr1[0])

            elif j == 2:
                arr2 = arr[i][j].split(' ')
                arr3 = arr2[2].split('-')
                arr4 = arr2[2][4:6]
                arr5 = arr2[2][6:8]
                arr[i][j] = '(' + str(arr2[1]) + ')' + ' ' + str(arr3[0]) + '-' + str(arr4) + '-' + str(arr5)

    return sorting(arr)


def sorting(sub_li):
    sub_li.sort(key=lambda x: x[2])
    return sub_li
