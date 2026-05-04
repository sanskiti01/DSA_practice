def binary(digit):
    result = []

    def backtrack(path):
        if len(path)==digit:
            result.append(path)
            return
        
        backtrack(path + "0")
        backtrack(path + "1")

    backtrack("")
    return result

print(binary(3))