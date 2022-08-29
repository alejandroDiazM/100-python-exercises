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