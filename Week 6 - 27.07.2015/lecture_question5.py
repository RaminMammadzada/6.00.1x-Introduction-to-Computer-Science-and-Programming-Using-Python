class Queue(object):
    
    def __init__(self):
        self.vals=[]
        
    def insert(self, e):
        """Assumes e is an integer and inserts e into self""" 
        self.vals.append(e)
            
    def remove(self):
        try:
            element=self.vals[0]
            self.vals.remove(self.vals[0])
            return element
        except:
            raise ValueError
        
    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'
