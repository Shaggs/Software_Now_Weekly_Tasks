# Submission by S.Rees
# Question 1:

list = []
print("Enter 3 numbers:")
for x in range(0, 3):
    num = input("enter a number: ")
    list.append(num)
big = max(list)
small = min(list)
print("the largets number is "+str(big) + " The smallest is " + str(small))

# Question 2:
a = 1
for x in range(0, 6):
    print(a)
    a = a + 2
a = a - 3
for x in range(0, 6):
    print(a)
    a = a - 2

# Question 3:
print("Please enter 10 number and we shall see if they are odd or even")
print("lets get started")

# set odd as 0
odd = 0
# set even as 0
even = 0
# use a for loop to ask the question 10 times
for x in range(0, 10):
    # get users input
    number = input("please enter a number: ")
    if number == "":
        print("No number entered this will not be counted")
    else:
        # change the Number sting to an intiger
        if int(number) % 2 == 0:
            # If the Number is even a 1 to the even score
            even = even+1
        else:
            # if the number is not even we use else to add 1 to the odd score
            odd = odd+1
# print out results and turn odd and even from an initger to a string for printing
print("There are " + str(odd) + " odd numbers and " + str(even) + " even numbers")

# Question 4
while True:
    month = str(input("Please enter a month or quit to exit:"))
    if month == 'February':
        print("No. of days:28 or 29 (Leap Year)")
        running = True
    elif month in ("January", "March", "May", "July", "August", "October", "December"):
        print("No. of days:31")
        continue
    elif month in ("April", "June", "September", "November"):
        print("No. of days:30")
        continue
    elif month == "quit":
        print("Exiting")
        break
    else:
        print("Please enter the right spelling.")
