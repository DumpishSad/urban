def decoder(n):
    results = ''
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            if n % (i + j) == 0:
                results += str(i)
                results += str(j)
    return results


print(decoder(11))
