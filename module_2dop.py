def kod(chislo):
    n = ''
    for i in range(1, chislo):
        for j in range(i + 1, chislo):
            if chislo % (i + j) == 0:
                n += str(i) + str(j)
    return n

print('Введите число: ')
print(kod(int(input())))