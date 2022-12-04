import random, os, time

def character_name():
  name = input("Name your legend: ")
  type = input("Character Type (Human, Elf, Wizard, Orc): ")
  return name, type
  
def rollDice(side):
  result = random.randint(1,side)
  return result
  
def health():
  health_stats = round(((rollDice(6) * rollDice(12))/2) + 10)
  return health_stats

def strength():
  strength_stats = ((rollDice(6) * rollDice(8))/2) + 12
  return strength_stats

while True:
  print("⚔️  Character Builder ⚔️")
  print()
  time.sleep(1)
  character, type = character_name()
  health_stats = health()
  strength_stats = strength()
  print()
  print(f"{character}")
  time.sleep(1)
  print(f"TYPE: {type}")
  print(f"HEALTH: {health_stats}")
  print(f"STRENGTH: {strength_stats}")
  print()
  time.sleep(1)
  new_character = input("Generate another character? y or n: ")
  if new_character.lower() == 'y':
    os.system("clear")
    continue
  else:
    break
print()
print("Thanks for playing! See you next time.")