# #FileNotFound
#
# try:
# 	file = open("a_test.txt")
# 	a_dict = {"key": "value"}
# 	print(a_dict["key"])
# except FileNotFoundError:
# 	file = open("a_test.txt","w")
# 	file.write("Except Block Worked")
# except KeyError as error:
# 	print(f"The key {error} is not exist")
# else:
# 	content = file.read()
# 	print(content)
# finally:
# 	file.close()
# 	print("File Closed")

h = float(input("Height: "))
w = float(input("Weight: "))
if h > 3:
	raise   ValueError("Height is too high")
bmi = w / (h ** 2)
print(f"BMI: {bmi}")