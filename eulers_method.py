"""Let function = f
    h = step length
    x, y = initial value of x and y respectively
    n = number of iteration
    ** = raise to power
    z = Anaylytical solution
    app_y_values = approximate y values
    
    Note:
    The Independent values in a function should be written in terms of x and y
    The power 
"""
 

from math import *
#import pandas as pd

x = float(input("Enter initial value of x: "))
n = int(input("Enter number of iteration: "))
h = float(input("Enter number of step lenght 'h': "))
f = input('Enter function: ')
y = float(input("Enter initial value of y: "))
z = input("Enter the analytical solution: ")


#Generating values for x
x_values = []
for i in range(0, n):
    x = x + h
    x_values.append(x)
print(x_values)


#Generating approximate values for y
app_y_values = []
x = str(x)
y = str(y)
if x or y in f:
    f = f.replace("x", x)
    f = f.replace("y", y)
    f = float(eval(f))
    for i in x_values:
        y = float(y) + h * f
        app_y_values.append(y)
    print(app_y_values)
else:
    print('Enter dependent variable with respect to y and the dependent variable with respect to x.')


#Generating exact values for y
exact_y_values = []
if x in z:
    z = z.replace("x", x)
    for i in range(x_values):
        z = z.replace(x, i)
        y = float(y) + h * eval(z)
        exact_y_values.append(y)
    print(exact_y_values)


#Absolute error and relative error percentage
Absolute_error = []
Relative_error_percentage = []
for i,j in exact_y_values and app_y_values:
    absolute_error = i - j
    relative_error = absolute_error / i
    relative_error_percentage = relative_error * 100
    Absolute_error.append(absolute_error)
    Relative_error_percentage.append(relative_error_percentage)
print(Absolute_error)
print(Relative_error_percentage)

"""d = {'y exact': exact_y_values, 
     'y approximate': app_y_values, 
     'Absolute Error': Absolute_error, 
     'Relative Error %': Relative_error_percentage }
pd.DataFrame(data = d)"""