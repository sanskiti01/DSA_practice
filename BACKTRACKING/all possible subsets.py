def backtrck(start,path):
    print(path)

    for i in range(start,len(nums)):
        path.append(nums[i])
        backtrck(i+1,path)
        path.pop()

nums = [1, 2, 3]
backtrck(0, [])