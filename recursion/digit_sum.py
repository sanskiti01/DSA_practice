def digit_sum(n):
    if (n < 10):
        return n
    else:
        a = n%10
        return a + digit_sum(n//10)
print(digit_sum(1234))