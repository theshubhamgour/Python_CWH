#program to demostrate function for factorial

# n = 4
# pro = 1
# for i in range(n):
#     pro = pro*(i+1)
# print(pro)

def fact(n):
    pro = 1
    for i in range(n):
        pro = pro*(i+1)
    return pro


f = fact(4)
print(f)
