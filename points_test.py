import math
import time, threading

"""
def tot_points(guess, views):
    points = 0
    x = 0.0
    percent = 0.0
    raw_percent=0.0
    #if guess > 10*views or guess < views/10, no points are allowed
    raw_percent = (1.0 - abs(math.log10(guess/views)))
    if raw_percent < 0:
        raw_percent = 0
    #with x we account for the fact that guessing small numbers is harder than guessing big numbers
    x = 3.5*math.log10(100000000.0/views)
    percent = raw_percent + x/100
    points = int(round(1000*(percent)))
    return points
"""

def tot_points(guess, views):
    points = 0
    percent = 0.0
    base = 0.0
    #this accounts for the fact that guessing small numbers is harder than guessing large numbers
    #future development: find a polynomial fit (ax^2+bx+c/dx^2+ex+f) so that threshold for small views is 50, 10 for largest
    base = 10 + 7*math.log10(1000000000000000/views)
    argument = 0.0
    if base > 60.0:
        base = 60.0
    elif base < 20.0:
        base = 20.0
    argument = guess/views
    percent = (1.0 - abs(math.log(argument,base)))
    if percent < 0:
        percent = 0
    points = int(round(1000*(percent)))
    return points



guess = raw_input("Guess? ")
guess = float(guess)
views = raw_input("Views? ")
views = float(views)


print "POINTS: ", tot_points(guess, views)
print "This video had actually ", int(views), "views!"

