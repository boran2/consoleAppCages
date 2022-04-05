import os
from pickle import TRUE
from Constants import Constants
from LinearCode import LinearCode
from Cage import Cage
from AutomorphismDetail import AutomorphismDetail
import datetime


class AutomorphismMenu:
    
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
    def get_user_choice_Cage(self):
        graph = Cage(self.k,self.g)
        cage = graph.getCage()
        permutations = graph.getPermutationsOfAutomorphisms(cage)
        print("\t ")
        if self.isCage == TRUE:
            print("\t  " + self.const.N_AUTOMORPHISM_FROM + " " + self.const.CAGE +"("+str(self.k) +","+str(self.g) +"): "+str(len(permutations) + 1))
        else:
            print("\t  " + self.const.N_AUTOMORPHISM_FROM + " " + self.const.REC +"("+str(self.k) +","+str(self.g) +"): "+str(len(permutations) + 1))
        print("\t ")
        print("\t  " + self.const.CHOOSE_AUTOMORPHISM)
        print("\t ")
        for i in range(len(permutations)):
            print("\t    ["+str(i+1)+"] " + self.const.AUTOMORPHISM + "     " + str(permutations[i]))
        print("\t  ") 
        if self.isCage == TRUE:
            print("\t  [" + self.const.OPTION_X + "] " + self.const.BACK_TO  +  " "  + self.const.CAGE + "("+str(self.k) +","+str(self.g) + ") " + self.const.MENU) 
        else:
            print("\t  [" + self.const.OPTION_X + "] " + self.const.BACK_TO  +  " "  + self.const.REC + "("+str(self.k) +","+str(self.g) + ") " + self.const.MENU)  
        return input()  

    # vyvolanie akcie na zaklade vyberu moznosti
    def createFromCage(self):
        graph = Cage(self.k,self.g)
        choice = ''
        cage = graph.getCage()
        permutations = graph.getPermutationsOfAutomorphisms(cage)
        while choice != self.const.OPTION_X:    
            self.display_title_bar()  
            choice = self.get_user_choice_Cage()
            self.display_title_bar()

            for i in range(len(permutations)):
                if choice == str(i+1):
                    AutomorphismDetail(self.k, self.g, permutations[i], self.showable, str(i+1), self.isCage).showAutomorphism()
  
            if choice == self.const.OPTION_X:
                break

    #    navrat
    def get_user_choice_Code(self):
        if self.isCage == TRUE:
            print("\t  [" + self.const.OPTION_X + "] " + self.const.BACK_TO  +  " "  + self.const.CAGE + "("+str(self.k) +","+str(self.g) +") " + self.const.LINEAR_CODE + " " + self.const.MENU) 
        else:
            print("\t  [" + self.const.OPTION_X + "] " + self.const.BACK_TO  +  " "  + self.const.REC + "("+str(self.k) +","+str(self.g) +") " + self.const.LINEAR_CODE + " " + self.const.MENU)  
        return input()


    #    zobrazenie grupy automorfizmov z linearneho kodu
    def createFromLinearCode(self):
        linearCode = LinearCode(self.k,self.g,self.isCage)
        choice = ''
        permutations = linearCode.getPermutationsOfAutomorphisms()

        while choice != self.const.OPTION_X:    
            self.display_title_bar()
            print("\t ")
            if self.isCage == TRUE:
                print("\t  " + self.const.N_AUTOMORPHISM_FROM + " " + self.const.CAGE + "(" + str(self.k) +","+str(self.g) + ") " + self.const.FROM_CODE + " " + str(len(permutations) + 1))
            else:
                print("\t  " + self.const.N_AUTOMORPHISM_FROM + " " + self.const.REC + "("+ str(self.k) +","+str(self.g) + ") " + self.const.FROM_CODE + " " +str(len(permutations) + 1))
            print("\t ")
            for i in range(len(permutations)):
                print("\t    "+str(i+1) + self.const.NTH_AUTOMORPHISM + "     " + str(permutations[i]))
            print("\t  ") 
            choice = self.get_user_choice_Code()
            self.display_title_bar()
  
            if choice == self.const.OPTION_X:
                break

    #    ulozenie grupy automorfizmov z linearneho kodu
    def saveAutomorphismGroup(self):
        linearCode = LinearCode(self.k,self.g,self.isCage)
        choice = ''
        permutations = linearCode.getPermutationsOfAutomorphisms()
        if not os.path.exists(self.const.AUTOMORPHISM_GROUP_DIRECTORY):
            os.makedirs(self.const.AUTOMORPHISM_GROUP_DIRECTORY)
        startTime = datetime.datetime.now()
        file = open(self.const.AUT_GROUP_CAGE_DIR_PREFIX+str(self.k)+'_'+str(self.g)+self.const.AUT_GROUP_SUFFIX+self.const.TEXT_FILE, 'w')
        file.write("[\n")
        for i in range(len(permutations)):
            file.write("\t" +str(permutations[i]))
            if i < len(permutations) - 1:
                file.write(",")
            file.write("\n")
        file.write("]")
        file.close()
        time = datetime.datetime.now() - startTime
        while choice != self.const.OPTION_X:    
            self.display_title_bar()
            print("\t ")
            print('\t    '+self.const.AUT_GROUP_FILE_PREFIX+'('+str(self.k)+','+str(self.g)+')'+ self.const.AUT_GROUP_SUFFIX+ ' '+self.const.SUCCESS_CREATE+str(time.total_seconds()) +'s\n')
            choice = self.get_user_choice_Code()  
            self.display_title_bar()
            if choice == self.const.OPTION_X:
                break
            else:
                print("\t  " + self.const.OTHER_OPTION + "\n")
    
    # vrati sformatovany nazov menu
    def getTitle(self):
        spaceInString = len(str(self.k)) + len(str(self.g))
        title = self.const.LEFT_BORDER
        if self.isCage == TRUE:
            title += self.const.CAGE
            title += "("+str(self.k) +","+str(self.g) +") " + self.const.AUTOMORPHISM_GROUP
        else:
            title += self.const.REC
            title += "("+str(self.k) +","+str(self.g) +") " + self.const.AUTOMORPHISM_GROUP
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