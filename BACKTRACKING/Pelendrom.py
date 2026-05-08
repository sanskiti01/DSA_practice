def pelendrom(s):
    result = []

    def backtrack(start,path):
        if start == s:
            result.append(s)
            return

        for i in range(start, len(s)):
            subs = s[start:1+1]

            if subs == subs[::-1]:
                path.append(subs)
                backtrack(i+1,path)
                path.pop()

    backtrack(0,[])
    return result

print(pelendrom("aaababa"))