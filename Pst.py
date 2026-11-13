# Neon :- It is a number in which the sum of the digit of its square is equal to the original number.
# For ex :- n = 9 
# n = 9 * 9 = 81
# 81 = 8 + 1 = 9
# 9 is original number and it is called Neon number.

num=int(input("Enter a number"))
sum = 0
square = num * num
while square > 0:
    digit = square % 10
    sum = sum + digit
    square = square // 10
if sum == num:
    print(" Neon number")
else:
    print("Not neon number")
