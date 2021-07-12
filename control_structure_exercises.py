# -*- coding: utf-8 -*-
#%% cell 1
usr1 = input("What day of the week? >")
if usr1.lower() == "monday":
    print( "I hate mondays")
if usr1.lower() in ("monday", 'tuesday', 'wednesday', 'thursday', 'friday'):
    print("Not quite the weekend yet")
else:
    print("FREEDOM (until monday)")
    print("Thank god its not monday")
#%% cell 2
hrs_worked = int(input("How many hours worked this week? >> "))
pay_hr = int(input("Pay per hour? >> "))
weekly_pay = hrs_worked * pay_hr
if hrs_worked <= 40:
    print( weekly_pay)
elif hrs_worked > 40:
    for hr in range(0, hrs_worked):
        if hr > 40:
            weekly_pay = weekly_pay + (pay_hr * 1.5)
    print(weekly_pay)
#%% cell 3
i = 5
while i <= 14:
    i += 1
    print(i)
#%% cell 4
i2 = 100
while i2 > 5:
    i2 -= 5
    print(i2)
#%% cell 5
i3 = 2
while i3 < 1000000:
    print(i3)
    i3 = i3 ** 2
#%% cell 6
usr2 = int(input("Throw me a number >> "))
for num in range(1,11):
    print(f"{usr2} x {num} = {str(usr2 * num)}")

#%% cell 7
for r in range(1, 10):
        print(r * str(r))
#%% cell 8
usr3 = int(input("Please enter an odd number between one and fifty >> "))

while (usr3 > 1 & usr3 < 50) & (usr3 % 2 != 0):
    print("Number to skip is:", usr3)
    lst = list(range(1 ,50))
    if usr3 <= 1 ^ usr3 >= 50:
        break
    for i in lst:
        if i == usr3:
            print("Skip")
            continue
        if i % 2 == 0:
            continue
        print("Here is an odd:", i)
    if i == 49:
        break
#%% cell 9
usr4 = int(input("Please enter an even number >> "))
while usr4 > 0:
    usrrange = list(range(0, usr4 +1))
    for i in usrrange:
        print(i)
        if i == usrrange:
            break
    break
#%% cell 10
usr4 = int(input("Please enter an even number >> "))
while usr4 > 0:
    usrrange = reversed(list(range(1, usr4 +1)))
    for i in usrrange:
        print(i)
        if i == 0:
            break
    break
#%% cell 11
for n in range(1, 101):
    print(n)
    if n % 3 == 0 & n % 5 == 0:
        print("fizzbuzz")
        continue
    elif n % 3 == 0:
        print("fizz")
        continue
    elif n % 5 == 0:
        print("buzz")
        continue
#%% cell 12
usr5 = int(input("What number would you like to go up to? >> "))
while usr5 > 0:
    usr5range = list(range(1, usr5 +1))
    for i in usr5range:
        print(str(i ** 2), "|" + str(i**3))
        continue
    break

#%% cell 13
usr6 = ""
while usr6 != "exit":
    usr6 = int(input("Please enter your grade or char to exit >> "))
    if usr6 >= 0 and usr6 <= 100:
        if usr6 > 0 and usr6 < 60:
            print("F")
        elif usr6 >= 60 and usr6 < 63:
            print("D-")
        elif usr6 >= 63 and usr6 < 66:
            print("D")
        elif usr6 >= 66 and usr6 < 70:
            print("D+")
        elif usr6 >= 70 and usr6 < 73:
            print("C-")
        elif usr6 >= 73 and usr6 < 76:
            print("C")        
        elif usr6 >= 76 and usr6 < 80:
            print("C+")
        elif usr6 >= 80 and usr6 < 83:
            print("B-")
        elif usr6 >= 83 and usr6 < 86:
            print("B")
        elif usr6 >= 86 and usr6 < 90:
            print("B+")
        elif usr6 >= 90 and usr6 < 93:
            print("A-")
        elif usr6 >= 93 and usr6 < 96:
            print("A")
        elif usr6 >= 96 and usr6 < 100:
            print("A+")
        continue
    break