class Queens():
    def __init__(self,boardSize,count,board):
        '''
        Objective: To initialize data members of object of type
        Queens
        Input Parameters:
           self (implicit parameter)- object of type Queens
           boardSize, board,board - numeric
        Return Value: None
        '''
        self.boardSize = boardSize
        self.count = count
        self.board = board

    def getBoardSize(self):
        '''
        Objective: To return the value of the board size
        '''
        return self.boardSize

    def __str__(self):
        '''
        Objective: To return string representation of object of
        type Queens
        Input Parameter: self (implicit parameter)- object of
        type Queens
        Return Value: string
        '''
        return 'Board Size: ' + str(self.boardSize) + ', Count: ' +
        str(self.count)+ ', Board: ' + str(self.board) +'\n'

    def unguarded(self,col):
        if 


    '''
    def add(self, col):

    def remove(self, col):

    def isSolved(self):

    def solveFrom(configuration):

    def nQueens():
        
