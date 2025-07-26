# Append new content to the file
f = open("data.txt", "a")
f.write("\nwe never forgot his contribution in cricket")
f.close()

# Now read and print all content
f = open("data.txt", "r")
content = f.read()
print(content)
f.close()