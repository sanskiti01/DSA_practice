def combination_sum(nums, target):
    result = []

    def backtrack(start,path,total):
        

            if total == target:
                result.append(path[:])
                return

            if total > target:
                return
            
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i,path,total+nums[i])
                path.pop()

    backtrack(0,[],0)
    return result

print(combination_sum([1,2,3],2))
