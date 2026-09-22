
def Armstrong_number(n):
    num = n
    total =0
    nod = len(str(n))

    while num > 0:
        last = num % 10
        total += (last ** nod)
        num //= 10

    return total == n

n = 153
print(Armstrong_number(n))    