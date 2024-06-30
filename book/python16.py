import random
passlen = int(input("Please enter the length of the password you want to generate:"))
s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
p = "".join(random.sample(s, passlen))
print(p)
input()  # This last line is just waiting for user input and does not produce any output.