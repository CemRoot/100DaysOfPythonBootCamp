# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
age_as_int = int(age)

years_remaining = 90 - age_as_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
month_remaining = years_remaining * 12

print(f"You have {days_remaining} days, {weeks_remaining} weeks, and {month_remaining} months left.")

######## OR ############
"""
max_Day = 90 * 365
max_Week = 90 * 52
max_Month = 90 * 12 

your_Day = age_as_int * 365
your_Week = age_as_int * 52
your_Month = age_as_int * 12

remains_Day = max_Day - your_Day
remains_Week = max_Week - your_Week
remains_Month = max_Month - your_Month

print(f"You have {remains_Day} days, {remains_Week} weeks, and {remains_Month} months left.")
"""

