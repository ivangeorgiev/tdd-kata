'''
Get the first line from a file.

## Test Cases
- Can call readFromFile
- readFromFileReturns correct string
- readFromFile throws exception when file doesn't exist

'''
def readFromFile(filename):
    with open(filename, "r", encoding="utf8") as f:
        return f.readline()
