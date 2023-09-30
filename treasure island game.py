
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload



direction= input("You're at a cross road. Where do you wanna go? Type 'left' or 'right'.\n").lower()

if direction == "left":
  swim_wait=input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.\n").lower()
  if swim_wait =="wait":
    doors=input("You arrive at the island unharmed. There is a house with three doors. One red, one yellow, and one blue. Which color do you choose?.\n").lower()
    if doors== "red":
      print("Burned by fire. Game over.")
    elif doors=="yellow":
      print("You win!")
    elif doors=="blue":
      print("Eaten by beasts. Game over.")
    else:
      print("Game Over.")
  elif swim_wait== "swim":
    print("Attacked by trout. Game over.")
  else:
    print("Attacked by trout. Game Over")
elif direction=="right":
  print("Fall into a hole. Game over.")
else:
  print("Fall into a hole. Game over.")

