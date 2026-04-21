#reverse the array:

def rev(strr):
    if len(strr)==0:
        return ""
    else:
        return strr[-1]+rev(strr[:-1])
print(rev("kalli"))