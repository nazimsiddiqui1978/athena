a=[1,2,3,4,5] # Example of a list
b=(1,3,4,5) # Example of a tuple
c={"1": "one", "2": "two"} # Example of a dictionary
d=set([1, 2, 3]) # Example of a set
print(a, b, c, d) # Print all variables
print(b)    
print(c)
print(d)
c["1"] = "uno" # Modify dictionary value    
print(c) # Print modified dictionary
del c["2"] # Delete a key-value pair from dictionary
print(c) # Print dictionary after deletion

