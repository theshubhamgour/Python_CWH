def max(n1,n2,n3):
    if(n1>n2):
        if(n1>3):
            return n1
        else:
            return n3
    else:
        if(n2>n3):
            return n2
        else:
            return n3

m = max(4,5,98)
print("The Greater number is: "+str(m))