age=int (input("Hi! what is your Age \n ") )
print(type(age))  # Print the type of age variable
if age < 18:
    print("You are not eligible for vote.")  # Print if the user is not eligible for vote
else:
    print("You are eligible for vote.")