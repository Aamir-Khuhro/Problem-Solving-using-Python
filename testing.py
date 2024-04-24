# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 18:54:11 2024

"""

# Take n numbers from user and return max
max = -999999999
for _ in range(int(input())):
    num = float(input())
    if num > max:
        max = num
print("Maximum", max)

# Find the second lowest element from the list
grades = [20, 20.1, 20.01, 20.001]

second_lowest_grade = lowest_grade = float('inf')
for grade in grades:
    if grade < lowest_grade:
        second_lowest_grade = lowest_grade
        lowest_grade = grade
    elif grade < second_lowest_grade and grade != second_lowest_grade:
        second_lowest_grade = grade
    
        
print(second_lowest_grade)




#
records = []
scores = []
names = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    records.append([name, score])
    scores.append(score)
    names.append(name)
    

# print("records", records)
# print("names", names)
# print("scores", scores)
name, grade = ['Aamir Ali', 34.5]
print(name, grade)


grades = [41, 42, 33, 33, 41, 41, 55, 74, 73, 48]
unique_gradse = set(grades)
print(unique_gradse)


result = 'xxxx'  in "Hello my is exxxxx - Aamir Ali."
print(result)



    

# scores = [record[1] for record in records]
# sorted_scores = sorted(scores)
# sec_min = sorted_scores[1]


first_min = scores[0]
sec_min = scores[0]

for score in scores:
    if score < first_min:
        first_min = score   
print("First Min:", first_min)

        
for score in scores:
    if score != first_min and score < sec_min:
        sec_min = score
print("Second Min:", sec_min)


for record in records:
    if record[1] == sec_min:
        names.append(record[0])
        
sorted_names = sorted(names)
for name in sorted_names:
    print(name)
    

    
# Second Minimum in the list
nums = [35, 36, 33, 33, 33, 31, 31, 31, 37]
first_min = nums[0]
sec_min = nums[0]

for num in nums:
    if num < first_min:
        first_min = num
        
    
        
for num in nums:
    if num != first_min and num < sec_min:
        sec_min = num
        
for num in nums:
    if num == sec_min:
        print(num)
    
    
names = ["Saleem", "Noor Ahemd", "Aamir Ali"]
sorted_names = sorted(names)
print(sorted_names)

# Does list satifies some condition
numbers = [4, 5, 2, -3, 4, -4, 2, -2]
has_negative = False

for num in numbers:
    if num < 0:
        has_negative = True
        break
print(has_negative)


numbers = [4, 5, 2, -3, 4, -4, 2, -2]
has_negative = any(x < 0 for x in numbers)
print(has_negative)

name = "Aamri Ali Khuhro"
has_upper = any(ch.isupper() for ch in name)
print(has_upper)


# Is there any prime number in the list of given numbers
def prime(num):
    flag = True
    for div in range(2,num//2 + 1):
        if num % div == 0:
            return False
    return flag

numbers = [4, 6, 8, 10]
has_prime = any(prime(num) for num in numbers)
print(has_prime)


# Find the number of uppercase and lowercase letters in a text string
txt = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum
dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident,
sunt in culpa qui officia deserunt mollit anim id est laborum.'''

import re
print('Total Upper Case: ', len(re.findall('[A-Z]', txt)))
print('Total Lower Case: ', len(re.findall('[a-z]', txt)))
print('Total characters: ', len(txt))
print('Total words:', len(txt.split()))


txt = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum
dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident,
sunt in culpa qui officia deserunt mollit anim id est laborum.'''

# Split the text into words based on whitespace characters
words = txt.split()

# Count the number of words
num_words = len(words)

print("Total words:", num_words)
