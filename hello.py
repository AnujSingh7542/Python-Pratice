### A Disarium Number is a number in which the sum of its digits raised to their respective positions is equal to the original number.
# jab kisi number ke har digit ko uski position ki power se raise karke sabhi results ko 
# add karte hai aur sum original numbet ke equal hota hai, toh use Disarium Number kehte hai.
num =int(input("Enter the number"))
length =len(str(num))
sum = 0
temp = num 
if num > 0:
    digit = temp % 10
    sum = sum + digit ** length
    temp = temp // 10
    length = length - 1
if num == sum:
    print("It is  Diasorium Number")
else:
    print('It is not Diasorium Number')