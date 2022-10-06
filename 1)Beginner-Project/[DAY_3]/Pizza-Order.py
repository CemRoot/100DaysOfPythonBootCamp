# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bill = 0

if size == 'L':
  bill = 25
  #print("Large Pizza: $25")
elif size == 'M':
  bill = 20
  #print("Medium Pizza: $20")
elif size == 'S':
  bill = 15
  #print("Small Pizza: $15")
  
if size == 'S' and add_pepperoni == 'Y':
  bill +=2
  #print("Pepperoni for small pizza: +$2")
elif size == 'M'  and add_pepperoni == 'Y':
  bill +=3
  #print("Pepperoni for large pizza: +$3")
else:
  pass

if extra_cheese == 'Y':
  bill +=1
  #print("Extra cheese for any size pizza: +$1")
else:
  pass
  
print(f"Your final bill is: ${bill}.")


