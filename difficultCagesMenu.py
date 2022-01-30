import os
from const import Constants
from dificultCageMenu import dificultCageMenu

class DifficultCagesMenu:

    const = Constants()
    
    # hlavicka programu
    def display_title_bar(self):
        os.system(self.const.CLEAR)   
        print("\t********************************************************")
        print("\t*       "+self.const.NO_SHOWABLE+"       *")
        print("\t********************************************************")

    # zoznam moznosti v menu
    def get_user_choice(self):
        print("\t  [1] "+self.const.CAGE+"(3,16)")
        print("\t  [2] "+self.const.CAGE+"(3,17)")
        print("\t  [3] "+self.const.CAGE+"(3,18)")
        print("\t  [4] "+self.const.CAGE+"(3,20)")
        print("\t  [5] "+self.const.CAGE+"(3,23)")
        print("\t  [6] "+self.const.CAGE+"(3,25)")
        print("\t  [7] "+self.const.CAGE+"(4,10)")
        print("\t  [8] "+self.const.CAGE+"(5,10)")
        print("\t  [9] "+self.const.CAGE+"(7,7)")
        print("\t  [10] "+self.const.CAGE+"(7,8)")
        print("\t  [11] "+self.const.CAGE+"(10,5)")
        print("\t  [12] "+self.const.CAGE+"(11,5)")
        print("\t  [13] "+self.const.CAGE+"(12,5)")
        print("\t  [14] "+self.const.CAGE+"(13,5)")
        print("\t  ")
        print("\t  [x] " + self.const.BACK_TO_CAGE_CATEGORIES)   
        return input()

    # vyvolanie akcie na zaklade moznosti
    def create(self):
        choice = ''
        while choice != 'x':    
            self.display_title_bar()    
            choice = self.get_user_choice()
            self.display_title_bar()
            if choice == '1':
                dificultCageMenu(3,16).create()
            elif choice == '2':
                dificultCageMenu(3,17).create()
            elif choice == '3':
                dificultCageMenu(3,18).create()
            elif choice == '4':
                dificultCageMenu(3,20).create()
            elif choice == '5':
                dificultCageMenu(3,23).create()
            elif choice == '6':
                dificultCageMenu(3,25).create()
            elif choice == '7':
                dificultCageMenu(4,10).create()
            elif choice == '8':
                dificultCageMenu(5,10).create()
            elif choice == '9':
                dificultCageMenu(7,7).create()
            elif choice == '10':
                dificultCageMenu(7,8).create()
            elif choice == '11':
                dificultCageMenu(10,5).create()
            elif choice == '12':
                dificultCageMenu(11,5).create()
            elif choice == '13':
                dificultCageMenu(12,5).create()
            elif choice == '14':
                dificultCageMenu(13,5).create()
            elif choice == 'x':
                break
            else:
                print("\t  " + self.const.OTHER_OPTION + "\n")