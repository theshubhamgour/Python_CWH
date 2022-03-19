# program to create a dictonay of hindi words
# with values provide option to look it up for the user

dict = {
    "pankha" : "fan",
    "dabba": "tiffin",
    "vastu": "Item"
}

print("options are: ",dict.keys())
s = input("Enter hindi word: ")
print("The meaning is: ",dict.get(s))