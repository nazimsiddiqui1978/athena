f = open("data.txt","+r")
# Open the file in read mode
content = f.read()
# Read the content of the file
f.close()
# Close the file after reading
print(content)
# Print the content of the file