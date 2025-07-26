# Open the file in write mode ('w')
file = open("myfile.txt", "w")

# Write content to the file
file.write("Hello, this is a sample text file.\n")
file.write("Python makes file handling easy!\n")

# Close the file
file.close()

print("Content written to 'myfile.txt' successfully.")