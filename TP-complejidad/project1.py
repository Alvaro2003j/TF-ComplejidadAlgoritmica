class Vertice:
    def __init__(self, id=0, value=None):
        self.id = id
        self.value = value
        self.node = []
    
    def pushNode(self, node=None):
        if node!= None:
            node.append(node)
        else:
            return
    
    def printNodes(self):
        for v in range(len(self.node)):
            print(self.node.id)




class Hotel:
    def __init__(self, id=0, name=" ", deparment=" "):
        self.id=id
        self.name=name
        self.deparment=deparment