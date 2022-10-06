############DEBUGGING#####################

# # Describe Problem
# def my_function():
#   for i in range(1, 20): # there is a bug here its should be i in range(1, 21)
#     if i == 20:
#       print("You got it")
# my_function()

# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1,6) # There is a bug here its should be randint(1,5)
# print(dice_imgs[dice_num])

# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year > 1994: # there is a bug here its should be year >= 1994
#   print("You are a Gen Z.")

# # Fix the Errors
# age = input("How old are you?") #there is a bug when you input its will be str not int
# if age > 18:
# print("You can drive at age {age}.") # bug here ıts should be start f"blabla"

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: ")) # there is a bug here its should be word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

# #Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
# b_list.append(new_item) there is a bug here Indentation bug
#   print(b_list)
#
# mutate([1,2,3,5,8,13])