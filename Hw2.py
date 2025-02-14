import random

# Exercise-1
print("Hello World\n")

# Exercise-2
print("7 + 3 =", 7+3)
print("7 - 3 =", 7-3)
print("7 * 3 =", 7*3)
print("7 / 3 =", 7/3, "\n")

# Exercise-3
age = 21
print("I am", age, "years old.\n")

# Exercise-4
Celsius = int(input("Enter Celsius: "))
print("The temperature in Fahrenheit is: ", (Celsius * 9/5) + 32, "\n")

# Exercise-5
Number = int(input("Enter a number: "))
if Number % 2 == 0:
   print(Number, "is even.\n")
else:
   print(Number, "is odd.\n")

# Exercise-6
Number = int(input("Enter a number: "))
if Number > 0:
   print(Number, "is positive.\n")
elif Number < 0:
   print(Number, "is negative.\n")
else:
   print(Number, "is zero.\n")

# Exercise-7
Numbers = [5, 3, 7, 4]
Numbers.append(10)
Numbers.remove(3)
print(len(Numbers))
Numbers.sort()
print(Numbers, "\n")

# Exercise-8
Total = 1
Number = int(input("Enter a number: "))
for i in range(1,Number + 1):
   Total = Total*i
print("The Factorial is:", Total, "\n")

# Exercise-9
Number = int(input("Enter a number: "))
for i in range(1, 10):
   print(Number, "*", i, "=", Number * i)
print("\n")

# Exercise-10
list = [1, 2, 3, 4, 5]
Sum = 0
for i in range(0,len(list)):
   Sum += list[i]
print("The sum is:", Sum,"\n")

# Exercise-11
Ans = random.randint(1, 20)
Guess = 0
while Guess != Ans:
   Guess = int(input("Enter a guess:"))
   print("Your guess:", Guess)
   if Guess > Ans:
       print("Too high. Try again")
   elif Guess < Ans:
       print("Too low. Try again")
   else:
       print("Correct!\n")

# Exercise-12
Total = 0
String = input("Enter a string: ")
for i in String:
   if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
       Total += 1
print("Number of vowels:", Total)

# Exercise-13
for i in range(1, 100 + 1):
   if i % 3 == 0 and i % 5 == 0:
       print("FizzBuzz")
   elif i % 3 == 0:
       print("Fizz")
   elif i % 5 == 0:
       print("Buzz")

# Exercise-14
List = []
String = input("Enter a string: ")
for i in range(len(String), 0, -1):
    List.append(String[i - 1])

String = "".join(List)
print("Reversed:", String)
