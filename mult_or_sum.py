# calculating the multiplication and sum of two numbers
num1 = int(input("Tell me first number:\n"))  #Input from user
num2 = int(input("Tell me second number:\n"))  #Input from user

ans = num1 * num2  #Storing the product of two number
ans1 = num1 + num2  #Storing the sum of two number
if ans <= 1000:  #Appling if condition
  print(ans)
else:  #"IF" condition do not work then "else" condition will work
  print(f"Your result is {ans1}")  #Finally printing the result
