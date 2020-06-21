import string
import secrets


# defining characters

characters = string.ascii_letters + string.digits + string.punctuation


# random password with 16 letters using secrets module
password = ''.join(secrets.choice(characters) for i in range (16))

print("Here's your new random 16 characters password: \n" + password)
