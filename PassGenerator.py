import random

def GeneratePassword(Pass,length):
    Password = "".join(random.sample(Pass, length))
    print("Generated Password Is : ", Password)

lwr = "abcdefghijklmnopqrstuvwxyz"
upr = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = "0123456789"
sp_chars= "&@!$*-_#"

# Combining All Characters.
Pass = lwr + sp_chars + num + upr      

# Using Ternary Operator To Fix The Length Of The Password , Based On User Input.

strength = input(" Enter The Strength Of The Password Required - ( Weak / Strong / Very Strong) : ")
if strength.isalpha() == True :
    length = 6 if (strength == "weak") else 12 if (strength =="strong") else 18
    GeneratePassword(Pass,length)

else : print("Please Enter Valid Input( Weak / Strong / Very Strong)")
