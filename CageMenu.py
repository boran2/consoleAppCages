import os
from pickle import TRUE
from CageDetail import CageDetail
from Constants import Constants
from LinearCodeMenu import LinearCodeMenu
from AutomorphismMenu import AutomorphismMenu

class CageMenu:
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
        print("\t    [" + self.const.OPTION_1 + "] " + self.const.SHOW_H)
        print("\t    [" + self.const.OPTION_2 + "] " + self.const.SAVE_H)
        print("\t    [" + self.const.OPTION_3 + "] " + self.const.SHOW_DATA)
        if self.isCage == TRUE:
            print("\t    [" + self.const.OPTION_4 + "] " + self.const.SHOW_AUTGROUP_CAGE)
            print("\t    [" + self.const.OPTION_5 + "] " + self.const.SAVE_AUTGROUP_CAGE)
        else:
            print("\t    [" + self.const.OPTION_4 + "] " + self.const.SHOW_AUTGROUP_REC)
            print("\t    [" + self.const.OPTION_5 + "] " + self.const.SAVE_AUTGROUP_REC)
        print("\t    [" + self.const.OPTION_6 + "] " + self.const.SHOW_CODE)
        if self.showable == TRUE:
            print("\t    [" + self.const.OPTION_7 + "] " + self.const.SHOW_GRAPH)
        print("\t  ")
        print("\t  [" + self.const.OPTION_X + "] "+self.const.BACK_TO+" "+self.const.MAIN+" "+self.const.MENU)   
        return input()

    # vyvolanie akcie na zaklade vyberu moznosti
    def create(self):
        choice = ''
        while choice != self.const.OPTION_X:    
            self.display_title_bar()      
            choice = self.get_user_choice()
            self.display_title_bar()
            if choice == self.const.OPTION_1:
                CageDetail(self.k,self.g,self.isCage).showParityCheckMatrix()
            elif choice == self.const.OPTION_2:
                CageDetail(self.k,self.g,self.isCage).saveParityCheckMatrix()
            elif choice == self.const.OPTION_3:
                CageDetail(self.k,self.g,self.isCage).showCageData()
            elif choice == self.const.OPTION_4:
                AutomorphismMenu(self.k,self.g,self.showable,self.isCage).createFromCage()
            elif choice == self.const.OPTION_5:
                CageDetail(self.k,self.g,self.isCage).saveAutomorphismGroup()
            elif choice == self.const.OPTION_6:
                LinearCodeMenu(self.k,self.g,self.showable,self.isCage).create()
            elif choice == '7' and self.showable == TRUE:
                CageDetail(self.k,self.g,self.isCage).showGraphOfCage()
            elif choice == self.const.OPTION_X:
                break
            else:
                print("\t  " + self.const.OTHER_OPTION + "\n")
    
    # vrati nazov menu
    def getTitle(self):
        spaceInString = len(str(self.k)) + len(str(self.g))
        title = "*****        "
        if self.isCage == TRUE:
            title += self.const.CAGE
            title += "("+str(self.k) +","+str(self.g) + ") " + self.const.MENU
        else:
            title += self.const.REC
            title += "("+str(self.k) +","+str(self.g) +") " + self.const.MENU + " "
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