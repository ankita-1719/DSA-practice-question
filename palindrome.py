
def palindrome_number(n):
    res = 0
    num = n
    while num > 0:
        last = num % 10
        res = (res * 10 ) + last
        num //= 10
    return n == res

n = 567435
print(palindrome_number(n))    
# T C = O(log 10 (n))