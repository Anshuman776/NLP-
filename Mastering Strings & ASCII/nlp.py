def upper(text):
    string = ''
    for char in text:
        # Check if the character is a lowercase letter (ASCII range 97-122)
        if ord(char) >= 97 and ord(char) <= 122:
            # Convert to uppercase by subtracting 32 from ASCII value
            string += chr(ord(char) - 32)
        else:
            # Add the character as is if it's not a lowercase letter
            string += char
    return string

def lower(text):
    string = ''
    for char in text:
        # Check if the character is an uppercase letter (ASCII range 65-90)
        if ord(char) >= 65 and ord(char) <= 90:
            # Convert to lowercase by adding 32 to ASCII value
            string += chr(ord(char) + 32)
        else:
            # Add the character as is if it's not an uppercase letter
            string += char
    return string

def check_alpha(text):
    c = 0  # Initialize a counter to track the number of alphabetic characters
    for i in text:  # Loop through each character in the input string 'text'
        # Check if the character is an uppercase or lowercase letter
        if((ord(i) >= 65 and ord(i) <= 90) or (ord(i) >= 97 and ord(i) <= 122)):
            c += 1  # Increment the counter if the character is a letter
    # If the total number of characters in the string is equal to the number of letters
    # then it means all characters are alphabetic, so return True
    if(len(text) == c):
        return True
    else:
        return False  # Return False if there are any non-alphabetic characters

def check_digit(text):
    c = 0  # Initialize a counter to track the number of digit characters
    for i in text:  # Loop through each character in the input string 'text'
        # Check if the character is a digit (ASCII values for '0' to '9' are 48 to 57)
        if((ord(i) >= 48 and ord(i) <= 57)):
            c += 1  # Increment the counter if the character is a digit
    # If the total number of characters in the string is equal to the number of digits
    # then it means all characters are digits, so return True
    if(len(text) == c):
        return True
    else:
        return False  # Return False if there are any non-digit characters

def title(text):
    # Initialize an empty list to store the words with title case
    output = []
    
    # Loop through each word in the input text
    for word in text.split(' '):
        # Append the word with the first letter capitalized and the rest in lowercase
        output.append(word[0].upper() + word[1:].lower())
    
    # Join the words into a single string and return the result
    return ' '.join(output)


def capitalize(text):
     result = '' 
     first_char = text[0].upper()
     rest_of_text = text[1:].lower()
     result = first_char + rest_of_text 
     return result

def check_alnum(text):
    c=0
    for i in text:
        if((ord(i) >= 65 and ord(i) <= 90) or (ord(i) >=97 and ord(i) <= 122) or (ord(i) >= 48 and ord(i) <= 57)):
            c+=1
    if(len(text) == c):
        return True 
    else:
        return False 