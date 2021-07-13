#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def is_two(num):
    return num == 2 ^ num == '2'
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
        return word.title()
    else:
        return word
#%%

def calculate_tip(bill, tip):
    total = 0
    total += (tip * bill)
    return total + total

#%%

def apply_discount(price, d):
    return price * (d / 100)

print(apply_discount(10, 15))
#%%
def handle_commas(num):
    nums = num.split(",")
    return "".join(nums)
    
print(handle_commas("100,000"))
#%%
def remove_vowels(word):
    new_word =[]
    for letter in word:
        if is_vowel(letter) == False:
            new_word.append(letter)
    return "".join(new_word)
print(remove_vowels("Apple"))
#%%
def get_letter_grade(grade):
    if grade > 0 and grade < 60:
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
    newname = []
    namestrp = name.strip()
    for char in namestrp:
        if (char.isnumeric() == True) or (char.isalpha()) or (char == " "):
                newname.append(char)
    normal_name = "".join(newname)
    normal_name = normal_name.replace(" ", "_")
    return normal_name.lower()
print(normalize_name("    3453Marley Robinson    "))
print(normalize_name("      Marley   Robinson46546    "))
print(normalize_name("    Marley Robinson  "))