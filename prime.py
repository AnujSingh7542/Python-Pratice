# Write a program to print Nth prime Number.
n =int(input("Enter the location of the number"))
count = 0
num = 1
while count < n:
    num = num +1
    prime = True
    for i in range(2,num):
        if num % i == 0:
            prime = False
            break 
    if prime:
        count = count + 1
        print("The",n,"th prime number is",num)
