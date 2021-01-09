import random


def GeneratePassword(Pass,length):
    Password = "".join(random.sample(Pass, length))
    print("Generated Password Is : ", Password)


lwr = "abcdefghijklmnopqrstuvwxyz"
upr = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = "0123456789"
sp_chars= "&@!$*-_#"
Pass = lwr + sp_chars + num + upr
strength =  input("Enter The Strength Of The Password Required - (Weak/Strong/VeryStrong) : ")
length = 6 if (strength == "Weak") else  12 if (strength =="Strong") else 18
GeneratePassword(Pass,length)
