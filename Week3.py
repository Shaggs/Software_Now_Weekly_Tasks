# by Shane Rees

# Question 1:
"""Write a program that takes input from the user and when the user press enter
 to quit the program gives the sum of all even numbers and the sum of
 all odd numbers."""
even = []
odd = []
while 1:
    x = input("Please enter a number and press enter or just enter to exit: ")
    if x == "":
        break
    elif int(x) % 2 == 0:
        even.append(x)
    else:
        odd.append(x)

print(even)
print(odd)
AddEven = 0
AddOdd = 0
for number in even:
    AddEven = AddEven + int(number)
for number in odd:
    AddOdd = AddOdd + int(number)

print("Sum of even number: ", str(AddEven))
print("Sum of odd number: ", str(AddOdd))

# Question 2
"""Write a program to take a string as input and your program should:

Print the same string with all lowercase letters. Note:  You should not use
islower() function.

Print the number of vowels  ‘aeiou’ present in the string.
"""
strin = input("Please enter some text and ill show you the vowels:  ")
strin = str.lower(strin)
print(strin)
vowels = 0
for letter in strin:
    if(letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or
       letter == 'u'):
        vowels = vowels+1
print("There are " + str(vowels) + " Vowels in yout string")

# Question 3
"""Write a program to ask input from the user the number of asterisk to print
and how many lines need to be printed."""

asterisk = int(input("how many asterisk do you want to print? "))
line = int(input("How many lines do you want this? "))

for x in range(line):
    print("*" * asterisk)

# Question 4
"""Write a program to check whether the user input number is a prime
number or not.
"""

number = int(input("Please enter a number and we will see if its a PRIME number: "))
if int(number) > 1:
    for x in range(2, int(number)):
        if int(number) % x == 0:
            print("The number " + str(number) + " is not PRIME")
        else:
            print("The number " + str(number) + " is PRIME")


# question 5
"""Write a program to print the numbers in the following format:
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""
for i in range(1, 5+1):
    for r in range(1, i+1):
        print(r, end="")
    print()
# Question 6
"""Write a program that accepts a sentence and calculate the number of letters and digits."""

digit = 0
letter = 0
string = input("Please enter a sing with numbers and digits: ")
if sting == "":
    print("nothing has been entered")
else:
    for item in string:
        if item.isdigit():
            digit = digit += 1
        elif item.isalpha():
            letter = letter += 1
        else:
            print(letter + " is not a letter or a digit.... Good try :P")
    print("Total letters found: " + letter)
    print("Toltal numbers found: " + digits)
print("All done see you next week :)")
