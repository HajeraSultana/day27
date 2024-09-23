import random, os, time
def name():
  name = input("Name your Legend: ")
  return name

def type():
  type = input("Character Type (Human, Elf, Wizard, Orc): ")
  return type

def health():
  health = ((random.randint(1,6) * random.randint(1,12)) / 2) + 10
  return health

def strength():
  strength = ((random.randint(1,6) * random.randint(1,12)) /2) + 12
  return strength
while True:
  print("Character Builder\033[34m")
  print()
  print(name())
  print("HEALTH:", health())
  print("STRENGTH:", strength())
  time.sleep(3)
  os.system("clear")
  again = input("\033[0mDo you want to build another character? ")
  if again == "yes":
    time.sleep(1)
    os.system("clear")
    continue
  else:
    time.sleep(1)
    os.system("clear")
    print("Thanks for playing!")
    break