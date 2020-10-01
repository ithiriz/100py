class InputOutString(object):
    def __init__(self):
        self.i = ""

    def getString(self):
        self.i = input()

    def printString(self):
        print (self.i.upper())

make = InputOutString()
make.getString()
make.printString()
