from const import Constants
from sage.all import *

class Cage:
    const = Constants()
    def __init__(self, k, g):
        self.k = k
        self.g = g
    
  # sledujeme 3 zoznamy uvazovanych klietok s ktorymi porovnavame parametre, pre kazdy zoznam sa grafy generuju inym sposobom
    def getCage(self):
        sageCages = [[3,5], [3,6], [3,7], [3,8], [3,10], [3,11], [4,5], [7,5]]
        exoosCages = [[3,14], [3,16], [3,17], [3,18], [3,20], [3,23], [3,25], [4,7], [4,9], [4,10], [5,10], [7,7], [7,8], [10,5], [11,5], [12,5], [13,5]]
        myConstructedCages = [[6,4]]

        cageInput =[]
        cageInput.append(self.k)
        cageInput.append(self.g)

        if ((cageInput in sageCages) == False and (cageInput in exoosCages) == False and (cageInput in myConstructedCages) == False):
            print("\n")
            print( self.const.CAGE_NON_EXIST+"\n")
            return
        cage = graphs.EmptyGraph();
        if cageInput in sageCages:
            if self.k == 3:
                if self.g == 5:
                    cage = graphs.PetersenGraph()
                if self.g == 6:
                    cage = graphs.HeawoodGraph()
                if self.g == 7:
                    cage = graphs.McGeeGraph()
                if self.g == 8:
                    cage = graphs.TutteCoxeterGraph()
                if self.g == 10:
                    cage = graphs.Balaban10Cage()
                if self.g == 11:
                    cage = graphs.Balaban11Cage()
            if self.k == 4 and self.g == 5:
                cage = graphs.RobertsonGraph()
            if self.k == 7 and self.g == 5:
                cage = graphs.HoffmanSingletonGraph()
        elif cageInput in exoosCages:
            cage = self.generateGraphandCageFromExoosAdjacencylist(self.const.EXOOS_CAGE_PREFIX + str(self.k) + "_"+str(self.g) + self.const.TEXT_FILE)
        elif cageInput in myConstructedCages:
            if self.k == 6 and self.g == 4:
                cage = self.generate_6_4CageGraph()
        if (self.cageVerification(cage) == False):
           print(self.const.NO_CAGE + "\n")
           return
        cage = self.setNonZeroVerticesLabels(cage)
        return cage

    # nastavi vrcholy od 1 po pocet vrcholov pre danu klietku
    def setNonZeroVerticesLabels(self, cage):
        vertices = []
        for vertex in range(len(cage.vertices(sort=False))):
            vertices.append(vertex + 1)
        cage.relabel(vertices)
        return cage

    # vrati zoznam automorfizmov
    def getPermutationsOfAutomorphisms(self, cage):
        vertices = cage.vertices()
        automorphismGroup = cage.automorphism_group().list()
        permutations = []
        for i in range(len(automorphismGroup)):
                if i > 0:
                    automorphism = str(automorphismGroup[i])
                    for vertex in vertices:
                        if str(vertex) not in automorphism:
                            automorphism += '(' + str(vertex) + ')';
                    permutations.append(str(automorphism))
        return permutations

    # vypocita najmensi mozny pocet vrcholov pre potencionalnu klietku (testovacie data)
    def calculateMooreBound(self):
        M = 0
        exp = 0
        if self.g % 2 == 1:
            exp = (self.g - 3) / 2
            for i in range(int(exp) + 1):
                M = M + (self.k * ((self.k - 1) ** i))
            M = M + 1
        else:
            exp = (self.g - 2)/2
            for i in range(int(exp) + 1):
                M = M + ((self.k - 1) ** i)
            M = 2 * M
        return M
    
    # vygeneruje Cage(6,4), bez vstupnych parametrov ako bipartitny graf - individualny pristup
    def generate_6_4CageGraph(self):
        self.k = 6
        self.g = 4
        M = self.calculateMooreBound()
        s =[]
        for i in range(int(M/2)):
            s.append(6)
        graph = graphs.DegreeSequenceBipartite(s,s)
        for i in range (M):
            graph.set_vertex(i, str(i))
        graph.name(self.const.CAGE_64)
        return graph

    # vypocita informacny pomer z matice H
    def getRate(self,nRows, nCols):
        return (nCols - nRows) / nCols

    # odstranenie hodnot zo zoznamu na zaklade hodnoty
    def remove_values_from_list(self,the_list, val):
        return [value for value in the_list if value != val]

    # parsovanie Exoo dokumentov so zoznamami susednych vrcholov na generovanie grafu
    def generateGraphandCageFromExoosAdjacencylist(self,filePath):
        file = open(filePath, "r")
        graph = graphs.EmptyGraph()
        mainVertex = 0
        for line in file:
            line = line.replace('\n', '')
            adjacencyVerticies = line.split(" ")
            adjacencyVerticies = self.remove_values_from_list(adjacencyVerticies, '')
            for adjacencyVertex in adjacencyVerticies:
                graph.add_edge(mainVertex, int(adjacencyVertex))
            mainVertex += 1
        file.close()
        return graph
    
    # vypocita potencionalny pocet hran na zaklade Moorovho ohranicenia (testovacie data)
    def numberOfEdgesByMooreBound(self,M):
        return M * self.k / 2

    # test vysledkov
    def cageVerification(self,cage):
        M = self.calculateMooreBound()
        minPocetHran = self.numberOfEdgesByMooreBound(M)
    #     verifikacia poctu vrcholov
        if len(cage.vertices()) < M or len(cage.incidence_matrix().column(0)) < M:
            return False
    #     verifikacia poctu hran
        if len(cage.edges()) < minPocetHran or len(cage.incidence_matrix().row(0)) < minPocetHran:
            return False
        return True

    # vrati kontrolnu maticu linearneho kodu ako incidencnu maticu klietky ziskanu z grafu nad polom Z2
    def getParityCheckMatrix(self,graph):
        return matrix(GF(2), graph.incidence_matrix())