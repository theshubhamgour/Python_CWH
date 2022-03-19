a = {"Fast": "In a Quick manner",
          "Gidean": "An A.I",
          "Marks": [1, 2, 5]}
# prints item          
print(a.items())

# retuns the list containg keys
print(a.keys())

a1 = {"Jarvis": "AI hai"}
a.update(a1)
print(a.items())

# prints the value of the specified keys
print(a.get("Marks"))
