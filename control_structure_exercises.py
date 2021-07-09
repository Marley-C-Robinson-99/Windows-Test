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
i2 = 0
while i2 <= 100:
    i2 = 2
    print(i2)
#%% cell 5
i3 = 2
while i3 < 1000000:
    print(i3)
    i3 = i3 ** 2
#%% cell 6
usr2 = int(input("Throw me a number >> "))
for num in range(1,11):
    print(f"{usr2} x {num} = ", str(usr2 * num))
    
    
#%% cell 7
for r in range(1, 10):
        print((r * str(r))+ " ")
#%% cell 8
usr3 = int(input("Please enter an odd number between one and fifty >> "))
print("Number to skip is:", usr3)
while (usr3 > 1 & usr3 < 50) & usr3 % 2 != 0:
    lst = list(range(1 ,50))
    if usr3 <= 1 ^ usr3 >= 50:
        break
    for i in lst:
        if i == usr3:
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