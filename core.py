# This simple calculator calculates the sum, the difference, the quotient and the product of two integers.
def calculator(input1,input2):
    summe = input1+input2
    difference=input1-input2
    quotient=input1/input2
    product=input1*input2
    
    results = [summe,difference,quotient,product]
    return results


    # Print the calculated values to console:
    print("Folgende Werte wurden berechnet:"
    "\nSumme ={:6.2f}".format(summe),
    "\nDifferenz ={:6.2f}".format(difference),     
    "\nProdukt ={:6.2f}".format(product),
    "\nQuotient ={:6.2f}".format(quotient))
    
    
# This function check, whether a given value is a prime number or not.
def is_prime(zahl):
    if zahl>1:
       for value in range(2,zahl):
           if (zahl % value) == 0:
               print(zahl,"ist keine Primzahl")
               return False
               break
       else:
           print(zahl,"ist eine Primzahl")
           return True

    else:
        print(zahl,"ist keine Primzahl")
        return False


# This function calculates the sum of two fractions
def add_frac(zaehler1,nenner1,zaehler2,nenner2):
    bruch1=[zaehler1,nenner1]
    bruch2=[zaehler2,nenner2]

    
# Calculation of the common denominator
    neuerzaehler1=bruch1[0]*bruch2[1]
    hauptnenner = bruch1[1]*bruch2[1]
    neuerzaehler2=bruch2[0]*bruch1[1]

# Calculation of the sum:
    summe =[neuerzaehler1+neuerzaehler2,hauptnenner]
    return summe

