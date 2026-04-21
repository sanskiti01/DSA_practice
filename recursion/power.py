def power(x,n):
    if n==0:
        return 1
    if n==1:
        return x
    if n<0:
        x = 1/x
        n = -n

    half = power(x,n//2)
    
    if n % 2 == 0:
        return half * half
    else:
        return x*half*half
print(power(3,2)) 
print(power(4,2)) 