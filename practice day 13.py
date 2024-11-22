#creating class using init function 
class person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname,self.lastname)

x = person('Hafeez','Ahmad')
x.printname()
        