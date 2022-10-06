import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆
#Write your code below this line 👇
#Important: You are not allowed to use the choice() function.
            #random_name = random.choice(names)
random_name = len(names) #list olarak atamasını yaptı len list olarak çalışıyor.
rasgla = random.randint(0,random_name -1)
who_pay = names[rasgla]
print(f"{who_pay} is going to buy the meal today!")
  