import random
import string

print("Welcome to the random password generator")

def myPassword():
    length=int(input("\nEnter the required length of the password:"))
    lowerData=string.ascii_lowercase
    upperData=string.ascii_uppercase
    digitData=string.digits
    symbolData=string.punctuation
    combine=lowerData+upperData+digitData+symbolData
    randomCombination=random.sample(combine,length)
    password="".join(randomCombination)
    print(password)
    myPassword()
myPassword()