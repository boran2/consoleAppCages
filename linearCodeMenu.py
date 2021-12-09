import os
from const import Constants
from linearCode import LinearCode


class LinearCodeMenu:
    
    const = Constants()
        
    def __init__(self, k, g):
        self.k = k
        self.g = g

    # hlavicka programu
    def display_title_bar(self):
        os.system(self.const.CLEAR)
                
        print("\t********************************************************")
        print("\t******       "+self.const.C_DETAIL+" - "+self.const.CAGE+" ("+str(self.k)+","+str(self.g)+")        ******")
        print("\t********************************************************")
        
    # zoznam moznosti v menu
    def get_user_choice(self):
        print("\t  [1] " + self.const.SHOW_G)
        print("\t  [2] " + self.const.SAVE_g)
        print("\t  [3] " + self.const.SHOW_SIZE_G )
        print("\t  [4] "+ self.const.AUTGROUP_C)
        print("\t  [5] " + self.const.LENGTH_C)
        print("\t  [6] " + self.const.NUMBER_CODEWORDS)
        print("\t  [7] " +self.const.MIN_HAMMING)
        print("\t  [8] " + self.const.P_C)
        print("\t  [x] " +self.const.BACK_TO_CAGES)   
        return input()

    # vyvolanie akcie na zaklade vyberu moznosti
    def create(self):
        lCodeDetail = LinearCode(self.k,self.g)
        choice = ''
        while choice != 'x':    
            self.display_title_bar()      
            choice = self.get_user_choice()
            self.display_title_bar()
            if choice == '1':
                lCodeDetail.showGeneratorMatrix()
            elif choice == '2':
                lCodeDetail.saveGeneratorMatrix()
            elif choice == '3':
                lCodeDetail.showDimOfGeneratorMatrix()
            elif choice == '4':
                lCodeDetail.showNAutomorphism()
            elif choice == '5':
                lCodeDetail.showCodeLength()
            elif choice == '6':
                lCodeDetail.showMaxNCodeWords()
            elif choice == '7':
                lCodeDetail.showMinimumDistance()
            elif choice == '8':
                lCodeDetail.showPerfectCodeParameter()
            elif choice == 'x':
                break
            else:
                print("\t  " + self.const.OTHER_OPTION + "\n")