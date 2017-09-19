""" program to display e to the nth digit """

def loadfile():
    """ function to open the file e.txt and read the number e """
    efile = open("e.txt", "r")
    return efile.read()

def getn():
    """ get n from the user """
    num = int(input("How many digits do you want to display? "))
    if num < 1 or num > 6220:
        print("The number of digits needs to be between 1 and 6220.")
        exit()
    elif num > 1:
        num = num + 1
    return num

print(loadfile()[:getn()])
