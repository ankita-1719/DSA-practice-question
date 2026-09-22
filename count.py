
def count_number(n):
    count = 0

    while n > 0:
        count += 1
        n //= 10
    return count

n = 5438
print(count_number(n))    
