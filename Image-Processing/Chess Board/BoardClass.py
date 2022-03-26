# Create the class Board , which has two attributes : a classified board that ’remembers ’
#the types of pieces that a square hold /held , and one unclassified board that only
# makes difference between the colors of the pieces .
#The class has three functions that updates the different boards in different regards .
class Board :

    def __init__ ( self ) :

    #The classified board . Initial values are the starting positions of the pieces ,
    #and as pieces are moved the squares will be updated using the functions below .
        self.C =[
            ["r", "n", "b", "q", "k", "b", "n", "r"],
            ["p", "p", "p", "p", "p", "p", "p", "p"],
            ["1", "1", "1", "1", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "1", "1", "1", "1"],
            ["P", "P", "P", "P", "P", "P", "P", "P"],
            ["R", "N", "B", "Q", "K", "B", "N", "R"]]
        
        self.UC=[
            ["1", "1", "1", "1", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "1", "1", "1", "1"]
        ]


    def firstUC(self) :
        self.UC=[
            ["B", "B", "B", "B", "B", "B", "B", "B"],
            ["B", "B", "B", "B", "B", "B", "B", "B"],
            ["1", "1", "1", "1", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "1", "1", "1", "1"],
            ["W", "W", "W", "W", "W", "W", "W", "W"],
            ["W", "W", "W", "W", "W", "W", "W", "W"],
        ]




        # Filling the squares with the colors occupying them .
    def updateUC ( self , NewRank , NewFile , Color ) :
        self.UC [ NewRank ][ NewFile ] = Color
        # Updating the classified board .
    def updateCBoard ( self , NewRank , NewFile , OldRank , OldFile ) :
        self.C [ NewRank ][ NewFile ] = self.C [ OldRank ][ OldFile ]
        self.C [ OldRank ][ OldFile ] = '1'