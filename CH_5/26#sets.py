# Sets don't have repetative items
'''
a = {1,6,9,7,1}
print(type(a))
print(a)
'''
# Properties:
#                 1. sets are unordered
#                 2. sets are unindexed
#                 3. There is no way to change items in sets.
#                 4. Sets cannot contain duplicate values

# Operations: 
s = {1,8,2,3}

# to print length of set
print(len(s))

s.remove(3)
print(s)

#removes random element
s.pop()
print(s)

# s.clear()
# print(s)
