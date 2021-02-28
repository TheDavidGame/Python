def f1(arr):
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
        elif arr[3] == 'hel':
            return 12
    elif arr[0] == 'ebnf':
        if arr[3] == 'hel':
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

def f2():
    


def f3():
    arr = [["0.57", "19.10.2004", "+7 188 821-7259"],
           ["0.86", "23.08.2001", "+7 193 013-0609"],
           ["0.73", "19.04.2000", "+7 604 422-1041"]]

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
                    arr[i][j] = str(arr1[2]) + '.' + str(arr1[1]) + '.' + str(arr1[0]) + ' '

             elif j == 2:
                    arr2 = arr[i][j].split(' ')
                    arr3 = arr2[2].split('-')
                    arr4 = arr2[2][4:6]
                    arr5 = arr2[2][6:8]
                    arr[i][j] = '(' + str(arr2[1]) + ')' + ' ' + str(arr3[0]) + '-' + str(arr4) + '-' + str(arr5)
    print(arr)

# print(all)
# print(table)
# for i in range(len(arr)):
#     for j in range(len(arr[i])):
#         if j == 1:
#             arr1 = arr[i][j].split('.')
#             all = all + str(arr1[2]) + '.' + str(arr1[0]) + '.' + str(arr1[1])
#             # print(all)
#
# for i in range(len(arr)):
#     for j in range(len(arr[i])):
#         if j == 2:
#             arr1 = arr[i][j].split(' ')
#             arr2 = arr1[2].split('-')
#             arr3 = arr1[2][4:6]
#             arr4 = arr1[2][6:8]
# print('(' + arr1[1] + ')' + ' ' + arr2[0] + '-' + arr3 + '-' + arr4)
# print(all)
