import math as m
import time as t


def square_with_delay(num, time):
    t.sleep(time/1000)
    return m.sqrt(num)
 

print(square_with_delay(25100, 2123))