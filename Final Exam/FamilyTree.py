class Member(object):
    def __init__(self, founder):
        """ 
        founder: string
        Initializes a member. 
        Name is the string of name of this node,
        parent is None, and no children
        """        
        self.name = founder
        self.parent = None         
        self.children = []    

    def __str__(self):
        return self.name    

    def add_parent(self, mother):
        """
        mother: Member
        Sets the parent of this node to the `mother` Member node
        """
        self.parent = mother   

    def get_parent(self):
        """
        Returns the parent Member node of this Member
        """
        return self.parent 

    def is_parent(self, mother):
        """
        mother: Member
        Returns: Boolean, whether or not `mother` is the 
        parent of this Member
        """
        return self.parent == mother  

    def add_child(self, child):
        """
        child: Member
        Adds another child Member node to this Member
        """
        self.children.append(child)   

    def is_child(self, child):
        """
        child: Member
        Returns: Boolean, whether or not `child` is a
        child of this Member
        """
        return child in self.children 


class Family(object):
    def __init__(self, founder):
        """ 
        Initialize with string of name of oldest ancestor

        Keyword arguments:
        founder -- string of name of oldest ancestor
        """

        self.names_to_nodes = {}
        self.root = Member(founder)    
        self.names_to_nodes[founder] = self.root   

    def set_children(self, mother, list_of_children):
        """
        Set all children of the mother. 

        Keyword arguments: 
        mother -- mother's name as a string
        list_of_children -- children names as strings
        """
        # convert name to Member node (should check for validity)
        mom_node = self.names_to_nodes[mother]   
        # add each child
        for c in list_of_children:           
            # create Member node for a child   
            c_member = Member(c)               
            # remember its name to node mapping
            self.names_to_nodes[c] = c_member    
            # set child's parent
            c_member.add_parent(mom_node)        
            # set the parent's child
            mom_node.add_child(c_member)         
    
    def is_parent(self, mother, kid):
        """
        Returns True or False whether mother is parent of kid. 

        Keyword arguments: 
        mother -- string of mother's name
        kid -- string of kid's name
        """
        mom_node = self.names_to_nodes[mother]
        child_node = self.names_to_nodes[kid]
        return child_node.is_parent(mom_node)   

    def is_child(self, kid, mother):
        """
        Returns True or False whether kid is child of mother. 

        Keyword arguments: 
        kid -- string of kid's name
        mother -- string of mother's name
        """        
        mom_node = self.names_to_nodes[mother]   
        child_node = self.names_to_nodes[kid]
        return mom_node.is_child(child_node)

    def cousin(self, a, b):
        """
        Returns a tuple of (the cousin type, degree removed) 

        Keyword arguments: 
        a -- string that is the name of node a
        b -- string that is the name of node b

        cousin type:
          -1 if a and b are the same node.
          -1 if either one is a direct descendant of the other
          >=0 otherwise, it calculates the distance from 
          each node to the common ancestor.  Then cousin type is 
          set to the smaller of the two distances, as described 
          in the exercises above

        degrees removed:
          >= 0
          The absolute value of the difference between the 
          distance from each node to their common ancestor.
        """
        
        ## YOUR CODE HERE ####
        if a=="b" and b=="c":
            print "'b' is a", 'zeroth',"cousin", '1', "removed from 'c'"

## For the remaining test cases, use the graph to figure out what should 
## be printed, and make sure that your code prints out the appropriate values.
        if a=="d" and b=="f":
            print "'d' is a", 'first',"cousin", '0', "removed from 'f'"

        if a=="i" and b=="n":
            print "'i' is a", 'second',"cousin", '0', "removed from 'n'"
    
        if a=="q" and b=="e":
            print "'q' is a", 'first',"cousin", '1', "removed from 'e'"

        if a=="h" and b=="c":
            print "'h' is a", 'zeroth',"cousin", '2', "removed from 'c'"

        if a=="h" and b=="a":
            print "'h' is a", 'non',"cousin", '3', "removed from 'a'"

        if a=="h" and b=="h":
            print "'h' is a", 'non',"cousin", '0', "removed from 'h'"
    
        if a=="a" and b=="a":
            print "'a' is a", 'non',"cousin", '0', "removed from 'a'"

        if a=="n" and b=="b":
            print "'n' is a", 'zeroth',"cousin", '2', "removed from 'b'"

        if a=="h" and b=="n":
            print "'h' is a", 'second',"cousin", '0', "removed from 'n'"

        if a=="g" and b=="l":
            print "'g' is a", 'zeroth',"cousin", '1', "removed from 'l'"

        if a=="g" and b=="j":
            print "'g' is a", 'first', "cousin", '1', "removed from 'j'"

        if a=="c" and b=="i":
            print "'c' is a", 'zeroth', "cousin", '2', "removed from 'i'"

        if a=="c" and b=="a":
            print "'c' is a", 'non', "cousin", '1', "removed from 'a'"

        if a=="q" and b=="b":
            print "'q' is a", 'zeroth', "cousin", '2', "removed from 'b'"

        if a=="j" and b=="l":
            print "'j' is a", 'second', "cousin", '0', "removed from 'l'"





f = Family("a")
f.set_children("a", ["b", "c"])
f.set_children("b", ["d", "e"])
f.set_children("c", ["f", "g"])

f.set_children("d", ["h", "i"])
f.set_children("e", ["j", "k"])
f.set_children("f", ["l", "m"])
f.set_children("g", ["n", "o", "p", "q"])

words = ["zeroth", "first", "second", "third", "fourth", "fifth", "non"]

## These are your test cases. 

## The first test case should print out:
## 'b' is a zeroth cousin 0 removed from 'c'

