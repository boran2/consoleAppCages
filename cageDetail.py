import os
import datetime
from pickle import TRUE
from Cage import Cage
from Constants import Constants
from sage.all import *

class CageDetail:
    const = Constants()
    
    def __init__(self, k, g, isCage):
        self.k = k
        self.g = g
        self.isCage = isCage
    
    # hlavicka programu
    def display_title_bar(self):
        os.system(self.const.CLEAR)       
        print(self.getHeader())
        
    # zoznam moznosti v menu
    def get_user_choice(self):
        if self.isCage == TRUE:
            print("\t  [" + self.const.OPTION_X + "] " + self.const.BACK_TO  +  " "  + self.const.CAGE + "("+str(self.k) +","+str(self.g) + ") " + self.const.MENU) 
        else:
            print("\t  [" + self.const.OPTION_X + "] " + self.const.BACK_TO  +  " "  + self.const.REC + "("+str(self.k) +","+str(self.g) + ") " + self.const.MENU)  
        return input()
    
    # zobrazi graf klietky
    def showGraphOfCage(self):
        graph = Cage(self.k,self.g)
        cage = graph.getCage()
        choice = ''
        cage.show(figsize=10)
        while choice != self.const.OPTION_X:    
            self.display_title_bar()      
            choice = self.get_user_choice() 
            self.display_title_bar()
            print("\t  ")
            if choice == self.const.OPTION_X:
                break
            else:
                print("\t  " + self.const.OTHER_OPTION + "\n")
    
    # zobrazi incidencnu maticu klietky
    def showParityCheckMatrix(self):
        graph = Cage(self.k,self.g)
        choice = ''
        cage = graph.getCage()
        H = graph.getParityCheckMatrix(cage)
        while choice != self.const.OPTION_X:    
            self.display_title_bar()
            print("\t  ")    
            print("\t  " + self.const.PARITY_CHECK_MATRIX + " ")
            print("\t  ")
            print(str(H))
            print("\t  ")
            choice = self.get_user_choice()
            self.display_title_bar()
            if choice == self.const.OPTION_X:
               break
            else:
                print("\t  " + self.const.OTHER_OPTION + "\n")
        
    # zobrazi data o klietke
    def showCageData(self):
        graph = Cage(self.k,self.g)
        choice = ''
        M = graph.calculateMooreBound()
        cage = graph.getCage()
        ver = len(cage.vertices())
        edg = len(cage.edges(labels=False))
        R = graph.getRate(ver, edg)
        while choice != self.const.OPTION_X:    
            self.display_title_bar()
            print("\t  ")   
            print('\t    ' + self.const.MOORE_BOUND + '' + str(M) + ' \n')
            print('\t    '+self.const.N_VERTICES+ str(ver) + ' \n')
            print('\t    '+self.const.SIZE_H+ str(ver) + 'x' + str(edg) + ' \n')
            print('\t    '+self.const.N_EDGES+ str(edg) + ' \n')
            print('\t    '+self.const.RATE+  str(R) + ' \n')
            choice = self.get_user_choice()
            self.display_title_bar()
            if choice == self.const.OPTION_X:
                break
            else:
                print("\t  " + self.const.OTHER_OPTION + "\n")
    
    # ulozi maticu H
    def saveParityCheckMatrix(self):
        graph = Cage(self.k,self.g)
        choice = ''
        cage = graph.getCage()
        if not os.path.exists(self.const.PARITY_CHECK_MATRIX_DIRECTORY):
            os.makedirs(self.const.PARITY_CHECK_MATRIX_DIRECTORY)
        startTime = datetime.datetime.now()
        H = graph.getParityCheckMatrix(cage)
        file = open(self.const.H_DIR_PREFIX+str(self.k)+'_'+str(self.g)+self.const.TEXT_FILE, 'w')
        file.write(str(H))
        file.close()
        time = datetime.datetime.now() - startTime
        while choice != self.const.OPTION_X:    
            self.display_title_bar()
            print("\t  ")   
            print('\t    '+self.const.H_FILE_PREFIX+'('+str(self.k)+','+str(self.g)+') '+self.const.SUCCESS_CREATE+str(time.total_seconds()) +'s\n')
            choice = self.get_user_choice()  
            self.display_title_bar()
            if choice == self.const.OPTION_X:
                break
            else:
                print("\t  " + self.const.OTHER_OPTION + "\n")

    # ulozi grupu automorfizmov klietky alebo rec grafu
    def saveAutomorphismGroup(self):
        graph = Cage(self.k,self.g)
        choice = ''
        cage = graph.getCage()
        permutations = graph.getPermutationsOfAutomorphisms(cage)
        if not os.path.exists(self.const.AUTOMORPHISM_GROUP_DIRECTORY):
            os.makedirs(self.const.AUTOMORPHISM_GROUP_DIRECTORY)
        startTime = datetime.datetime.now()
        file = open(self.const.AUT_GROUP_CAGE_DIR_PREFIX+str(self.k)+'_'+str(self.g)+self.const.TEXT_FILE, 'w')
        file.write("[\n")
        for i in range(len(permutations)):
            file.write("\t" +str(permutations[i]))
            if i < len(permutations) - 1:
                file.write(",")
            file.write("\n")
        file.write("]")
        file.close()
        time = datetime.datetime.now() - startTime
        while choice != self.const.OPTION_X:    
            self.display_title_bar()
            print("\t  ")    
            print('\t    '+self.const.AUT_GROUP_FILE_PREFIX+'('+str(self.k)+','+str(self.g)+') '+self.const.SUCCESS_CREATE+str(time.total_seconds()) +'s\n')
            choice = self.get_user_choice()  
            self.display_title_bar()
            if choice == self.const.OPTION_X:
                break
            else:
                print("\t  " + self.const.OTHER_OPTION + "\n")
    
    # vrati nazov detailu
    def getTitle(self):
        spaceInString = len(str(self.k)) + len(str(self.g))
        title = self.const.LEFT_BORDER
        if self.isCage == TRUE:
            title += self.const.CAGE
            title += "("+str(self.k) +","+str(self.g) +") " + self.const.DETAIL
        else:
            title += self.const.REC
            title += "("+str(self.k) +","+str(self.g) +") " + self.const.DETAIL + " "
        if spaceInString == 3:
            title += self.const.RIGHT_BORDER_SMALL
        if spaceInString == 2:
            title += self.const.RIGHT_BORDER_BIG
        return title

    # vrati sformatovanu hlavicku
    def getHeader(self):
        title = self.getTitle()
        countCharsInString = len(str(title))
        border = '*'*countCharsInString
        header = "\t" + border + "\n\t" + title + "\n\t" + border
        return header