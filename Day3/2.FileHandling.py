# Task no 1: Create a text file and write data into it.

file = open("file.txt", "w")
file.write("Hello, World!\n")
file.close()
print("Data written successfully.")


# Task no 2: Read and display file contents

file = open("file.txt", "r")

content = file.read()

print("File Contents:")
print(content)

file.close()

# Task no 3: # Append data to an existing file

file = open("file.txt", "a")

file.write("This line was added later.\n")
file.close()

print("Data appended")


# Task no 4: # Count the number of lines in a file

file = open("file.txt", "r")

lines = file.readlines()
print("Total number of lines in file.txt:", len(lines))
file.close()

