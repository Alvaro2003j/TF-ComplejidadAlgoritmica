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
        self.deparments = {"Lima": [], "Cuzco": [], "Huancayo": []}
        #self.G=[]
    
    def pushNode(self, value:Node):
        self.Nodes.append(value)
    
    def DesignGraf(self):
        #Adicionando los nodos a los departamentos
        for node in self.Nodes:
            if node.value.vecino == "N":
                if node is not self.deparments[node.value.departamento]:
                    self.deparments[node.value.departamento].append(node)
                else:
                    continue
            else:
                continue
        #Adicionando los nodos a los hoteles
        for node in self.Nodes:
            if node.value.vecino != "N":
                





def main():
    path = "text/tp.csv"
    file = open(path)
    lines = file.readlines()
    g=Grafo()

    for line in lines:
        line = line.rstrip()
        line = line.split(',')
        
        #Creando uniones entre departamentos con hoteles
        






