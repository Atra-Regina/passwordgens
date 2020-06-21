import string
import secrets

# defining characters

characters = string.ascii_letters + string.digits

# letting the user choose how many characters their password will have
user_input = int(input("Type the number of characters you want your password to have and press Enter: "))
password = ''.join(secrets.choice(characters) for i in range (user_input))


print("This is your new strong random password:\n" + password)
