import os
import random
import pygame

def cls():
  os.system('cls' if os.name=='nt' else 'clear')

class pStats():
  def __init__(self, _name, _level, _atk, _def, _hp):
    self.Name = _name
    self.Level = _level
    self.Atk = _atk
    self.Def = _def
    self.HP = _hp

  Name = ""
  Level = 1
  Atk = 1
  Def = 1
  HP = 1

class Player(pStats):
  def __init__(self, _name, _gender):
    self.Gender = _gender
    pStats.__init__(self, _name, 1, 2 + self.Level, 1 + self.Level, 10 + self.Level)

  def printStats(self):
    print("Name:", self.Name)
    print("Gender:", self.Gender)
    print("Level:", self.Level)
    print("Atk:", self.Atk)
    print("Def:", self.Def)
    print("HP:", self.HP)

  Gender = "F"

class Enemy(pStats):
  def __init__(self, _name, _level, _atk, _def, _hp):
    pStats.__init__(self, _name, _level, _atk, _def, _hp)

  def printStats(self):
    print("Enemy Name:", self.Name)
    print("Enemy Level:", self.Level)

def main():
  # Clear Screen
  cls()

  # Input Name
  tempName = input("What is your name Adventurer: ")
  tempGender = ""

  # Input Gender with Check
  while(tempGender not in ["y", "n"]):
    tempGender = input("Small PP (y/n): ")

  if tempGender == "y":
    tempGender = "M"
  else:
    tempGender = "F"

  # Creation of Hero Object
  Hero = Player(tempName, tempGender)

  # Clear Screen
  cls()

  # Print Stats
  Hero.printStats()

  input("Press Enter to continue...")

  print("You Encountered a Goblin!")

  input("Press Enter to continue...")

  Goblin = Enemy("Goblin", random.randint(1, 2), random.randint(1, 4), random.randint(1, 3), random.randint(5, 10))

  cls()

  Goblin.printStats()


###################################
#.................................#
#........................A........#
#.................A...............#
#......A..........................#
#..............X..................#
#..A..............................#
#.................................#
###################################

# Calling Main Function
main()