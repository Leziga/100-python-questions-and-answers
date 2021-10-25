'''
Question 5
Question:
Define a class which has at least two methods:

getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.

Hints:
Use init method to construct some parameters
'''


class GetPrintString:

    def __init__(self):
        self.name = ''

    def getString(self):
        self.string = input()

    def printString(self):
        print(self.string.upper())


test = GetPrintString()
test.getString()
test.printString()
