def Queen2(n):
    cols = set()
    dig1 = set()
    dig2 = set()

    def backtrack(row):
        if row == n:
            return 1
        
        count = 0

        for col in range(n):

            if col in cols or row-col in dig1 or row+col in dig2:
                continue

            cols.add(col)
            dig1.add(row-col)
            dig2.add(row+col)

            count += backtrack(1+row)
            
            cols.discard(col)
            dig1.discard(row-col)
            dig2.discard(row+col)

        return count
    return backtrack(0)

print(Queen2(6))