def get_primes(seq):
    for num in seq:
        if num <= 1:
            continue

        for div in range(2, num):
            if num % div == 0:
                break
        else:
            yield num

print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))