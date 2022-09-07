# database.py
print('This is the database.py module')
print(f"Python thinks this is called {__name__}")

#import blood_calculator
#import blood_calculator as bc
from blood_calculator import check 

#answer = blood_calculator.check(55)
answer = check(55)
print(f"The HDL of 55 is {answer}")

