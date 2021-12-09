import os
import datetime
from cage import Cage
from const import Constants
from sage.all import *

class LinearCode:
    
    const = Constants()
        
    def __init__(self, k, g):
        self.k = k
        self.g = g
        
    # hlavicka programu
    def display_title_bar(self):
        os.system(self.const.CLEAR)
                
        print("\t********************************************************")
        print("\t******      "+self.const.LINEAR_CODE_MENU+" - "+self.const.CAGE+"("+str(self.k)+","+str(self.g)+")       ******")
        print("\t********************************************************")
    
    # zoznam moznosti v menu
    def get_user_choice(self):
        print("\t  [x] " + self.const.BACK_TO_C_MENU)   
        return input()

    # vrati kontrolnu maticu linearneho kodu ako incidencnu maticu klietky ziskanu z grafu nad polom Z2
    def getParityCheckMatrixFromCage(self):
        return Cage(self.k,self.g).getParityCheckMatrix(Cage(self.k,self.g).getCage())

    # vrati generujucu maticu linearneho kodu z kontrolnej matice
    def getGeneratorMatrix(self,H):
        C = self.getLinearCode(H)
        return C.systematic_generator_matrix()
    
    # vrati linearny kod z kontrolnej matice 
    def getLinearCode(self,H):
        return codes.from_parity_check_matrix(H)
    
    # vypocita pocet kodovych slov pomocou generujucej matice
    def countMaxNumberOfCodewords(self,G):
        return 2**(G.nrows())
    
    # udava vzdialenost nasho kodu od perfektneho v intervale 0 - 1, kedy 1 je perfektny kod
    def getPerfectCodeParameter(self,n,M,d):
        if d % 2 == 1:
            t = (d-1)/2     # t=(d-1)/2 pre neparne
        else:
            t = (d-2)/2    # parne (d-1)/2 dostavam desatinne cislo, uvazujem len cele, preto d-2
        sum = 0.0
        for i in range(0,int(t) + 1):
            sum = sum + self.combinationNumber(n,i)
        parameter = (M*sum)/(2**n)
        return parameter

    # vypocet faktorialu
    def factorial(self,n):
        fact = 1
        for i in range(1,n+1):
            fact = fact * i
        return fact

    # vypocet kombinacneho cisla
    def combinationNumber(self,n,k):
        return self.factorial(n)/(self.factorial(k)*self.factorial(n-k))
    
    # ak je sucet vsetkych elementov matice sucinu G a Ht rovny 0 a sucasne plati ze ma tato matica 
    # rovnaky pocet riadkov ako G a rovnaky pocet stlpcov ako H^t potom je kod validny
    def isLinearCodeValid(self,G,H):
        Ht = H.transpose()
        validationMatrix = G * Ht
        elementsSum = sum(sum(validationMatrix))
        if len(G.column(0)) == len(validationMatrix.column(0)) and len(Ht.row(0)) == len(validationMatrix.row(0)) and elementsSum == 0:
            return True
        else:
            return False
    
    # zisti minimalnu vzdialenost v kode
    def getMinimumDistance(self,H):
        C = self.getLinearCode(H)
        return C.minimum_distance()
    
    # zisti pocet automorfizmov z kodu
    def getNumberOfAutomorphism(self,H):
        C = self.getLinearCode(H)
        Gr = C.permutation_automorphism_group(algorithm = "partition")
        return Gr.order()
    
    # zisti pocet kodovych slov
    def getMaxNCodewords(self,H):
        G = self.getGeneratorMatrix(H)
        return self.countMaxNumberOfCodewords(G)

    # zisti dlzku kodu
    def getCodeLength(self,H):
        G = self.getGeneratorMatrix(H)
        return G.ncols()
    
    # zobrazi generujucu maticu
    def showGeneratorMatrix(self):
        choice = ''
        H = self.getParityCheckMatrixFromCage()
        G = self.getGeneratorMatrix(H)
        b = self.isLinearCodeValid(G,H)
        while choice != 'x':    
            self.display_title_bar()
            print('\t  '+ self.const.G+' \n' + str(G) + ' \n');
            if(b):
                print('\t  '+self.const.C_VALID+' \n')
            else:
                print('\t  '+self.const.C_INVALID+' \n')
            choice = self.get_user_choice()
            self.display_title_bar()
            if choice == 'x':
               break
            else:
                print("\t  " + self.const.OTHER_OPTION + "\n")
    
    # ulozi generujucu maticu
    def saveGeneratorMatrix(self):
        choice = ''
        H = self.getParityCheckMatrixFromCage()
        startTime = datetime.datetime.now()
        G = self.getGeneratorMatrix(H)
        file = open(self.const.G_DIR_PREFIX+str(self.k)+'_'+str(self.g)+self.const.TEXT_FILE, 'w')
        file.write(str(G))
        time = datetime.datetime.now() - startTime
        file.close()
        while choice != 'x':    
            self.display_title_bar()      
            print('\t  '+self.const.G_FILE_PREFIX+str(self.k)+','+str(self.g)+') '+self.const.SUCCESS_CREATE+str(time.total_seconds()) +'s\n')
            choice = self.get_user_choice()  
            self.display_title_bar()
            if choice == 'x':
                break
            else:
                print("\t  " + self.const.OTHER_OPTION + "\n")
    
    # zobrazi rozmer generujucej matice
    def showDimOfGeneratorMatrix(self):
        choice = ''
        H = self.getParityCheckMatrixFromCage()
        G = self.getGeneratorMatrix(H)
        while choice != 'x':    
            self.display_title_bar()      
            print('\t  ' +self.const.G_SIZE + str(G.nrows()) +'x'+ str(G.ncols()) + ' \n')
            choice = self.get_user_choice()  
            self.display_title_bar()
            if choice == 'x':
                break
            else:
                print("\t  " + self.const.OTHER_OPTION + "\n") 
    
    # zobrazi minimalnu vzdialenost kodu          
    def showMinimumDistance(self):
        choice = ''
        H = self.getParityCheckMatrixFromCage()
        d = self.getMinimumDistance(H)  
        while choice != 'x':    
            self.display_title_bar()
            print('\t  '+self.const.D+ str(d) + ' \n');
            choice = self.get_user_choice()
            self.display_title_bar()
            if choice == 'x':
               break
            else:
                print("\t  " + self.const.OTHER_OPTION + "\n")
    
    # zobrazi pocet automorfizmov z lin. kodu
    def showNAutomorphism(self):
        choice = ''
        H = self.getParityCheckMatrixFromCage()
        autGroupC = self.getNumberOfAutomorphism(H)  
        while choice != 'x':    
            self.display_title_bar()
            print('\t  '+self.const.AUTGROUP_CODE + str(autGroupC) + ' \n');
            choice = self.get_user_choice()
            self.display_title_bar()
            if choice == 'x':
               break
            else:
                print("\t  " + self.const.OTHER_OPTION + "\n")
    
    # zobrazi dlzku kodu
    def showCodeLength(self):
        choice = ''
        H = self.getParityCheckMatrixFromCage()
        n = self.getCodeLength(H)
        while choice != 'x':    
            self.display_title_bar()
            print('\t  ' +self.const.N+ str(n) + ' \n');
            choice = self.get_user_choice()
            self.display_title_bar()
            if choice == 'x':
               break
            else:
                print("\t  " + self.const.OTHER_OPTION + "\n")
    
    # zobrazi pocet kodovych slov
    def showMaxNCodeWords(self):
        choice = ''
        H = self.getParityCheckMatrixFromCage()
        m = self.getMaxNCodewords(H)
        while choice != 'x':    
            self.display_title_bar()
            print('\t  '+self.const.N_CODEWORDS + str(m) + ' \n');
            choice = self.get_user_choice()
            self.display_title_bar()
            if choice == 'x':
               break
            else:
                print("\t  " + self.const.OTHER_OPTION + "\n")      
    
    # zobrazi parameter perfektneho kodu
    def showPerfectCodeParameter(self):
        choice = ''
        H = self.getParityCheckMatrixFromCage()
        n = self.getCodeLength(H)
        m = self.getMaxNCodewords(H)
        d = self.getMinimumDistance(H)
        p = self.getPerfectCodeParameter(n,m,d)
        while choice != 'x':    
            self.display_title_bar()
            print('\t  '+self.const.P_PAR + str(p) + ' \n');
            choice = self.get_user_choice()
            self.display_title_bar()
            if choice == 'x':
               break
            else:
                print("\t  " + self.const.OTHER_OPTION + "\n")