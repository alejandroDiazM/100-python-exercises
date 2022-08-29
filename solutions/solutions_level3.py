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
