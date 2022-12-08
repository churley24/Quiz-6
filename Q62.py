#Camryn Hurley

class Ambulance:
    """Represents an ambulance

    attributes: priority, speed, capacity"""

object = Ambulance()

object.priority = 1
object.speed = 70
object.capacity = 1

import math

p = object.priority
s = object.speed
c = object.capacity

def controlled_velocity(p, s, c):
    v = -10(1 - p) + 2.37 (s/ 10)**3.98 + 30(c + 1.2)
    return v
