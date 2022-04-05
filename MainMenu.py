import os
from pickle import FALSE, TRUE
from Constants import Constants
from CageMenu import CageMenu

class MainMenu:
    const = Constants()
    
    # hlavicka programu
    def display_title_bar(self):
        os.system(self.const.CLEAR)
        print(self.getHeader())
    
    # zoznam moznosti v menu
    def get_user_choice(self):
        print("\t  ")
        print("\t  Vyberte graf vzdialenosti:")
        print("\t  ")
        print("\t    [" + self.const.OPTION_1 + "]  " + self.const.CAGE + "(3,5)")
        print("\t    [" + self.const.OPTION_2 + "]  " + self.const.CAGE + "(3,6)")
        print("\t    [" + self.const.OPTION_3 + "]  " + self.const.CAGE + "(3,7)")
        print("\t    [" + self.const.OPTION_4 + "]  " + self.const.CAGE + "(3,8)")
        print("\t    [" + self.const.OPTION_5 + "]  " + self.const.CAGE + "(3,10)")
        print("\t    [" + self.const.OPTION_6 + "]  " + self.const.CAGE + "(3,11)")
        print("\t    [" + self.const.OPTION_7 + "]  " + self.const.CAGE + "(3,14)")
        print("\t    [" + self.const.OPTION_8 + "]  " + self.const.REC + "(3,16)")
        print("\t    [" + self.const.OPTION_9 + "]  " + self.const.REC + "(3,17)")
        print("\t    [" + self.const.OPTION_10 + "] " + self.const.REC + "(3,18)")
        print("\t    [" + self.const.OPTION_11 + "] " + self.const.REC + "(3,20)")
        print("\t    [" + self.const.OPTION_12 + "] " + self.const.REC + "(3,23)")
        print("\t    [" + self.const.OPTION_13 + "] " + self.const.REC + "(3,25)")
        print("\t    [" + self.const.OPTION_14 + "] " + self.const.CAGE + "(4,5)")
        print("\t    [" + self.const.OPTION_15 + "] " + self.const.CAGE + "(4,7)")
        print("\t    [" + self.const.OPTION_16 + "] " + self.const.CAGE + "(4,9)")
        print("\t    [" + self.const.OPTION_17 + "] " + self.const.CAGE + "4,10)")
        print("\t    [" + self.const.OPTION_18 + "] " + self.const.CAGE + "(5,10)")
        print("\t    [" + self.const.OPTION_19 + "] " + self.const.CAGE + "(6,4)")
        print("\t    [" + self.const.OPTION_20 + "] " + self.const.CAGE + "(7,5)")
        print("\t    [" + self.const.OPTION_21 + "] " + self.const.CAGE + "(7,7)")
        print("\t    [" + self.const.OPTION_22 + "] " + self.const.CAGE + "(7,8)")
        print("\t    [" + self.const.OPTION_23 + "] " + self.const.REC + "(10,5)")
        print("\t    [" + self.const.OPTION_24 + "] " + self.const.REC + "(11,5)")
        print("\t    [" + self.const.OPTION_25 + "] " + self.const.REC + "(12,5)")
        print("\t    [" + self.const.OPTION_26 + "] " + self.const.REC + "(13,5)")
        print("\t  ")
        print("\t  [" + self.const.OPTION_Q + "] " + self.const.QUIT)   
        return input()

    # vyvolanie akcie na zaklade vyberu moznosti
    def main(self):
        choice = ''
        while choice != 'q':    
            self.display_title_bar()    
            choice = self.get_user_choice()
            self.display_title_bar()
            if choice == self.const.OPTION_1:
                CageMenu(3,5,TRUE,TRUE).create()
            elif choice == self.const.OPTION_2:
                CageMenu(3,6,TRUE,TRUE).create()
            elif choice == self.const.OPTION_3:
                CageMenu(3,7,TRUE,TRUE).create()
            elif choice == self.const.OPTION_4:
                CageMenu(3,8,TRUE,TRUE).create()
            elif choice == self.const.OPTION_5:
                CageMenu(3,10,TRUE,TRUE).create()
            elif choice == self.const.OPTION_6:
                CageMenu(3,11,TRUE,TRUE).create()
            elif choice == self.const.OPTION_7:
                CageMenu(3,14,TRUE,TRUE).create()
            elif choice == self.const.OPTION_8:
                CageMenu(3,16,FALSE,FALSE).create()
            elif choice == self.const.OPTION_9:
                CageMenu(3,17,FALSE,FALSE).create()
            elif choice == self.const.OPTION_10:
                CageMenu(3,18,FALSE,FALSE).create()
            elif choice == self.const.OPTION_11:
                CageMenu(3,20,FALSE,FALSE).create()
            elif choice == self.const.OPTION_12:
                CageMenu(3,23,FALSE,FALSE).create()
            elif choice == self.const.OPTION_13:
                CageMenu(3,25,FALSE,FALSE).create()
            elif choice == self.const.OPTION_14:
                CageMenu(4,5,TRUE,TRUE).create()
            elif choice == self.const.OPTION_15:
                CageMenu(4,7, TRUE,TRUE).create()
            elif choice == self.const.OPTION_16:
                CageMenu(4,9,TRUE,TRUE).create()
            elif choice == self.const.OPTION_17:
                CageMenu(4,10,FALSE,TRUE).create()
            elif choice == self.const.OPTION_18:
                CageMenu(5,10,FALSE,TRUE).create()
            elif choice == self.const.OPTION_19:
                CageMenu(6,4,TRUE,TRUE).create()
            elif choice == self.const.OPTION_20:
                CageMenu(7,5,TRUE,TRUE).create()
            elif choice == self.const.OPTION_21:
                CageMenu(7,7,FALSE,TRUE).create()
            elif choice == self.const.OPTION_22:
                CageMenu(7,8,FALSE,TRUE).create()
            elif choice == self.const.OPTION_23:
                CageMenu(10,5,FALSE,FALSE).create()
            elif choice == self.const.OPTION_24:
                CageMenu(11,5,FALSE,FALSE).create()
            elif choice == self.const.OPTION_25:
                CageMenu(12,5,FALSE,FALSE).create()
            elif choice == self.const.OPTION_26:
                CageMenu(13,5,FALSE,FALSE).create()
            elif choice == self.const.OPTION_Q:
                print("\t  "+self.const.BYE+"\n")
                break
            else:
                print("\t  " + self.const.OTHER_OPTION + "\n")

    # vrati sformatovanu hlavicku  
    def getHeader(self):
        title = self.const.LEFT_BORDER  +self.const.TESIS + " " + self.const.MAIN + " " + self.const.MENU + self.const.RIGHT_BORDER_BIG
        countCharsInString = len(str(title))
        border = '*'*countCharsInString
        header = "\t" + border + "\n\t" + title + "\n\t" + border
        return header

# spustenie programu
m = MainMenu()
m.main()