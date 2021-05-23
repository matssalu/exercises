import sys

with open(sys.argv[1], "r") as file1:
    with open(sys.argv[2], "w") as file2:
        file2.write(file1.read())
