def is_prime(func):
    def wrapper(*args, **kwargs):
        sum_ = func(*args)
        for i in range(2, sum_ - 1):
            if sum_ % i == 0:
                print('Составное')
                break
            else:
                print('Простое')
                break
        return sum_
    return wrapper


@is_prime
def sum_three(*args):
    return sum(args)


result = sum_three(2, 3, 6)
print(result)
