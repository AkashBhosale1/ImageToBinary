#################################################### PROG2 #########################################
#####convert text into binary numbers
# Open the text file
with open("textfile.txt", "r") as file:
    # Read the contents of the file
    text = file.read()

# Convert the text to binary (0 and 1)
binary_text = ""
for char in text:
    # Get the Unicode code point of the character
    code_point = ord(char)
    # Convert the code point to binary and append it to the binary text
    binary_text += format(code_point, "08b")

# Save the binary text to a file
with open("Binary_text.txt", "w") as file:
    file.write(binary_text)