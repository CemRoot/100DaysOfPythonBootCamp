with open("file1.txt") as fd:
    file_data = fd.readlines()
with open("file2.txt") as fd2:
    file_data2 = fd2.readlines()

result  = [int(num) for num in file_data if num in file_data2]

# Write your code above 👆

print(result)


