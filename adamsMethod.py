"""
Let:
f = function
f_0 = function of x-initial and y-initial
f_1 = function of x_1 and y_1
y_predictor = y obtained from explicit computation
y_corrector = y obtained from implicit computation
h = step-length
n = number iterations

"""

class PredictorCorrector:
    def predictorCorrector_2_step(self, n, y_0, f_0, h = 0.1, x = 0):
        f_0 = x + y_0

        y_1 = y_0 + (h*f_0)

        f_1 = 0

        y_predictor = 0
        y_corrector = 0
        count = 1

        print(f"""\nUsing the 2 step predictor corrector method
        Given:
        h = {h} \t n = {n} \t y-initial = {y_0} \t x-initial = {y_0} \t 
        f(x) = {f_0}
        """)

        print(f"f-zero = {f_0} \t f-one = {f_1} \t  \n")

        print("S/n \t y-predictor \t\t\t y-corrector \t\t x-values")
        print(f"{count} \t {y_1} \t\t\t\t ------- \t\t {x}")

        x = x + h
        f_1 = x + y_1

        for i in range(0, n):
            y_predictor = y_1 + (h/2)*((3*f_1) - f_0)
            f_2 = x  + y_predictor
            y_corrector = y_1 + (h/12)*(5*f_2 + 8*f_1 - f_0)

            f_1 = f_2
            y_1 = y_corrector
            x = x +  h
            count = count + 1
            print(f"{count} \t {y_predictor} \t {y_corrector} \t\t{x}")



    def predictorCorrector_3_step(self, n, f, y_0, x = 0, h = 0.1):
        f_0 = -(y_0)
        y_1 = y_0 + (h*f_0)
        y_2 = y_1 + (h*f_0)
        f_1 = -(y_1)
        f_2 = -(y_2)
        f_3 = 0
        y_predictor = 0
        y_corrector = 0
        count = 0
        print(f"""Using the predictor corrector method for a 3 step problem
        Given:
        h = {h} \t n = {n} \t x-initial = {x} \t y-initial = {y_0} \t 
        f(x) = {f}
        """)

        print(f"f-zero ={f_0} \t f-one = {f_1} \t f-two = {f_2} \n")
        print("S/n \t y-predictor \t\t\t y-corrector \t\t x-values")
        print(f"{count} \t {y_1} \t\t\t\t ------ \t\t {x}")
        for i in range(0, n):
            y_predictor = y_2 + (h/12)*((23*f_2) - (16*f_1) +(8*f_0))
            f_3 = -(y_predictor)
            y_corrector = (1/17)*((9*y_2) + (9*y_1) - y_0) + ((6*h)/17)*(f_3 + 3*f_2)

            f_0 = f_1
            f_1 = f_2

            y_0 = y_1
            y_1 = y_2
            y_2 = y_corrector
            x = x +  h
            count = count + 1
            print(f"{count} \t {y_predictor} \t  {y_corrector} \t\t {x} ")


class AdamsMethod:
    def implicit_2(self, f_0, y_0, n, x = 0, h = 0.1 ):
        f_0 = -(y_0)

        y_1 = y_0 + (h*f_0)


        f_1 = -(y_1)

        y_2 = y_1 + (h*f_1)

        f_2 = -(y_2)


        count = 2
        print(f"""\n Using the implicit method for a 2 step problem
        Given:
        h = {h} \t n = {n} \t x-initial = {x} \t y-initial = {y_0} \t 
        f(x) = {f_0}
        """)

        print(f"f-zero ={f_0} \t f-one = {f_1} \t")
        print("S/n \t y \t\t\t x ")
        print(f"{count} \t {y_1} \t\t\t {x}")

        for i in range(0, n):
            
            y_2 = y_1 + (h/12)*(5*f_2 + 8*f_1 - f_0)
            f_2 = -(y_2)
            
            f_0 = f_1
            f_1 = f_2

            y_0 = y_1
            y_1 = y_2

            x = x +  h
            count = count + 1
            print(f"{count} \t {y_2} \t {x}")



    def implicit_3(self, f_0, y_0, n, x = 0, h = 0.1, ):
        f_0 = -(y_0)

        y_1 = y_0 + (h*f_0)

        f_1 = -(y_1)

        y_2 = y_1 + (h*f_1)

        f_2 = -(y_2)
        f_3 = 0

        count = 0
        print(f"""\nUsing the implicit method for a 3 step problem
        Given:
        h = {h} \t n = {n} \t x-initial = {x} \t y-initial = {y_0} \t 
        f(x) = {f_0}
        """)

        print(f"f-zero ={f_0} \t f-one = {f_1} \t f-two = {f_2} \n")
        print("S/n \t y \t\t\t x-values ")
        print(f"{count} \t {y_1} \t\t\t {x}")
        x = x + h
        count = count + 1
        print(f"{count} \t {y_2} \t\t {x}")


        for i in range(0, n):
            
            y_3 = (1/17)*((9*y_2) + (9*y_1) - y_0) + (h/17)*((6/17)*f_3 + (18/17)*f_2)
            f_3 = -(y_3)
            
            f_0 = f_1
            f_1 = f_2
            f_2 = f_3

            y_0 = y_1
            y_1 = y_2
            y_2 = y_3
            x = x +  h
            count = count + 1
            print(f"{count} \t {y_3} \t {x}")



    def explicit_2(self, f_0, y_0, n, x = 0, h = 0.1):
        y_1 = y_0 + (h*f_0)

        f_1 = -(y_1)
        print(f"f 1 = {f_1}")


        count = 1
        print(f"""\n Using the explicit method for a 2 step problem
        Given:
        h = {h} \t n = {n} \t x-initial = {x} \t y-initial = {y_0} \t 
        f(x) = {f_0}
        """)

        x = x + h
        
        print(f"f-zero ={f_0} \t f-one = {f_1} \t")
        print("S/n \t y \t\t\t x ")
        print(f"{count} \t {y_1} \t\t\t {x}")
        for i in range(0, n):
            
            y_2 = y_1 + (h/2)*(3*f_1 - f_0)
            f_2 = -(y_2)
            
            f_0 = f_1
            f_1 = f_2

            y_0 = y_1
            y_1 = y_2

            x = x +  h
            count = count + 1
            print(f"{count} \t {y_2} \t {x}")



    def explicit_3(self, f_0, y_0, n, x = 0, h = 0.1):
        #Explicit method
        #Using the Adams Bashforth method for the three step analysis
        print("\n Using Adams Bashforth 3 step method")
        #When h = 0.1
        h = 0.1
        x = 0
        y_0 = 1
        n = 50
        f_0 = -(y_0)
        y_1 = y_0 + (h*f_0)
        y_2 = y_1 + (h*f_0)
        f_1 = -(y_1)
        f_2 = -(y_2)
        f_3 = 0


        count = 1
        print(f"""
        Given:
        h = {h} \t n = {n} \t x-initial = {x} \t y-initial = {y_0} \t 
        f(x) = {f_0}
        """)

        print(f"f-zero ={f_0} \t f-one = {f_1} \t f-two = {f_2} \n")
        print("S/n \t y \t\t\t x ")
        print(f"{count} \t {y_1} \t\t\t {x} ")

        for i in range(0, n):
            y_3 = y_2 + (h/12)*((23*f_2) - (16*f_1) +(8*f_0))
            f_3 = -(y_3)

            f_0 = f_1
            f_1 = f_2
            f_2 = f_3

            y_0 = y_1
            y_1 = y_2
            y_2 = y_3
            x = x +  h
            count = count + 1
            print(f"{count} \t {y_3} \t {x}")
            


adamsMethod = AdamsMethod()
predictorCorrector = PredictorCorrector()


h = 0.1
x = 0
y_0 = 1
n = 50
while h >= 0.001:
    predictorCorrector.predictorCorrector_2_step(n, y_0,  x + y_0, h, x)

    predictorCorrector.predictorCorrector_3_step(n, x + y_0, y_0, x, h)

    adamsMethod.explicit_2(-(y_0), y_0, n, x, h)

    adamsMethod.explicit_3(-(y_0), y_0, n, x, h)

    adamsMethod.implicit_2(-(y_0), y_0, n, x, h)
    
    adamsMethod.implicit_3(-(y_0), y_0, n, x, h)

    h = h/10