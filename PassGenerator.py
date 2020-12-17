import random


def GeneratePassword(Pass,length):
    Password = "".join(random.sample(Pass, length))
    print("Generated Password Is : ", Password)


lwr = "abcdefghijklmnopqrstuvwxyz"
upr = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = "0123456789"
sp_chars= "&@!$*-_#"
Pass = lwr + sp_chars + num + upr
length = 12
GeneratePassword(Pass,length)
