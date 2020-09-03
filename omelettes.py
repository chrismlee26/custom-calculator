print("Welcome to the delicious omelette calculator")
name = input("What's your name? ")
print("It doesn't matter, " + name)

omelette_type = input("French? or American Omelette? ")

#if ({omelette_type} = "american"):
#omelette_type = input("Nobody likes American Omelettes try again ")
## french omelette proceeds !while loop!
    ## "Ok, how many eggs?"
#if french then howmany_eggs, if American, go back up one level.
## american omelette says "wrong choice" and goes back to asking

howmany_eggs = input("Ok, 2 or 3 or 4 eggs? ")
print(f"Ok calculating for {howmany_eggs} eggs")

#pan_size = int(howmany_eggs) * 3

def pan_egg_ratio(howmany_eggs, pan_size):
  pan_size = 0
  if int(howmany_eggs) == "2":
    return pan_size == "6"
  elif int(howmany_eggs) == "3":
    return pan_size == "8-10"
  elif int(howmany_eggs) == "4":
    return pan_size == "12"
 



howmuch_butter = int(howmany_eggs)*.5

print(f"Ok so {omelette_type} omelette and {howmany_eggs} eggs. Here's your receipe")

print("1. Whisk eggs completely.")

print(f"2. Grab a {pan_size}\" pan, {howmany_eggs} eggs and {howmuch_butter} tablespoons of butter. On medium heat, place butter until melted and slightly frothy. Pour in the {howmany_eggs} whisked eggs and turn the heat to low.")

print("3. Stir into a circular pattern until eggs begin to form. Continually lift sides of eggs and shake the pan for allow uncooked eggs and butter to form under the egg that has already set.")

print(f"4. Once 60-70% formed, add salt and fold the {omelette_type} omelette into thirds.")

print(f"5. Place {omelette_type} omelette onto plate, seam side down. Brush surface with more butter and dust with salt if desired.")


##calculator needs 2 eggs for 6"-8" pan, 3 eggs 10", 4 eggs 12"
##larger than 12" this it makes some joke about a scramble
##5" below it makes some joke about pan too small


