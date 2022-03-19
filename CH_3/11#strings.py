# String is a datatype in python
# three types: 
# single quote: a= 'Barry'
# double quote: b = "Barry"
# triple quote: c = '''BArry'''

name = "Shubham"
print(name)
# string slicing
print(name[1:4])

# below slicing will work same
print(name[0:4]) 
print(name[:4])

# function in string

# length of name
print(len(name))

# endswith
print(name.endswith("d"))

#count the occurence
print(name.count("a"))

# capitalize the first character of the string
print(name.capitalize())

#replace the character
print(name.replace("a", "o"))

# find the first occurance
print(name.find("h"))
