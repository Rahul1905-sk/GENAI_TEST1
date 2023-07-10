## question 4


a. Write a Python program that takes a string input from the user and prints out the reversed string.  
For instance, if a user inputs: "Python is fun"

Expected output:

nuf si nohtyP

*


def reverse_string(str): 
    res = ""
    for char in str:
        res = char+res
    return res

print(reverse_string("Python is fun"))



### b. List of Dictionaries - Max Salary
*

def max_salary(employess):
for emp in employees: 
    max = {salary:0}
    if emp.salary > max.salary: 
        max = emp
return max


print(max_salary(employess))

