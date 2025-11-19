
#als je zelf een error wil veroorzaken omdat iets niet klopt.

def set_age():
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError("age cannot be negative")

    return age

set_age()


#als je een error wil opvangen zodat je programma niet crasht. (rond risicovolle code geplaatst)
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("That's not a valid number")

try:
    result = 10 / x
except ZeroDivisionError:
    print("Cannot divide by zero")

