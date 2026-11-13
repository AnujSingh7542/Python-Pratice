# Automorphic Number :- It is a number whose square end with the same digits as the number itself.
# for ex:- n = 5 
# n = 5 * 5 = 25

num =int(input("Enter a number"))
square = num * num
digit = len(str(num))
if square % (10 ** digit) == num:
    print("Automorphic Number")
else:
    print("Not Automorphic Number")
