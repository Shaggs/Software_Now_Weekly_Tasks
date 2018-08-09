# Week 4

# Q1

data = [1, 2, 5, 6, 7, 8]
total = 0
for item in data:
    total += item
print(total)

# Q2


def sum(low, high):
    data = []
    new_total = 0
    for number in range(low, high):
        new_total += number
    return(new_total)
 low = int(input("Please Enter the lowest number"))
 high = int(input("Please enter the highest number"))
 print(sum(low, high))

# Q3
 data = {"b": 20, "a": 35}
 print(data)
 data.update({"b": -20})
 print(data)
 data.update({"c": 40})
 print(data)
 del data["b"]
 print(data)
 data.update({"b": -20})
 for key, value in data.items():
    print(key, value)

# Q4
My_List = {8, 9, 33, 1, 3, 6, 8, 55, 43}
print(min(My_List))
# Q5
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
endlist = {}
endlist.update(dic1)
endlist.update(dic2)
endlist.update(dic3)
print(endlist)
