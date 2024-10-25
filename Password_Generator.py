import random
import string

length = int(input('Enter the length:'))

password = ''


small = string.ascii_lowercase
capital = string.ascii_uppercase
digit = string.digits
char = string.punctuation

characters = small + capital + digit + char

for i in range(length):
    random_number = random.choice(characters)
    password = password + random_number


print (f"Password is {password}")