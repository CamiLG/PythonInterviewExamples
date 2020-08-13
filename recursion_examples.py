"""Using recursion to implement power and factorial functions"""

def power(num, pwr):
    if pwr == 0:
        return 1
    else:
        return num * power (num, pwr -1)

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

#Examples of using these implementations

print(power(2, 3)) #should return eight

print(factorial(3)) #should return six