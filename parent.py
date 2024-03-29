##  IMPORTS  ##

import erro1
import enum

##  TYPEDEFS AND ENUMS  ##

'''
class Foods(enum.Enum):

    Refrigerante = 1
    Cerveja = 2
    Biscoito = 3
'''

##  BEGIN MAIN  ##

##  SHOULD BE COMPLETELY STATIC  ##
class Communication:

    def check_in(array):
        if (erro1.not_null(array) != 0):
            return erro1.not_null(array)
        pass

    def ler_arq(nomeArq):

        result = list()
        currentArray = list()
        currentLine = ""
        listComida = list()
        auxArray = list()
        count = 0

        arq = open(nomeArq, "r")
        linesAmount = len(arq.readlines())
        arq.close()

        arq = open(nomeArq, "r")
        for index in range(linesAmount):

            count += 1
            currentLine = arq.readline()

            if (currentLine[0] == "~"):
                currentArray.append(currentLine[1:len(currentLine) - 1])
                count = 0

            if (count == 1):
                currentArray.append(int(currentLine))
            if (count == 2):
                currentArray.append(currentLine.split())

            if (count == 3):
                auxArray.clear()
                for index2 in range(len(currentLine.split())):
                    auxArray.append(int(currentLine.split()[index2]))
                currentArray.append(auxArray.copy())

            if (count == 4):
                auxArray.clear()
                for index2 in range(len(currentLine.split())):
                    auxArray.append(int(currentLine.split()[index2]))
                currentArray.append(auxArray.copy())

                result.append(currentArray.copy())
                currentArray.clear()

        arq.close()
        return result

    def escrever_arq(array):

        arq = open('ArqListas.txt', 'a')

        arq.seek(0)

        arq.write("~")
        arq.write(array[0])
        arq.write("\n")
        arq.write(str(array[1]))
        arq.write("\n")
        for index in range(len(array[2])):
            arq.write(array[2][index])
            arq.write(" ")
        arq.write("\n")
        for index in range(len(array[3])):
            arq.write(str(array[3][index]))
            arq.write(" ")
        arq.write("\n")

        arq.close()
        return 0


class User:

    userName = ""
    memberAmount = 1
    foodArray = list()
    foodAmount = list()
    wasteBoolArray = list()

    def set_subfoods(self, array):

        foods = read_foods()
        subFoods = open("subFoods.txt", "w")
        subFoods.close()
        subFoods = open("subFoods.txt", "a")
        subFoods.seek(0)

        for index in range(len(foods)):
            if array.count(str(index)) > 0:
               subFoods.write("1 \n")
            else:
                subFoods.write("0 \n")

        subFoods.close()

    def set_food_array(self):

        listaVazia = list()
        arq = open('subFoods.txt', 'r')
        linha = arq.readline()
        foods = read_foods()

        while linha != '':
            if (linha[0] == "1"):
                listaVazia.append(linha)
            linha = arq.readline()



        for index in range(len(listaVazia)):
            if listaVazia[index][0] == "1":
                listaVazia[index] = foods[index]

        arq.close()

        self.foodArray = listaVazia
        return listaVazia

    def set_recommendations(self, averageArray):

        result = list()
        foods = read_foods()
        wastedFoods = list()
        position = 0
        aux = 0

        print(self.foodArray)

        for index in range(len(self.foodAmount)):

            if (self.wasteBoolArray[index] != 0):
                wastedFoods.append(self.foodArray[index])
                position = foods.index(self.foodArray[index])
                if (self.foodAmount[index] >= (2*averageArray[position])):
                    result.append((averageArray[position] + int(averageArray[position]/5)))
                elif ((self.foodAmount[index] >= averageArray[position])
                and(self.foodAmount[index] <= (2*averageArray[position]))):
                    result.append((averageArray[position] + self.foodAmount[index])/2)
                elif (self.foodAmount[index] < averageArray[position]):
                    if (self.foodAmount[index]/4 >= 1):
                        result.append(self.foodAmount[index] - int(self.foodAmount[index]/4))
                    else:
                        result.append(self.foodAmount[index] - 1)

        for index in range(len(result)):
            result[index] = int(result[index])

        print(wastedFoods)
        return result

    pass


class AverageCalculator:

    def set_totals(self):

        rawData = Communication.ler_arq("ArqListas.txt")
        rawFoods = read_foods()
        rawSums = list()
        rawPeople = list()

        for index in range(len(rawFoods)):

            rawSums.append(0)
            rawPeople.append(0)

            for index2 in range(len(rawData)):

                for index3 in range(len(rawData[index2][2])):

                    if ((rawData[index2][2][index3] == rawFoods[index])
                    and (rawData[index2][4][index3] == 0)):
                        rawSums[index] += rawData[index2][3][index3]
                        rawPeople[index] += 1

        return [rawSums, rawPeople]

    def set_average(self, sumArray, peopleArray):

        result = list()

        for index in range(len(sumArray)):
            if (peopleArray[index] != 0):
                result.append(sumArray[index]/peopleArray[index])

        return result

    def set_waste(self):

        rawData = Communication.ler_arq("ArqListas.txt")
        rawFoods = read_foods()
        rawPeople = list()
        wasteSums = list()
        found = False

        for index in range(len(rawFoods)):

            wasteSums.append(0)
            rawPeople.append(0)

            for index2 in range(len(rawData)):

                found = False
                for index3 in range(len(rawData[index2][2])):

                    if ((rawData[index2][2][index3] == rawFoods[index])
                    and (rawData[index2][4][index3] == 1)):
                        found = True
                        wasteSums[index] += rawData[index2][3][index3]
                        rawPeople[index] += 1

        return [wasteSums, rawPeople]

    def set_waste_average(self, wasteSumArray, peopleArray):

        result = list()

        for index in range(len(wasteSumArray)):
            if (peopleArray[index] != 0) and (wasteSumArray[index] != 0):
                result.append(wasteSumArray[index] / peopleArray[index])
            else:
                result.append(0)

        return result

class UsrInterface:

    def home_screen(self):
        print("||=====================================")
        print("||                           (3)Sair            ")
        print("||  (1)Entrar dados                    ")
        print("||  (2)Sugestão de compras             ")
        print("||           ")
        print("||                                     ")
        print("||=====================================")

        entryMenu = input()
        if (entryMenu == "1"):
            print("||=====================================")
            print("|| Quais desses produtos voce consome? ")
            print("|| (Ex resposta: \"0 3 4 6\", ou \"2\")    ")
            print("||                                     ")
            print("||   (1)Refrigerante                   ")
            print("||   (2)Leite                          ")
            print("||   (3)Cerveja                        ")
            print("||   (4)Feijao                         ")
            print("||   (5)Arroz                          ")
            print("||   (6)Farinha                        ")
            print("||   (7)Biscoito                       ")
            print("||=====================================")
            entryMenu = input()
            userFoods = entryMenu.split()

##  AUXILIARY FUNCTIONS  ##


def read_foods():

    listaVazia = list()
    arq = open('foods.txt', 'r')
    linha = arq.readline()

    while linha != '':
        listaVazia.append(linha)
        linha = arq.readline()

    for index in range(len(listaVazia)):
        if listaVazia[index][-1] == '\n':
            listaVazia[index] = listaVazia[index][0:-1]

    arq.close()

    return listaVazia

##  TESTES

'''
        if (entryMenu == "2"):
            print("||=====================================")
            print("|| Produtos recomendados               ")
            print("|| (Ex resposta: \"0 3 4 6\", ou \"2\")")
            print("||                                     ")
            print("||   (1)<var1>                         ")
            print("||   (2)<var2>                         ")
            print("||   (3)<var3>                         ")
            print("||   (4)<var4>                         ")
            print("||   (5)<var5>                         ")
            print("||   (6)<var6>                         ")
            print("||   (7)<var7>                         ")
            print("||=====================================")
            entryMenu = input()
            userFoods = entryMenu.split()           

def waste_screen(self):
    print("||=====================================")
    print("||   Houve sobra da compra de <var1>?  ")
    print("||  (1)Sim                             ")
    print("||  (2)Não                             ")
    print("||                                     ")
    print("||=====================================")
def name_screen(self):
    print("||=====================================")
    print("||   Insira seu nome:                  ")
    print("||   <input()>                         ")
    print("||                                     ")
    print("||                                     ")
    print("||=====================================")
    
'''

AverageObj = AverageCalculator()
totals = AverageObj.set_totals()
wasteTotals = AverageObj.set_waste()

AverageObj.set_waste_average(wasteTotals[0], wasteTotals[1])
averages = AverageObj.set_average(totals[0], totals[1])

UIObj = UsrInterface()

UserObj = User()
UserObj.set_subfoods(["1", "3", "4", "6"])
UserObj.set_food_array()
UserObj.userName = "bento"
UserObj.memberAmount = 1
UserObj.foodAmount = [2, 12, 2, 2]
UserObj.wasteBoolArray = [0, 1, 0, 1]

print()
print(UserObj.set_recommendations(averages))

#UIObj.home_screen()