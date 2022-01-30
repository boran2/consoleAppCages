import os
from const import Constants
from graficCageMenu import graphicCageMenu

class GraphicCagesMenu:
    const = Constants()

    # hlavicka programu
    def display_title_bar(self):
        os.system(self.const.CLEAR)           
        print("\t********************************************************")
        print("\t*        "+self.const.SHOWABLE+"        *")
        print("\t********************************************************")
        
    # zoznam moznosti v menu
    def get_user_choice(self):
        print("\t  [1] "+self.const.CAGE+"(3,5)")
        print("\t  [2] "+self.const.CAGE+"(3,6)")
        print("\t  [3] "+self.const.CAGE+"(3,7)")
        print("\t  [4] "+self.const.CAGE+"(3,8)")
        print("\t  [5] "+self.const.CAGE+"(3,10)")
        print("\t  [6] "+self.const.CAGE+"(3,11)")
        print("\t  [7] "+self.const.CAGE+"(3,14)")
        print("\t  [8] "+self.const.CAGE+"(4,5)")
        print("\t  [9] "+self.const.CAGE+"(4,7)")
        print("\t  [10] "+self.const.CAGE+"(4,9)")
        print("\t  [11] "+self.const.CAGE+"(6,4)")
        print("\t  [12] "+self.const.CAGE+"(7,5)")
        print("\t  ")
        print("\t  [x] " + self.const.BACK_TO_CAGE_CATEGORIES)
        return input()

    # vyvolanie akcie na zaklade vyberu moznosti
    def create(self):
        choice = ''
        while choice != 'x':    
            self.display_title_bar()     
            choice = self.get_user_choice()
            self.display_title_bar()
            if choice == '1':
                graphicCageMenu(3,5).create()
            elif choice == '2':
                graphicCageMenu(3,6).create()
            elif choice == '3':
                graphicCageMenu(3,7).create()
            elif choice == '4':
                graphicCageMenu(3,8).create()
            elif choice == '5':
                graphicCageMenu(3,10).create()
            elif choice == '6':
                graphicCageMenu(3,11).create()
            elif choice == '7':
                graphicCageMenu(3,14).create()
            elif choice == '8':
                graphicCageMenu(4,5).create()
            elif choice == '9':
                graphicCageMenu(4,7).create()
            elif choice == '10':
                graphicCageMenu(4,9).create()
            elif choice == '11':
                graphicCageMenu(6,4).create()
            elif choice == '12':
                graphicCageMenu(7,5).create()
            elif choice == 'x':
                break
            else:
                print("\t  " + self.const.OTHER_OPTION + "\n")
