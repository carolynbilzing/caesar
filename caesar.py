def alphabet_position(letter):
    letter = letter.lower()
    alphabet ="abcdefghijklmnopqrstuvwxyz"
            
    return alphabet.index(letter)

def rotate_character(char,rot):
    alphabet ="abcdefghijklmnopqrstuvwxyz"
    isupper = char.isupper()
    position = alphabet_position (char)
    newPosition = position + rot
    
    newPosition = newPosition % 26
    newLetter = alphabet[newPosition]
    if isupper:
        newLetter = newLetter.upper()
    return newLetter

def encrypt (text,rot):
    keyposition = 0
    encrypted = ""
    for char in text:
        if not char.isalpha():
            encrypted = encrypted + char
        else:
            encrypted = encrypted + rotate_character(char,rot)
                
    return encrypted