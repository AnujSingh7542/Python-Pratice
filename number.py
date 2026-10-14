# write a program to count the occurance of a particular digit in number 
num =int(input("Enter a number "))
m =int(input("Enter a digit"))
count = 0
while num > 0:
    digit = num % 10
    if digit == m:
        count = count + 1
    num = num // 10 
print(count)