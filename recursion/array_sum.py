def sum_array(n):
    if len(n) == 0:
        return 0
    else:
        first= n[0]
        rest= n[1:]
    return first + sum_array(rest)

print(sum_array([1,2,3,4,5]))