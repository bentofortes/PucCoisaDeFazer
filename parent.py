##  IMPORTS  ##

import erro1
import enum

##  TYPEDEFS AND ENUMS  ##


class Foods(enum.Enum):

    Refrigerante = 1
    Cerveja = 2
    Biscoito = 3


##  BEGIN MAIN  ##

##  SHOULD BE COMPLETELY STATIC  ##
class Communication:

    def check_in(self, array):
        pass


class User:

    def __init__(self, userName, memberAmount, foodArray, foodAmount):
        self.userName = userName
        self.memberAmount = memberAmount
        self.foodArray = foodArray
        self.foodAmount = foodAmount
#    frequency
    pass


##  TESTES

errArray = [None]
errArray2 = None
print(erro1.not_null(None))
print(erro1.not_null([None]))
obj1 = User("Pedro", 4, ["leite", "feijao"], [1, 2])
print(obj1.userName, obj1.memberAmount, obj1.foodArray, obj1.foodAmount)

print(Foods.Refrigerante.name)

