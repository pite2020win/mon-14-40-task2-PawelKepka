#
#Flight simulator. 
#Write a code in python that simulates the tilt correction of the plane (angle between plane wings and earth). 
#The program should print out current orientation, and applied tilt correction.
# (Tilt is "Roll" in this diagram https://www.novatel.com/assets/Web-Phase-2-2012/Solution-Pages/AttitudePlane.png)
#The program should run in infinite loop, until user breaks the loop. 
#Assume that plane orientation in every new simulation step is changing with random angle with gaussian distribution (the planes is experiencing "turbuence"). 
# Hint: "random.gauss(0, 2*rate_of_correction)"
#With every simulation step the orentation should be corrected, correction should be applied and printed out.
#Try to expand your implementation as best as you can. 
#Think of as many features as you can, and try implementing them.
#
#Try to expand your implementation as best as you can. 
#Think of as many features as you can, and try implementing them.
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.
#
#Your program must be runnable with command "python task.py".
#Show some usecases of your library in the code (print some things)
#Delete these comments before commit!
#
#Good luck.

import random
import time
from dataclasses import dataclass

@dataclass
class Airplane:
  name: str
  wingsAngle: float

  def __init__ (self, name):
    self.name = name
    self.wingsAngle = 0.0

  def changeWingsAngle(self, angle):
    self.wingsAngle += angle



if __name__ == "__main__":
  airplane = Airplane("First airplane")
  i = 1
  while 1:
    rate_of_correction = 1
    angle = random.gauss(0, 2*rate_of_correction)
    airplane.changeWingsAngle(angle)
    print(airplane.wingsAngle)
    time.sleep(0.1)
    if airplane.wingsAngle > 180:
      print("upside down!")

    #no time for user input 
    i = i + 1
    if i > 20:
      break
    
    

