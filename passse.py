import rondom
import string

 def generate_password(length,numbers=true,special_characters=true):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation
    print(letters,digits,special)
