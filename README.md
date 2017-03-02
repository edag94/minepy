# minepy
C++ school project rewritten in python

TNT det instead of void should return two ints, total rubble and count, instead of the “hack” of counting them as objects 
and passing them into the function. Primitive types (ints, floats, bools) are always passed by value into functions. 
Therefore just passing in an int will not get it to be modified by the function, hence why I passed in in as a list 
with one member. This is the better way to do it in python:

def RectToPolar(x, y):
    r = (x ** 2 + y ** 2) ** 0.5
    theta = math.atan2(y, x)
    return r, theta # return 2 things at once

r, theta = RectToPolar(3, 4) # assign 2 things at once

str.split() will split a string everytime it sees the string in the parathesis and will add it to a list

what failed:
need a way to update priorities when breaking invariant
need a way to compare by checking if tile was cleared

this can be done by writing my own pq with its own comp function, however I tried using the built in heapq function, 
but this didn’t work because the comparison predicate is more complicated then just comparing the elts in the tuples
