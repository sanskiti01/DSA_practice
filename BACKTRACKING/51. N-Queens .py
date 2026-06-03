def queen1(n:int):
    res =[]
    board = [["."]*n for _ in range(n)]


    cols = set()
    dig1 = set()
    dig2 = set()
    def backtrack(row):
        if row == n:
            res.append(["".join(r)for r in board])
            return
        for col in range(n):
            if col in cols:
                continue
            if (row-col)in dig1:
                continue
            if (row+col)in dig2:
                continue
        
            board[row][col]="Q"
            cols.add(col)
            dig1.add(row-col)
            dig2.add(row+col)

            backtrack(row+1)

            board[row][col]="."
            cols.discard(col)
            dig1.discard(row-col)
            dig2.discard(row+col)

    backtrack(0)
    return res  

print(queen1(4))  



