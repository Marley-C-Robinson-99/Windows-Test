#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def is_two(num): 
    return num == 2 or num == '2' #Checking for string or int
print(is_two(2))
#%%

def is_vowel(strng):
    return strng in ('aeiouAEIOU')
print(is_vowel("Hello"))
#%%

def is_consonant(l):
    return is_vowel(l) == False
#%%

def cap(word):
    if word[0] != ('aeiouAEIOU'):
        return word.title() #Used ttitlecase to capitalize first word in case of SSV in value
    else:
        return word
#%%

def calculate_tip(bill, tip):
    total = 0 #setting base var to 0
    total += (tip * bill) #Math for calc tim  + total
    return total + total

#%%

def apply_discount(price, d):
    return price * (d / 100) #assuming a whole int input for d, converts percentage to decima

print(apply_discount(10, 15))
#%%
def handle_commas(num):
    nums = num.split(",") #splitting along commas
    return "".join(nums) #Rejoining the list insto a str
    
print(handle_commas("100,000"))
#%%
def remove_vowels(word):
    new_word =[] #Empty list for use later
    for letter in word:
        if is_vowel(letter) == False: #calling a previous function
            new_word.append(letter) #If word is not vowel, append to empty list
    return "".join(new_word) #joins list into a string
print(remove_vowels("Apple"))
#%%
def get_letter_grade(grade):
    if grade > 0 and grade < 60: #doing grade ranges from F to A
        return("F")
    elif grade >= 60 and grade < 70:
        return("D")
    elif grade >= 70 and grade < 80:
        return("C")
    elif grade >= 80 and grade < 90:
        return("B")
    elif grade >= 90 and grade < 100:
        return("A")
#%%
def normalize_name(name):
    newname = "" #init empty str
    namestrp = name.strip() #stripping name value
    for char in namestrp: 
        if (char.isnumeric() == True) or (char.isalpha()) or (char == " "): #checking for chars, nums, and spaces
                newname += char #if is num, char, or space, add to empty str
    normal_name = newname.replace(" ", "_") #replacing spaces with underscores
    return normal_name.lower() #Finally lowercasing
#%%
def cumulative_sum(nums):
    lst1 = [] #init empty list
    n = 0 #init empty var
    for num in range(0,len(nums)):
        n += nums[num] #for each number, += n to nums[index], then moves on and does the same with n = the sum of previous numbers
        lst1.append(n) #appending n to the list with each iteration
    return lst1
        
print(cumulative_sum([10, 27.5, 10]))
