import os
from pickle import TRUE
from AutomorphismMenu import AutomorphismMenu
from Constants import Constants
from LinearCode import LinearCode


class LinearCodeMenu:
    
    const = Constants()
        
    def __init__(self, k, g, showable, isCage):
        self.k = k
        self.g = g
        self.showable = showable
        self.isCage = isCage

    # hlavicka programu
    def display_title_bar(self):
        os.system(self.const.CLEAR)
        print(self.getHeader())
        
    # zoznam moznosti v menu
    def get_user_choice(self):
        print("\t  ")
        print("\t  " + self.const.CHOOSE_FROM_OPTIONS)
        print("\t ")
        print("\t    [" + self.const.OPTION_1 + "] " + self.const.SHOW_G)
        print("\t    [" + self.const.OPTION_2 + "] " + self.const.SAVE_G)
        print("\t    [" + self.const.OPTION_3 + "] " + self.const.SHOW_DIM_G)
        print("\t    [" + self.const.OPTION_4 + "] " + self.const.SHOW_AUTGROUP_C)
        print("\t    [" + self.const.OPTION_5 + "] " + self.const.SAVE_AUTGROUP_C)
        print("\t    [" + self.const.OPTION_6 + "] " + self.const.SHOW_N_M)
        print("\t    [" + self.const.OPTION_7 + "] " + self.const.SHOW_D)
        print("\t    [" + self.const.OPTION_8 + "] " + self.const.SHOW_P)
        print("\t  ")
        if self.isCage == TRUE:
            print("\t  [" + self.const.OPTION_X + "] " + self.const.BACK_TO + " " + self.const.CAGE  + "("+str(self.k) +","+str(self.g) + ") " + self.const.MENU) 
        else:
            print("\t  [" + self.const.OPTION_X + "] " + self.const.BACK_TO  +  " "  + self.const.REC + "("+str(self.k) +","+str(self.g) + ") " + self.const.MENU)  
        return input()  

    # vyvolanie akcie na zaklade vyberu moznosti
    def create(self):
        lCodeDetail = LinearCode(self.k,self.g,self.isCage)
        choice = ''
        while choice != self.const.OPTION_X:    
            self.display_title_bar()      
            choice = self.get_user_choice()
            self.display_title_bar()
            if choice == self.const.OPTION_1:
                lCodeDetail.showGeneratorMatrix()
            elif choice == self.const.OPTION_2:
                lCodeDetail.saveGeneratorMatrix()
            elif choice == self.const.OPTION_3:
                lCodeDetail.showDimOfGeneratorMatrix()
            elif choice == self.const.OPTION_4:
                AutomorphismMenu(self.k,self.g, self.showable, self.isCage).createFromLinearCode()
            elif choice == self.const.OPTION_5:
                AutomorphismMenu(self.k,self.g, self.showable, self.isCage).saveAutomorphismGroup()
            elif choice == self.const.OPTION_6:
                lCodeDetail.showCodeLengthAndMaxNCodeWords()
            elif choice == self.const.OPTION_7:
                lCodeDetail.showMinimumDistance()
            elif choice == self.const.OPTION_8:
                lCodeDetail.showPerfectCodeParameter()
            elif choice == self.const.OPTION_X:
                break
            else:
                print("\t  " + self.const.OTHER_OPTION + "\n")

# vrati nazov menu
    def getTitle(self):
        spaceInString = len(str(self.k)) + len(str(self.g))
        title = self.const.LEFT_BORDER
        if self.isCage == TRUE:
            title += self.const.CAGE
            title += "("+str(self.k) +","+str(self.g) +") " + self.const.LINEAR_CODE + " " + self.const.MENU
        else:
            title += self.const.REC
            title += "("+str(self.k) +","+str(self.g) +") " + self.const.LINEAR_CODE + " " + self.const.MENU
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