for i in range(6):
    for j in range(1, 6 - i):
        print(end=" ")
    for k in range(2 * i - 1):
        print('*', end="")
    print()
for x in range(2):
    print('    *')
