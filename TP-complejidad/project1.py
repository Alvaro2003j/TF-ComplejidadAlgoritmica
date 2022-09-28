__author__ = 'ALVARO'

class Hotel:
    def __init__(self, nombre=" ", cost=0.0,departamento=" ", vecino=" "):
        self.nombre=nombre
        self.cost=cost
        self.departamento=departamento
        self.vecino=vecino

class Node:
    def __init__(self, id=0, name=" ", cost=0.0, departamento=" ", vecino=" "):
        self.id=id
        self.value=Hotel(name, cost, departamento, vecino)
        self.visited=False
        self.nodes={}

    def pushEdge(self, node:Hotel):
        self.nodes[node.name] = node

class Grafo:
    def __init__(self):
        self.Nodes=[]
        self.deparments = {"Lima": {}, "Cuzco": {}, "Huancayo": {}} #Grafo
    
    def pushNode(self, value:Node):
        if value.value.nombre != " ":
            self.Nodes.append(value)
        else:
            return
        
    def DesignGraph(self):
        #Adicionando los nodos a los departamentos
        for node in self.Nodes:
            if node.value.vecino == "N":
                if node is not self.deparments[node.value.departamento]:
                    self.deparments[node.value.departamento][node.value.nombre] = node  
                else:
                    continue
            else:
                continue
        #Adicionando los nodos a los hoteles
        for node in self.Nodes:
            if node.value.vecino != "N":
                #if node is not self.deparments[node.value.departemento][node.value.]:
                if node is not self.deparments[node.value.departamento][node.value.vecino] or len(self.deparments[node.value.departamento][node.value.vecino].nodes) <= 0:
                    self.deparments[node.value.departamento][node.value.vecino].nodes[node.value.nombre] = node
    #Limpiadores
    def ClearGraph(self):
        self.deparments.clear()
    
    def ClearNodes(self):
        self.Nodes.clear()

    def printGraph(self, depart=" "):
        print("List of " + depart)
        for v in self.deparments[depart]:
            print(v)
            if len(self.deparments[depart][v].nodes) > 0:
                for x in self.deparments[depart][v].nodes:
                    print(x)
    
    def PrintGrafo(self):
        self.printGraph("Lima")
        self.printGraph("Cuzco")
        self.printGraph("Huancayo")
######################################################################################################
                    #####Main####

path = "external/tp.csv"
file = open(path)
lines = file.readlines()
g=Grafo()
file.close()
for line in lines:
    line = line.rstrip()
    line = line.split(',')
    line[0] = int(line[0])
    line[2] = float(line[2])
    #creación de mis lista de nodos
    tmp = Node(line[0], line[1], line[2], line[3], line[4])
    print(tmp.id, tmp.value.cost, tmp.value.nombre, tmp.value.departamento, tmp.value.vecino)
    g.pushNode(tmp)

for node in g.Nodes:
    print(node)
#Creando uniones entre departamentos con hoteles
g.DesignGraph()
g.PrintGrafo()