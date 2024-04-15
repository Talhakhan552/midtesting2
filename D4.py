# --------QUESTION NO.1-------------
# string are immutable
# name=str(input("Enter your name:"))
# print(name.upper())
# print(name.lower())
# # print(name)
# strip=str(input("strip a character:"))
# print(name.rstrip())


# name = str(input("Enter your name:"))
# alpha=input("type any char:")

# print(alpha)
# # print(name)
# print(name.rstrip(alpha))

#-----------CHATGPT---------------

# Get the user's name
user_name = input("Please enter your name: ")

# Ask the user for a character to remove
char_to_remove = input("Enter a character you want to remove from your name: ")

# Remove the specified character from the name
new_name = user_name.replace(char_to_remove, '')

# Print the modified name
print("Your name with", char_to_remove, "removed:", new_name)

# -----------------------------------------------------------------------------------

name=input("Enter your name:")
rem_char=input("char to be removerd:")

new_name=name.replace(rem_char,"talha" )
print(new_name)









         

