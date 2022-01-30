import os
from const import Constants
from linearCode import LinearCode
from cage import Cage
from automorphism import AutomorphismDetail


class AutomorphismMenu:
    
    const = Constants()
        
    def __init__(self, k, g, showable):
        self.k = k
        self.g = g
        self.showable = showable

    # hlavicka programu
    def display_title_bar(self):
        os.system(self.const.CLEAR)
                
        print("\t*********************************************************************")
        print("\t******           " + self.const.AUT_GROUP + " - " + self.const.CAGE + " ("+str(self.k)+","+str(self.g)+")           ******")
        print("\t*********************************************************************")
        
    # zoznam moznosti v menu
    def get_user_choice(self):
        graph = Cage(self.k,self.g)
        choice = ''
        cage = graph.getCage()
        permutations = graph.getPermutationsOfAutomorphisms(cage) 
        for i in range(len(permutations)):
            print("\t  ["+str(i+1)+"] "+self.const.AUT_GROUP+"      " + str(permutations[i]))
        print("\t  ") 
        print("\t  [x] " + self.const.BACK_TO +" "+ self.const.CAGE+"("+str(self.k)+","+str(self.g)+") - " + self.const.MENU)   
        return input()

    # vyvolanie akcie na zaklade vyberu moznosti
    def create(self):
        graph = Cage(self.k,self.g)
        choice = ''
        cage = graph.getCage()
        permutations = graph.getPermutationsOfAutomorphisms(cage)
        while choice != 'x':    
            self.display_title_bar()  
            choice = self.get_user_choice()
            self.display_title_bar()

            for i in range(len(permutations)):
                if choice == str(i+1):
                    AutomorphismDetail(self.k, self.g, permutations[i], self.showable).showAutomorphism()
  
            if choice == 'x':
                break