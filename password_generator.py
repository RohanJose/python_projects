import string,random
random_characters = string.ascii_letters + "!@#$%^&*()"+"1234567890"

print("PASSWORD GENERATOR\n")
length = int(input("Enter length of the password: "))
password = ""
for i in range(length):
    password = password + random_characters[random.randint(0,len(random_characters))]

print("GENERATED PASSWORD :",password)