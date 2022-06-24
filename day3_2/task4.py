def odd_indexes(data):
    l1 = []
    for i in range(len(data)):
        if data[i] % 2 == 0:
            l1.append(i)
    return l1
