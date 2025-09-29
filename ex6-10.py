"""
Exercise 6: Tax and Tip
The program you create for this exercise will begin by reading the cost
of a meal ordered at a restaurant from the user.  Then your program will
compute the tax and tip for the meal.  Use your local tax rate when 
computing the amount of tax owing.  Compute the tip as 18 percent of  the 
meal amount (without tax).  The output from your program should include
both the tax and the tip.  Format the output so that all of the values
are displayed using two decimal places.  (17 lines)
"""

def taxAndTip():
    mealCost = input("how much was the cost? ")
    taxRate = input("how much is the tax rate (in a percentage) where you live? ")
    mealCost = float(mealCost)
    taxRate = float(taxRate)
    totalCost = mealCost + (mealCost * (taxRate / 100)) + (mealCost * 0.18)
    print("your meal will cost $ " + str(totalCost) + " with 18% tax")

taxAndTip()

"""
Exercise 7:  Sum of the First n Positive Integers
Write a program that reads a positive integer, n, from the user and 
then displays the sum of all the integers from 1 to n.  The sum of the 
first n positive integers can be computed using the formula:
sum = (n*(n+1))/2
(12 lines)
"""

def sum():
    num = float(input("choose a random number "))
    sum = (num*(num+1))/2
    print("the sum of all numbers from 1 to the number you inputted: " + str(sum))

sum()

"""
Exercise 8:  Widgets and Gizmos
An online retailer sells two products:   widgets and gizmos.  Each widget 
weighs 75 grams.  Each gizmo weighs 112 grams.  Write a program that reads
the number of gizmos in an order from the user.  Then your program should 
compute and display the total weight of the order.  (15 lines)

"""

def WidgetsGizmos():
    numGizmos = float(input("how many gizmos do you have? "))
    numWidgets = float(input("how many widgets do you have? "))
    weight = (numGizmos * 112) + (numWidgets * 75)
    print("you have " + str(weight) + " g of gizmos and widgets")

WidgetsGizmos()

"""
Exercise 9:  Compound Interest
Pretend that you have just opened a new savings account that earns 4 percent
interest per year.  The interest that you earn is paid at the end of the year, 
and is added to the balance of the savings account.  Write a program that begins
by reading the amount of money deposited into the account from the user.  Then 
your program should compute and display the amount in the savings account after
1, 2, and 3 years.  Display each amount so that it is rounded to 2 decimal 
places.  (19 lines)
"""

def compoundInterest():
    yearsT = float(input("how many years is the money in the bank? "))
    principalAmount = float(input("how much money do you have? "))
    totalAmount = principalAmount * ((1.0 + (0.04 / 1))**(1 * yearsT))
    print("after " + str(yearsT) + " years, you will have $" + str(round(float(totalAmount), 2)) + " in the bank")
    print("you originally have $" + str(round(principalAmount, 2)) + " in your bank account")

compoundInterest()

"""
Exercise 10:  Arithmetic
Create a program that reads two integers, a and b, from the user.  Your program
should compute and display:
- the sum of a and b
- the difference when b is subtracted from a
- the product of a and b
- the quotient when a is divided by b
- the remainder when a is divided by b
- the result of log10 a
- the result of a to the power of b

Hint:  you will probably find the log10 function in the math module helpful
for computing the second last item in the list.
"""
def arithmetic():
    import math
    int1 = float(input("input a number "))
    int2 = float(input("input a number "))
    print("the sum is " + str(int1 + int2))
    print("the difference is " + str(int1 - int2))
    print("the product is " + str(int1 * int2))
    print("the quotient is " + str(int1 / int2))
    print("the remainder is " + str(int1 % int2))
    print("the result of log10 of a is " + str(math.log10(int1)))
    print("the result of a to the power of b is " + str(int1 ** int2))

arithmetic()
