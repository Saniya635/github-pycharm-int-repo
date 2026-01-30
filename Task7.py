a = int(input())
b = int(input())

if a > b:
    a, b = b, a

for num in range(a, b + 1):
    if num > 1:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                breakk
        if is_prime:
            print(num, end=" ")
