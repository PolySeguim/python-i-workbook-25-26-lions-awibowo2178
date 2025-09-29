
"""
Exercise 1:  Mailing Address
Create a program that displays your name and complete mailing 
address formatted in the manner that you would usually see it 
on the outside of an envelope.  Your program does not need to 
read any input from the user.  (9 lines)
"""

def address():
    name = input("what is your name? ")
    homeAddress = input("what is the first line of your address? ")
    cityStateZip = input("what is the second line of your address? ")
    print(name)
    print(homeAddress)
    print(cityStateZip)
address()

"""
Exercise 2:  Hello
Write a program that asks the user to enter his or her name.  
The program should respond with a message that says hello to 
the user, using his or her name.  (9 lines)
"""

def hello():
    name = input("what is your name? ")
    print("hello, " + name)

hello()

"""
Exercise 3:  Area of a Room
Write a program that asks the user to enter the width and 
length or a room.  Once the values have been read, your 
program should compute and display the area of the room.  
The length and the width will be entered as floating point 
numbers.  Include units in your prompt and output message;  
either feet or meters, depending on which unit you are more 
comfortable working with.  (13 lines)
"""
def area():
    roomWidth = input("what is the width of the room, in feet? ")
    roomLength = input("what is the length of the room, in feet? ")
    roomArea = float(roomWidth) * float(roomLength)
    print("the area of the room is " + str(roomArea) + " feet")

area()

"""
Exercise 4:  Area of a Field
Create a program that reads the length and width of a 
farmer’s field from the user in feet.  Display the 
area of the field in acres.  
Hint: There are 43,560 square feet in an acre
"""

def areaField():    
    fieldWidth = input("what is the width of the field, in feet? ")
    fieldLength = input("what is the length of the field, in feet? ")
    fieldArea = (float(fieldWidth) * float(fieldLength)) / 43560
    print("the area of the field is " + str(fieldArea) + " acres")

areaField()

"""
Exercise 5:  Bottle Deposits
In many jurisdictions a small deposit is added to drink 
containers to encourage people to recycle them.  In one 
particular jurisdiction, drink containers holding one liter 
or less have a $0.10 deposit, and drink containers holding 
more than one liter have $0.25 deposit.
Write a program that reads the number of containers of each 
size from the user.  Your program should continue by computing 
and displaying the refund that will be received for returning 
those containers.  Format the output so that it includes a dollar 
sign and always displays exactly two decimal places.  (15 lines)
"""

def calculateDeposit():
    smallBottles = float(input("how many drink containers do you have that are less than 1 liter? "))
    largeBottles = float(input("how many drink containers do you have that are more than 1 liter? "))
    deposit = (smallBottles * 0.10) + (largeBottles * 0.25)
    deposit = round(deposit, 2)
    print("Your refund will be: $", "{:.2f}".format(deposit))
calculateDeposit()

