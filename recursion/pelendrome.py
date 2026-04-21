def pelendrome(strr):
    if len(strr)<=1:
        return True
    else:
        if strr[0]!=strr[-1]:
            return False
        return pelendrome(strr[1:-1])
print(pelendrome("kalli"))
print(pelendrome("lol"))