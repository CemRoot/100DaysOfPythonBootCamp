"""
/<path> means start at the project root folder

./<path> means start at the current folder (in Python you can omit the ./)

../<path> means start at the parent folder of the current folder

<drive-letter>:/<path> means start at the drive root folder

The first three are called relative paths, because they are relative to the current file or project folder.

The last is called an absolute path, because it specifies the drive and path completely.
"""
with open("You should write your directory C/: bla bla") as file:
	contents = file.read()
	print(contents)
