# Question 1:
# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.
def divisible_seven_five():
    divisible = [str(n) for n in range(2000, 3201) if n % 7 == 0 and n % 5 != 0]
    print(','.join(divisible))


# Question 2:
# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
from math import factorial

def factorial_assign():
    print("From which number you wish to learn the factorial?:")
    n = int(input())
    print(factorial(n))


# Question 3:
# With a given integral number n, write a program to generate a dictionary that contains (i, i*i)
# such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
def squared_up():
    print("Tell me the number up to which you wish to output squares:")
    number = int(input())
    numbers_dict = dict()
    for n in range(1, number+1):
        numbers_dict[n] = n*n
    print(numbers_dict)


# Question 4:
# Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
def list_and_tuple():
    print("Give me a sequence of numbers separated by commas(no spaces):")
    sequence = input()
    splitted = sequence.split(",")
    print(splitted)
    print(tuple(splitted))


# Question 5:
# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.
class Stringer:
    def __init__(self):
        self.phrase = ""

    def getString(self):
        print("Feed me a string:")
        self.phrase = input()

    def printString(self):
        print(self.phrase.upper())


# Question 6:
# Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed all_evens of C and H:
# C is 50. H is 30.
# D is the variable whose all_evens should be input to your program in a comma-separated sequence.
from math import sqrt

def crazy_formula():
    print("Give me a number or a list of them, sepparated by commas:")
    items = [x for x in input().split(',')]
    c = 50
    h = 30
    result = []
    for d in items:
        result.append(str(int(round(sqrt(2*c*float(d)/h)))))
    print(','.join(result))


# Question 7:
# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. 
# The element value in the i-th row and j-th column of the array should be i*j.
# Note: i=0,1.., X-1; j=0,1,¡­Y-1.
def create_array():
    print("Input two numbers to create a two dimensional array")
    input_str = input()
    dimensions=[int(x) for x in input_str.split(',')]
    rowNum = dimensions[0]
    colNum = dimensions[1]
    array = [[0 for col in range(colNum)] for row in range(rowNum)]

    for row in range(rowNum):
        for col in range(colNum):
            array[row][col] = row*col
    return array


# Question 8:
# Write a program that accepts a comma separated sequence of words as input and prints 
# the words in a comma-separated sequence after sorting them alphabetically.
def sort_string():
    print("Which words do you want me to sort?:")
    words = [word for word in input().split(',')]
    words.sort()
    print(','.join(words))


# Question 9:
# Write a program that accepts sequence of lines as input and 
# prints the lines after making all characters in the sentence capitalized.
def capitalizer():
    lines = []
    while True:
        s = input()
        if s:
            lines.append(s.upper())
        else:
            break
    for line in lines:
        print(line)


# Question 10:
# Write a program that accepts a sequence of whitespace separated words as input and 
# prints the words after removing all duplicate words and sorting them alphanumerically.
def sorter_vol2():
    print("Give me a sequence of words separated by whitespace:")
    sequence = input()
    words = [word for word in sequence.split(" ")]
    print(" ".join(sorted(list(set(words)))))


# Question 11:
# Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether 
# they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
def binary_five():
    print("Input four binary numbers:")
    divisible_list = []
    binary_list =  [x for x in input().split(",")]
    for num in binary_list:
        if int(num, 2) % 5 == 0:
            divisible_list.append(num)
    print(",".join(divisible_list))


# Question 12:
# Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on a single line.
def even_range():
    all_evens = []
    for num in range(1000, 3001):
        s = str(num)
        if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
            all_evens.append(s)
    print(",".join(all_evens))


# Question 13:
# Write a program that accepts a sentence and calculate the number of letters and digits.
def count_chars():
    print("Write a sentence with letters and digits:")
    sentence = input()
    digit_count = sum(c.isdigit() for c in sentence)
    str_count = sum(c.isalpha() for c in sentence)
    print(f"Letter count: {str_count}\nDigit count: {digit_count}")

# Question 14:
# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
def upper_lower_count():
    print("Write a sentence with uppercase and lowercase letters:")
    sentence = input()
    upper_count = sum(c.isupper() for c in sentence)
    lower_count = sum(c.islower() for c in sentence)
    print(f"Uppercase count: {upper_count}\nLowercase count: {lower_count}")


# Question 15:
# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
def sum_myself():
    print("Pick a number between 1 and 9:")
    user_num = input()
    num = int(user_num)
    num2 = int(user_num * 2)
    num3 = int(user_num * 3)
    num4 = int(user_num * 4)
    result = num + num2 + num3 + num4
    print(result)


# Question 16:
# Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
def only_odds():
    print("Give me a list of numbers separated by commas:")
    sequence = input()
    odds = [x for x in sequence.split(',') if int(x) % 2 != 0]
    print(",".join(odds))


# Question 17:
# Write a program that computes the net amount of a bank account based a transaction log from console input. 
# The transaction log format is shown as following (D being deposit and W, withdrawal):
# D 100
# W 200
# In the above case, the output should be: -100
def bank_account():
    print("Input the amount, preceded of 'D' for deposits and 'W' for withdrawals:")
    ops = input()
    netAmount = 0
    while True:
        ops = input()
        if not ops:
            break
        else:
            values = ops.split(" ")
            operation = values[0]
            amount = int(values[1])
            if operation == "D":
                netAmount += amount
            elif operation == "W":
                netAmount -= amount
            else:
                pass
    print(f"The amount in your account is: {netAmount}")


# Question 18:
# Write a program to check the validity of password input by users.
# Following are the criteria for checking the password:
# 1. At least 1 letter between [a-z]
# 2. At least 1 number between [0-9]
# 1. At least 1 letter between [A-Z]
# 3. At least 1 character from [$#@]
# 4. Minimum length of transaction password: 6
# 5. Maximum length of transaction password: 12
# Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. 
# Passwords that match the criteria are to be printed, each separated by a comma.
import re

def valid_password():
    print("Write a few passwords separated by comms and I'll check if they're valid:")
    passwords = input().split(",")
    result = [password for password in passwords if re.search("[a-z]", password) and re.search("[0-9]", password)\
            and re.search("[A-Z]", password) and re.search("[$#@]", password) and not re.search("[\s]", password)]
    print("\nValid passwords:")
    print(','.join(result))
