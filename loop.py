#Print each fruit in a fruit list:

fruits = ["mango", "berry ", "cherry"]
for x in fruits:
  print(x)
#Loop through the letters in the word "banana":

for x in "sravani":
  print(x)
#Exit the loop when x is "banana":

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
#Exit the loop when x is "banana", but this time the break comes before the print:

fruits = ["apple", "banana", "berry"]
for x in fruits:
  if x == "apple":
    break
  print(x)
#you don't print banana:

fruits = ["mango", "banana", "apple"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
#Using the range() function:

for x in range(5):
  print(x)
#Using the start parameter:

for x in range(3, 7):
  print(x)
#Print all numbers from 0 to 5, and print a message when the loop has ended:

for x in range(6):
  print(x)
else:
  print("maximum in work!")
#Break the loop when x is 3, and see what happens with the else block:

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("mera nam kya!")
#Print each adjective for every fruit:

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

# we can use pass staement: 
    #for x in [0, 1, 2]:
  #pass


