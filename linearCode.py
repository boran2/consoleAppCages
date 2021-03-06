import os
import datetime
from pickle import TRUE
from re import X
from Cage import Cage
from Constants import Constants
from sage.all import *

class LinearCode:
    
    const = Constants()
        
    def __init__(self, k, g, isCage):
        self.k = k
        self.g = g
        self.isCage = isCage
        
    # hlavicka programu
    def display_title_bar(self):
        os.system(self.const.CLEAR)
        print(self.getHeader())
    
    # zoznam moznosti v menu
    def get_user_choice(self):
        if self.isCage == TRUE:
            print("\t  [" + self.const.OPTION_X + "] " + self.const.BACK_TO  +  "  " + self.const.CAGE +"("+str(self.k) +","+str(self.g) +") " + self.const.LINEAR_CODE + " " + self.const.MENU)  
        else:
            print("\t  [" + self.const.OPTION_X + "] " + self.const.BACK_TO  +  "  " + self.const.REC +"("+str(self.k) +","+str(self.g) +") " + self.const.LINEAR_CODE + " " + self.const.MENU)   
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
        Gr = C.permutation_automorphism_group()
        return Gr.order()

        # vrati zoznam automorfizmov dopneny o hrany
    def getPermutationsOfAutomorphisms(self):
        H = self.getParityCheckMatrixFromCage()
        C = self.getLinearCode(H)
        automorphismGroup = C.permutation_automorphism_group().list()
        permutations = []

        graph = Graph(H)
        graph = self.setDefaultVertices(graph)
        graph = self.setDefaultEdges(graph)

        edges=graph.edges()
        automorphism = ""
        for i in range(len(automorphismGroup)):
                if i > 0:
                    for group in automorphismGroup[i]:
                        automorphism += "("
                        for edgesInGroup in group:
                            for edgeInGroup in self.parseEdges(edgesInGroup):
                                for edge in edges:
                                    if str(edge[2]) == str(edgeInGroup):
                                        automorphism +=  str(edge)
                                        continue
                        automorphism += ")" 
                    for edge in edges:
                        if str(edge) not in automorphism:
                            automorphism += '(' + str(edge) + ')'   
                    permutations.append(str(automorphism))
                    automorphism = ""
        return permutations
    
    def parseEdges(self, group):
        return str(group).replace('(', '').replace(')', '').split(",")

        # nastavi vrcholy od 1 po pocet vrcholov pre dany graf
    def setDefaultVertices(self, graph):
        vertices = []
        for vertex in range(len(graph.vertices(sort=False))):
            vertices.append(vertex + 1)
        graph.relabel(vertices)
        return graph

        # nastavi lable pre hrany od 1 po pocet hran pre dany graf
    def setDefaultEdges(self, graph):
        edgeId = 0
        for u,v in graph.edge_iterator(labels=None):
            edgeId += 1
            graph.set_edge_label(u, v, str(edgeId))
        return graph
    
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
        while choice != self.const.OPTION_X:    
            self.display_title_bar()
            print("\t ")
            print('\t  ' + self.const.GENERATOR_MATRIX)
            print("\t ")
            print(str(G) + ' \n')
            if(b):
                print('\t    '+self.const.C_VALID+' \n')
            else:
                print('\t    '+self.const.C_INVALID+' \n')
            choice = self.get_user_choice()
            self.display_title_bar()
            if choice == self.const.OPTION_X:
               break
            else:
                print("\t  " + self.const.OTHER_OPTION + "\n")
    
    # ulozi generujucu maticu
    def saveGeneratorMatrix(self):
        choice = ''
        H = self.getParityCheckMatrixFromCage()
        if not os.path.exists(self.const.GENERATOR_MATRIX_DIRECTORY):
            os.makedirs(self.const.GENERATOR_MATRIX_DIRECTORY)
        startTime = datetime.datetime.now()
        G = self.getGeneratorMatrix(H)
        file = open(self.const.G_DIR_PREFIX+str(self.k)+'_'+str(self.g)+self.const.TEXT_FILE, 'w')
        file.write(str(G))
        time = datetime.datetime.now() - startTime
        file.close()
        while choice != self.const.OPTION_X:    
            self.display_title_bar()
            print("\t ")
            print('\t    '+self.const.G_FILE_PREFIX+str(self.k)+','+str(self.g)+') '+self.const.SUCCESS_CREATE+str(time.total_seconds()) +'s\n')
            choice = self.get_user_choice()  
            self.display_title_bar()
            if choice == self.const.OPTION_X:
                break
            else:
                print("\t  " + self.const.OTHER_OPTION + "\n")
    
    # zobrazi rozmer generujucej matice
    def showDimOfGeneratorMatrix(self):
        choice = ''
        H = self.getParityCheckMatrixFromCage()
        G = self.getGeneratorMatrix(H)
        while choice != self.const.OPTION_X:    
            self.display_title_bar()
            print("\t ")   
            print('\t    ' + self.const.GENERATOR_MATRIX_DIM + " " + str(G.nrows()) +'x'+ str(G.ncols()) + ' \n')
            choice = self.get_user_choice()  
            self.display_title_bar()
            if choice == self.const.OPTION_X:
                break
            else:
                print("\t  " + self.const.OTHER_OPTION + "\n") 
    
    # zobrazi minimalnu vzdialenost kodu          
    def showMinimumDistance(self):
        choice = ''
        H = self.getParityCheckMatrixFromCage()
        d = self.getMinimumDistance(H)  
        while choice != self.const.OPTION_X:    
            self.display_title_bar()
            print("\t ")  
            print('\t    ' + self.const.MIN_CODE_DISTANCE + " " + str(d) + ' \n')
            choice = self.get_user_choice()
            self.display_title_bar()
            if choice == self.const.OPTION_X:
               break
            else:
                print("\t  " + self.const.OTHER_OPTION + "\n")
    
    # zobrazi dlzku kodu a pocet kodovych slov
    def showCodeLengthAndMaxNCodeWords(self):
        choice = ''
        H = self.getParityCheckMatrixFromCage()
        n = self.getCodeLength(H)
        m = self.getMaxNCodewords(H)
        while choice != self.const.OPTION_X:    
            self.display_title_bar()
            print("\t   ")  
            print('\t    ' + self.const.CODE_LENGTH + " " + str(n) + ' \n')
            print('\t    ' + self.const.NUM_CODE_WORDS + " " + str(m) + ' \n')
            choice = self.get_user_choice()
            self.display_title_bar()
            if choice == self.const.OPTION_X:
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
        while choice != self.const.OPTION_X:    
            self.display_title_bar()
            print("\t ")  
            print('\t    ' + self.const.PERFECT_CODE_PARAMETER + " " + str(p) + ' \n')
            choice = self.get_user_choice()
            self.display_title_bar()
            if choice == self.const.OPTION_X:
               break
            else:
                print("\t  " + self.const.OTHER_OPTION + "\n")
    
    # vrati nazov detailu
    def getTitle(self):
        spaceInString = len(str(self.k)) + len(str(self.g))
        title = self.const.LEFT_BORDER
        if self.isCage == TRUE:
            title += self.const.CAGE
            title += "("+str(self.k) +","+str(self.g) +") " + self.const.LINEAR_CODE + " " +  self.const.DETAIL
        else:
            title += self.const.REC
            title += "("+str(self.k) +","+str(self.g) +") " + self.const.LINEAR_CODE + " " +  self.const.DETAIL
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