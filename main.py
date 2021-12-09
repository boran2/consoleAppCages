import os
from const import Constants
from difficultCagesMenu import DifficultCagesMenu
from graphicCagesMenu import GraphicCagesMenu

class Main:
    const = Constants()
    
    # hlavicka programu
    def display_title_bar(self):
        os.system(self.const.CLEAR)
                    
        print("\t********************************************************")
        print("\t*         "+self.const.TESIS+"         *")
        print("\t********************************************************")
    
    # zoznam moznosti v menu
    def get_user_choice(self):
        print("\t  [1] " + self.const.SHOWABLE_CATEGORY)
        print("\t  [2] " + self.const.NO_SHOWABLE_CATEGORY)
        print("\t  [q] " + self.const.QUIT)   
        return input()

    # vyvolanie akcie na zaklade vyberu moznosti
    def main(self):
        choice = ''
        while choice != 'q':    
            self.display_title_bar()    
            choice = self.get_user_choice()
            self.display_title_bar()
            if choice == '1':
                GraphicCagesMenu().create()
            elif choice == '2':
                DifficultCagesMenu().create()
            elif choice == 'q':
                print("\t  "+self.const.BYE+"\n")
                break
            else:
                print("\t  " + self.const.OTHER_OPTION + "\n")
                
# spustenie programu
m = Main()
m.main()