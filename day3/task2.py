def devisers(num):
    l = []
    for i in range(1, int(num/2+1)):
        if num % i == 0:
            l.append(i)
    return l
