#write python code for prime number without function
num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, int(num/2)+1):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")

#Write python code for sum of all elements in a list using function Eg:- Input: [1,2,3,4] Output: 10 
def sum_list(lst):
    total = 0
    for i in lst:
        total += i
    return total
input_list = [1, 2, 3, 4]
result = sum_list(input_list)
print("The sum of all elements in the list is:", result)

#Write a python program to extract digits from alphanumeric string 
# Eg:- Input: "abc123xyz" Output: 123 
# Input: "a1b2c3" Output: 123 
# Input: "no digits here" Output: 0
import re
def extract_digits(s):
    digits = re.findall(r'\d', s)
    if digits:
        return int(''.join(digits))
    else:
        return 0
input_str1 = "abc123xyz"
input_str2 = "a1b2c3"
input_str3 = "no digits here"
print("Extracted digits from '{}': {}".format(input_str1, extract_digits(input_str1)))
print("Extracted digits from '{}': {}".format(input_str2, extract_digits(input_str2)))
print("Extracted digits from '{}': {}".format(input_str3, extract_digits(input_str3)))

# write python program to count number of vowels in a string.
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count
input_string = "Hello World"
vowel_count = count_vowels(input_string)
print("Number of vowels in '{}': {}".format(input_string, vowel_count))

# Again Write a python program to count number of volwels in a string. 
# Eg:- Input: "Hello World" Output: 3 
# Input: "Python Programming" Output: 4

def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count
input_string1 = "Hello World"
input_string2 = "Python Programming"
vowel_count1 = count_vowels(input_string1)
vowel_count2 = count_vowels(input_string2)
print("Number of vowels in '{}': {}".format(input_string1, vowel_count1))
print("Number of vowels in '{}': {}".format(input_string2, vowel_count2))

"""
Comaprision between zero-shot and few-shot prompting
Zero-shot prompting involves providing the model with a task or question without any prior examples or context
Few-shot prompting, on the other hand, involves providing the model with a few examples or context to help it understand the task better before asking it to generate a response.
"""

#Write a python program to find minimum of 3 numbers without using builtin function.
# Eg:- Input: 3, 1, 2 Output: 1
# Input: -1, -2, -3 Output: -3
# Input: 0, 0, 0 Output: 0
def find_minimum(a, b, c):
    if a <= b and a <= c:
        return a
    elif b <= a and b <= c:
        return b
    else:
        return c
input1 = (3, 1, 2)
input2 = (-1, -2, -3)
input3 = (0, 0, 0)
print("Minimum of {} is: {}".format(input1, find_minimum(*input1)))
print("Minimum of {} is: {}".format(input2, find_minimum(*input2)))
print("Minimum of {} is: {}".format(input3, find_minimum(*input3)))
