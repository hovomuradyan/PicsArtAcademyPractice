def same_parity(n, *args):
    l1 = []
    for i in args:
        if i % n == 0:
            l1.append(i)
    return l1
