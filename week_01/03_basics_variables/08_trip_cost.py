'''
Receive the following arguments from the user:
    - miles to drive
    - MPG of the car
    - Price per gallon of fuel

Display the cost of the trip in the console.

'''

miles = float(input("How many miles will you be driving?"))
mpg = float(input("How many Miles per gallon do you get on average while driving?"))
fuel = float(input("How much does the price of a gallon of gas cost?"))


x = (float(miles * fuel * mpg))
print("The total cost of your trip would be ", x)