numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for i in numbers:
    k = 0
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            k += 1
    if k >= 1:
        not_primes.append(i)
    else:
        primes.append(i)

print('Primes: ', primes)
print('Not primes: ', not_primes)
