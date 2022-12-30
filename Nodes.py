class Thing: # A class for Node related operations
    def __init__(self, currentState):
        self.Current = currentState
        self.CurrentScore = 0
        self.children = {}

    def Make(self, i, j, player): # Function for generating a child node
        self.children[(i, j)] = Thing(self.Current.Get_currentState())
        mul = 1
        if player:
            mul *= -1
        self.children[(i, j)].CurrentScore = (self.children[(i, j)].Current.action(i, j,player) * mul) + self.CurrentScore

    def Populate(self, i, j, Child): # Function for adding a node
        self.children[(i,j)] = Child

    def Draw(self,mat2): # function for drawing the board
        if mat2:
            self.Current.Draw_mat2()
            return
        self.Current.Draw_mat()
    
