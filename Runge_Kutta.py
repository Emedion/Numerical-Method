
print(
    """"
Given the following question
1. f(x) = y^2 - xy, x = 0, y = 0.4, x = 0 (0.2) 100
2. f(x) = 2x - y, x = 0, y = 1, x = 0 (0.2) 50

Note n = number of iteration, 
     h = step length
     x_k_1 = x of k1
     y_k_1 = y of k1
     x_k_2 = x of k2
     y_k_2 = y of k2
    """
)


#Using the Heun's method for question 1
y, x, h, n = 0.4, 0, 0.2, 500
print("Using Heun's method for question 1")
#y = y + (h/4) * (k_1 + 3 * k_2)
#k_1 = f(x, y), k_2 = f(x + (2*h)/3, y + (2*h)/3*k_1)

for i in range(0, n):
    k_1 = y*y  - x * y

    x_k_2 = x + (2*h)/3
    y_k_2 = y + ((2*h)/3) * k_1

    k_2 = (y_k_2)**2 - (x_k_2) * y_k_2

    y = y + (h/4) * (k_1 + 3 * k_2)
    #y = round(y, 4)
    x = x + 0.2
    #x = round(x, 4)
    print(f"y{i} = {y}, x{i} = {x}")



#Using the Heun's method for question 2
y, x, h, n = 1, 0, 0.2, 250

print("\n \nUsing Heun's method for question 2")
#y = y + c_1 * k_1 + c2 * k_2
#k_1 = f(x, y), k_2 = f(x + (2*h)/3, y + (2*h)/3*k_1)

for i in range(0, n):
    k_1 = (2*x) - y

    x_k_2 = x + (2*h)/3
    y_k_2 = y + ((2*h)/3) * k_1

    k_2 = (2 * x_k_2) - y_k_2

    y = y + (h/4) * (k_1 + 3 * k_2)

    x  = x + 0.2

    #y = round(y, 8)
    x = round(x, 8)
    print(f"y{i} = {y}, x{i} = {x}")


#Using modified Euler's method for question 1

y, x, h, n = 0.4, 0, 0.2, 500
iterate = 0
print("\n \nUsing modified Euler's method for question 1")
while iterate < n:
    k_1 = (y*y)  - (x * y)

    x_k_2 = x + h/2
    y_k_2 = y + (h/2) * k_1

    k_2 = (y_k_2**2) - (x_k_2 * y_k_2)

    y = y + (h * k_2)

    x = x + 0.2

    #y = round(y, 8)
    x = round(x, 8)

    iterate = iterate + 1
    print(f"y{iterate} = {y}, x{iterate} = {x}")


#Using modified Euler's method for question 2
y, x, h, n = 1, 0, 0.2, 250

iterate = 0
print("\n \nUsing modified Euler's method for question 2")
while iterate < n:
    k_1 = 2*x  - y

    x_k_2 = x + h/2
    y_k_2 = y + (h/2) * k_1

    k_2 = 2 * (x_k_2) - y_k_2

    y = y + (h * k_2)

    x = x + 0.2

    #y = round(y, 8)
    x = round(x, 8)
    iterate = iterate + 1
    #print(f"y{iterate} = {y}, x{iterate} = {x}")
    print(f"y{iterate} = {y}, x{iterate} = {x}")
    

#Using the four step method
y, x, h, n = 0.4, 0, 0.2, 500


print("\n \nAnswers for question 1")
print("Using the four step method")
for e in range(0, n):
    k_1 = y**2  - x * y

    x_k_2 = x + (h/2)
    y_k_2 = y + (h/2) * k_1

    k_2 = (y_k_2)**2 - (x_k_2) * y_k_2

    x_k_3 = x_k_2
    y_k_3 = y + ((h*k_2)/2) 

    k_3 = (y_k_3)**2 - x_k_3 * y_k_3

    x_k_4 = x + h
    y_k_4 = y + h * k_3

    k_4 = (y_k_4*y_k_4) - (x_k_4 * y_k_4)

    y = y + (h/6) * (k_1 + 2 * k_2 + 2 * k_3 + k_4)

    x  = x + 0.2

    #y = round(y, 8)
    x = round(x, 8)
    print(f"y{e} = {y}, x{e} = {x}")



#Using 4 step method for question 2
print("\n \n Answers to question two using 4-step method")



y, x, h, n = 1, 0, 0.2, 250
for r in range(0, n):
    k_1 = (2  * x) - y

    x_k_2 = x + (h/2)
    y_k_2 = y + (h/2) * k_1

    k_2 = (2 * x_k_2) - y_k_2

    x_k_3 = x_k_2
    y_k_3 = y + ((h*k_2)/2) 

    k_3 = (2 * x_k_3) - y_k_3

    x_k_4 = x + h
    y_k_4 = y + h * k_3

    k_4 = (2 * x_k_4) - y_k_4

    y = y + (h/6) * (k_1 + 2 * k_2 + 2 * k_3 + k_4)

    x  = x + 0.2
    print(f"y{r} = {y}, x{r} = {x}")
