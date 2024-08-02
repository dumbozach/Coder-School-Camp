import random
import string
while True:

    chars = list(string.ascii_letters + string.punctuation)
    char_count = int(input("how many characters do you want your password to be?"))
    password = ""

    if char_count > 50:
        print("Password length is too long")
    else:

        for i in range(char_count):
            randnum = random.randint(0,84)
            randchar = chars[randnum]
            password = password + randchar

        print(password)