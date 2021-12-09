import os
import datetime
from cage import Cage
from const import Constants
from sage.all import *

class CageDetail:
    const = Constants()
    
    def __init__(self, k, g):
        self.k = k
        self.g = g
    
    # hlavicka programu
    def display_title_bar(self):
        os.system(self.const.CLEAR)       
        print("\t********************************************************")
        print("\t******               "+self.const.CAGE+" ("+str(self.k) +","+str(self.g) +") "+self.const.DETAIL+"            ******")
        print("\t********************************************************")
        
    # zoznam moznosti v menu
    def get_user_choice(self):
        print("\t  [x] " + self.const.BACK_TO_CAGE_DETAILS)   
        return input()
    
    # zobrazi graf klietky
    def showGraphOfCage(self):
        graph = Cage(self.k,self.g)
        cage = graph.getCage()
        choice = ''
        cage.show(figsize=10)
        while choice != 'x':    
            self.display_title_bar()      
            choice = self.get_user_choice() 
            self.display_title_bar()
            if choice == 'x':
                break
            else:
                print("\t  " + self.const.OTHER_OPTION + "\n")
    
    # zobrazi incidencnu maticu klietky
    def showParityCheckMatrix(self):
        graph = Cage(self.k,self.g)
        choice = ''
        cage = graph.getCage()
        H = graph.getParityCheckMatrix(cage)
        while choice != 'x':    
            self.display_title_bar()      
            print('\t  '+self.const.INCIDENCE_MATRIX+'  \n' + str(H) + ' \n')
            choice = self.get_user_choice()
            self.display_title_bar()
            if choice == 'x':
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
        autGroup = len(cage.automorphism_group())
        R = graph.getRate(ver, edg)
        while choice != 'x':    
            self.display_title_bar()      
            print('\t  ' + self.const.MOORE_BOUND + '' + str(M) + ' \n')
            print('\t  '+self.const.N_VERTICES+ str(ver) + ' \n')
            print('\t  '+self.const.SIZE_H+ str(ver) + 'x' + str(edg) + ' \n')
            print('\t  '+self.const.N_EDGES+ str(edg) + ' \n')
            print('\t  '+self.const.AUTGROUP+ str(autGroup) + ' \n')
            print('\t  '+self.const.RATE+  str(R) + ' \n')
            choice = self.get_user_choice()
            self.display_title_bar()
            if choice == 'x':
                break
            else:
                print("\t  " + self.const.OTHER_OPTION + "\n")
    
    # ulozi maticu H
    def saveParityCheckMatrix(self):
        graph = Cage(self.k,self.g)
        choice = ''
        cage = graph.getCage()
        startTime = datetime.datetime.now()
        H = graph.getParityCheckMatrix(cage)
        file = open(self.const.H_DIR_PREFIX+str(self.k)+'_'+str(self.g)+self.const.TEXT_FILE, 'w')
        file.write(str(H))
        time = datetime.datetime.now() - startTime
        file.close()
        while choice != 'x':    
            self.display_title_bar()      
            print('\t  '+self.const.H_FILE_PREFIX+'('+str(self.k)+','+str(self.g)+') '+self.const.SUCCESS_CREATE+str(time.total_seconds()) +'s\n')
            choice = self.get_user_choice()  
            self.display_title_bar()
            if choice == 'x':
                break
            else:
                print("\t  " + self.const.OTHER_OPTION + "\n")