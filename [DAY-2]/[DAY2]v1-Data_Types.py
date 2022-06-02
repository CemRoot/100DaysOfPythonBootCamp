# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ") #39
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

str_one = two_digit_number[0] #3 str() 
str_two = two_digit_number[1] #9 str()
num_one = int(str_one)
num_two = int(str_two)
result = num_one+num_two
#print(num_one,"+",num_two,"=",result)
print(result)

########OR###############
""" 
first_digit = two_digit_number[0]
second_digit = two_digit_number[1]

result = int(first_digit) + int(second_digit)
print(result) 
"""