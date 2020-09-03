print("Welcome to the delicious omelette calculator")
name = input("What's your name? ")
print("It doesn't matter, " + name)

omelette_type = input("French? or American Omelette? ")

def pan_egg_ratio(num_eggs):
  pan_size = 0
  if int(num_eggs) == 2:
    pan_size = 6
  elif int(num_eggs) == 3:
    pan_size = 8
  elif int(num_eggs) == 4:
    pan_size = 12
  return pan_size

#pan_size = int(num_eggs) * 3    <---- backup code for failed function above

while omelette_type != "french":
 omelette_type = input("Nobody likes American omelettes try \"french\" ")

num_eggs = input("Ok, 2 or 3 or 4 eggs? ")
print(f"Ok calculating for {num_eggs} eggs")

pan_size = pan_egg_ratio(num_eggs)

num_butter = int(num_eggs)*.5

print(f"Ok so {omelette_type} omelette and {num_eggs} eggs. Here's your receipe")

print("1. Whisk eggs completely.")

print(f"2. Grab a {pan_size}\" pan, eggs and {num_butter} tablespoons of butter. On medium heat, place butter until melted and slightly frothy. Pour in the {num_eggs} whisked eggs and turn the heat to low.")

print("3. Stir into a circular pattern until eggs begin to form. Continually lift sides of eggs and shake the pan for allow uncooked eggs and butter to form under the egg that has already set.")

print(f"4. Once 60-70% formed, add salt and fold the {omelette_type} omelette into thirds.")

print(f"5. Place {omelette_type} omelette onto plate, seam side down. Brush surface with more butter and dust with salt if desired.")





