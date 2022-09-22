__author__ = 'ALVARO'

class Hotel:
    def __init__(self, id=0, name=" ", cost=0.0, deparment=" "):
        self.id=id
        self.name=name
        self.cost=cost
        self.deparment=deparment
#############################################################
class Vertice:
    def __init__(self, value=None):
        self.value = value
        self.node = []
    
    def pushNode(self, node=None):
        if node!= None:
            self.node.append(node)
        else:
            return
    
    def printNodes(self):
        for i in range(len(self.node)):
            print(self.node[i])
#############################################################
class Grafo:
    def __init__(self):
        self.vertices = []
    
    def pushVertice(self, value):
        if value.name not in self.vertices or len(self.vertices) < 1:
            self.vertices.append(Vertice(value))

    def readDocument(self, path):
        fh = open(path)
        lines = fh.readline()
        for line in lines:
            line = line.rstrip()
            line = line.split(',')
            self.pushVertice(Hotel(line[0], line[1], float(line[2]), line[3]))

    
def main():
    g = Grafo()
    
    print("d")


###############################################################



main()





