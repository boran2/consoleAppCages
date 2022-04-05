import os
import datetime
from pickle import TRUE
from Cage import Cage
from Constants import Constants
from sage.all import *

class AutomorphismDetail:
    const = Constants()
    
    def __init__(self, k, g, permutation, showable, id, isCage):
        self.permutation = permutation
        self.k = k
        self.g = g
        self.showable = showable
        self.id = id
        self.isCage = isCage
    
    # hlavicka programu
    def display_title_bar(self):
        os.system(self.const.CLEAR)       
        print(self.getHeader())
        
    # zoznam moznosti v menu
    def get_user_choice(self):
        if self.isCage == TRUE:
            print("\t  [" + self.const.OPTION_X + "] " + self.const.BACK_TO  +  " "  + self.const.CAGE + "("+str(self.k) +","+str(self.g) +") " + self.const.AUTOMORPHISM_GROUP) 
        else:
            print("\t  [" + self.const.OPTION_X + "] " + self.const.BACK_TO  +  " "  + self.const.REC + "("+str(self.k) +","+str(self.g) +") " + self.const.AUTOMORPHISM_GROUP)    
        return input()
    

    # zobrazi graf obrazu kliekty pokial je to mozne a vygeneruje jeho kontrolnu a gener maticu  
    def showAutomorphism(self):
        graph = Cage(self.k,self.g)
        cage = graph.getCage()
        p = Permutation(self.permutation)
        cage.relabel(p)

        # podmienka prehladneho zobrazenia
        if (self.showable):
            cage.show(figsize=10)

        H = graph.getParityCheckMatrix(cage)
        C = codes.from_parity_check_matrix(H)
        G = C.systematic_generator_matrix()

        choice = ''

        while choice != self.const.OPTION_X:    
            self.display_title_bar()
            print('\t  ')
            print('\t  ') 
            print('\t  '+self.const.INCIDENCE_MATRIX+'  \n')
            print('\t  ') 
            print(str(H) + ' \n')
            print('\t  ') 
            print('\t  ') 
            print('\t  '+self.const.GENERATOR_MATRIX+'  \n')
            print('\t  ')
            print(str(G) + ' \n')  
            print('\t  ')  
            choice = self.get_user_choice() 
            self.display_title_bar()
            if choice == self.const.OPTION_X:
                break
            else:
                print("\t  " + self.const.OTHER_OPTION + "\n")

    # vrati sformatovanu hlavicku
    def getHeader(self):
        title = self.const.LEFT_BORDER + str(self.id) + ". " + self.const.AUTOMORPHISM + " " + str(self.permutation) + " " + self.const.DETAIL  + self.const.RIGHT_BORDER_BIG
        countCharsInString = len(str(title))
        border = '*'*countCharsInString
        header = "\t" + border + "\n\t" + title + "\n\t" + border
        return header