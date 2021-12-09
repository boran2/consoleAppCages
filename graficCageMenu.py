import os
from cageDetail import CageDetail
from const import Constants
from linearCodeMenu import LinearCodeMenu

class graphicCageMenu:
    
    const = Constants()
        
    def __init__(self, k, g):
        self.k = k
        self.g = g

    # hlavicka programu
    def display_title_bar(self):
        os.system(self.const.CLEAR)     
        print("\t********************************************************")
        print("\t******               "+self.const.CAGE+" ("+str(self.k) +","+str(self.g) +") "+self.const.MENU+"              ******")
        print("\t********************************************************")
        
    # zoznam moznosti v menu
    def get_user_choice(self):
        print("\t  [1] " + self.const.SHOW_CAGE_GRAF)
        print("\t  [2] " + self.const.SHOW_H)
        print("\t  [3] " + self.const.SAVE_H)
        print("\t  [4] " + self.const.SHOW_CAGE_DATA)
        print("\t  [5] " + self.const.SHOW_MENU)
        print("\t  [x] " + self.const.BACK_TO_SHOWABLE_CAGES)   
        return input()

    # vyvolanie akcie na zaklade vyberu moznosti
    def create(self):
        choice = ''
        while choice != 'x':    
            self.display_title_bar()      
            choice = self.get_user_choice()
            self.display_title_bar()
            if choice == '1':
                CageDetail(self.k,self.g).showGraphOfCage()
            elif choice == '2':
                CageDetail(self.k,self.g).showParityCheckMatrix()
            elif choice == '3':
                CageDetail(self.k,self.g).saveParityCheckMatrix()
            elif choice == '4':
                CageDetail(self.k,self.g).showCageData()
            elif choice == '5':   
                LinearCodeMenu(self.k,self.g).create()
            elif choice == 'x':
                break
            else:
                print("\t  " + self.const.OTHER_OPTION + "\n")
