class MITPerson(Person):
    nextIdNum=0 # next ID number to assign

    def __init__(self,name):
        Person.__init__(self,name) # initialize Person attributes
        # new MITPerson attribute: a unique ID nukber
        self.idNum=MITPerson.nextIdNum
        MITPerson.nextIdNum+=1

    def getIdNum(self)
        return self.idNum

    # sorting MIT people uses their ID number, not game!
    def __it__(self, other):
        return self.idNum<other.idNum
