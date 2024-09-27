example1 = "Example1.txt"
file1 = open(example1, "r")

print(file1.name)
print(file1.mode)
print(file1.read())

print("-----------------------")

with open(example1, "r") as file1:
    FileContent = file1.read()
    print(FileContent)

with open(example1, "r") as file1:
    print(file1.read(4))

with open(example1, "r") as file1:
    print(file1.read(4))
    print(file1.read(4))
    print(file1.read(7))
    print(file1.read(15))

with open(example1, "r") as file1:
    print(file1.read(16))
    print(file1.read(5))
    print(file1.read(9))

with open(example1, "r") as file1:
    print("first line: " + file1.readline())

with open(example1, "r") as file1:
    print(file1.readline(20)) # does not read past the end of line
    print(file1.read(20)) # Returns the next 20 chars

# Iterate through the lines

with open(example1,"r") as file1:
        i = 0
        for line in file1:
            print("Iteration", str(i), ": ", line)
            i = i + 1

# Read all lines and save as a list

with open(example1, "r") as file1:
    FileasList = file1.readlines()


print(FileasList[0])
