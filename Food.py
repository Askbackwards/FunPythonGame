
"""You can add food in this class, and grab it from the food_list. Get it's fill amoung from getFill() and get the name from getName()"""


class Food( object ):
    
    def __init__( self, fill_amount=0, name='' ):
        """Creates a new food: Takes how much the food will fill you and what its name is"""
        
        self.__fill = fill_amount
        self.__name = name
        
    #--------------------------------------------------------------------------
    
    def __repr__( self ):
        """ Shows food as a string"""
        
        fill = str(self.__fill)
        temp = ("Fill Hunger = " + fill + " Name = " + self.__name)
        
        return temp
        
    #--------------------------------------------------------------------------
    
    def getName( self ):
        """return the name of the food"""
        return self.__name
        
    #--------------------------------------------------------------------------
    
    def getFill( self ):
        """return the fill amount of the food"""
        return self.__fill
        
        
#Food list
food_list = []
beans = Food(10, "Can of Beans")
soup = Food(5, "Soup")
ham = Food(20, "Ham")

food_list.append(beans)
food_list.append(soup)
food_list.append(ham)
    
