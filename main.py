"""
input from the user for the number they want to start the countdown from (positive int)
countdown to 0
"""


import time


number = int(input('Give me a number...\t'))
while number >= 0:
    print(number)
    number = number - 1
    time.sleep(1)
