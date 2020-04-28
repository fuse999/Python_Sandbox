def sockMerchant(n, ar):
    ar.sort()
    pairs = 0
    while len(ar) > 1:
        if ar[0] == ar[1]:
            ar.pop(0)
            ar.pop(0)
            pairs += 1
        else:
            ar.pop(0)
    return pairs

count = 15
lst2 = [6, 5, 2, 3, 5, 2, 2, 1, 1, 5, 1, 3, 3, 3, 5]

sockMerchant(count, lst2)