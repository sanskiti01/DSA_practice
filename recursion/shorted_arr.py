def shorted_arr(arr):
    if len(arr)<=1:
        return True
    if arr[0]>arr[1]:
        return False
    return shorted_arr(arr[1:])
print(shorted_arr([1,3,4,6]))
print(shorted_arr([2,4,1,5]))
