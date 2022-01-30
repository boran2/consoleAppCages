import os
import datetime
from cage import Cage
from linearCode import LinearCode
from const import Constants
from sage.all import *

class AutomorphismDetail:
    const = Constants()
    
    def __init__(self, k, g, permutation, showable):
        self.permutation = permutation
        self.k = k
        self.g = g
        self.showable = showable
    
    # hlavicka programu
    def display_title_bar(self):
        os.system(self.const.CLEAR)       
        print("\t*********************************************************************")
        print("\t******      "+ self.const.AUTOMORPHISM +str(self.permutation)  + " - "+ self.const.BIG_DETAIL + "    ******")
        print("\t*********************************************************************")
        
    # zoznam moznosti v menu
    def get_user_choice(self):
        print("\t  [x] " + self.const.BACK_TO_AUTGROUP +" "+self.const.CAGE+"("+str(self.k)+","+str(self.g)+")")   
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

        while choice != 'x':    
            self.display_title_bar()
            print('\t  '+self.const.INCIDENCE_MATRIX+'  \n' + str(H) + ' \n') 
            print('\t  '+self.const.G+'  \n' + str(G) + ' \n')    
            choice = self.get_user_choice() 
            self.display_title_bar()
            if choice == 'x':
                break
            else:
                print("\t  " + self.const.OTHER_OPTION + "\n")
    