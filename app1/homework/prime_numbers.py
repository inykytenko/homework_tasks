n = int(input())
prime_numbers = []
k = 0
for i in range(2, n+1):
    for j in range(2, i):
        if i % j == 0:
            k = k + 1

    if k == 0:
        prime_numbers.append(i)
    else:
        k = 0
print(prime_numbers)