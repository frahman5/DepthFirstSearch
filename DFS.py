class Vertex(object):
    """
    A vertex on a graph.
    """
    def __init__(self,name,explored=0,edges=[]):
        """
        name: integer >= 0
        explored: Int, reflecting the number of times a vertex has been explored
        edges: ListOfIntegers, where the Integers are Names of other vertices
        """
        self.name = name
        self.explored = explored
        self.edges = edges
        self.leader = 0

    def getName(self):
        return self.name

    def getExplored(self):
        return self.explored
        
    def addExplored(self,explored):
        self.explored = self.explored + 1

    def getEdges(self):
        return self.edges

    def replaceEdges(self,newEdges):
        self.edges = newEdges

class Graph(object):
    """
    A Graph object, represented by an adjacency list
    """
    def __init__(self,text):
        """
        text: str. The location of the plaintext representation of
        the directed graph
        """
        assert type(text) == str
        self.numVertices, self.graph = getDirGraph(text)
        self.vertices = []
        for i in range(0,self.numVertices):
            self.vertices.append(Vertex(i+1,0,self.graph[i]))

    def getGraph(self):
        return self.graph

    def getVertices(self):
        return self.vertices

    def getNumVertices(self):
        return self.numVertices

    def setGraph(self,newGraph):
        """
        replace the current adjacency list representation of the graph
        with a new one
        """
        self.graph = newGraph

    def setVertsFalse(self):
        for i in range(0,self.numVertices):
            self.vertices[i].explored = 0

    def selfReverse(self):
        """
        Reverse the direction of all edges in self and initalizes all vertices as unexplored
        -> Changes self.graph to reflect the new adjacency list
        -> Updates each individual vertex in self.vertices to
        represent their new edges
        """
        newGraph = []
        for i in range(0,self.getNumVertices()):
            newGraph.append([])
        for i in range(0,self.getNumVertices()):
            for j in self.getGraph()[i]:
                newGraph[j-1].append(i+1)
        for i in range(0,self.getNumVertices()):
            self.getVertices()[i].replaceEdges(newGraph[i])
        self.setGraph(newGraph)
        self.setVertsFalse()
        return self
    
def getDirGraph(text):
    """
    str -> Integer[>=0} List
    text: a str representing the location of a plain text representation
          of a directed graph
    Output: Number of nodges n in the graph
            An adjacency list that represents the directed Graph
    Assumes: 1) The vertices are labeled 1 2 ... n
             2) Vertex n is not a sink
    """
    answer = []
    line_number = 0
    len_answer = 0
    with open(text,encoding = 'utf-8') as file:             #get the file
        for a_line in file:
            if '\n' in a_line:                              #remove the \n
                edited_line = a_line[:len(a_line)-1]
            else:
                edited_line = a_line
            edited_line = edited_line.split()               #split it into a list
            from_edge = int(edited_line[0])
            to_edge = int(edited_line[1])
            try:                                            #try to add to the adjacency list
                answer[from_edge-1].append(to_edge)         
            except(IndexError):                             #if list not long enough, extend then add
                for i in range(len_answer,from_edge):
                    answer.append([])
                answer[from_edge-1].append(to_edge)
                len_answer = from_edge                      #update len_graph without having to scan the graph
            line_number += 1
    return len_answer,answer

def DFS(G,s,calcFinishingTime=True,setLeaders=True):
    """
    Graph Integer -> Graph
    G: Graph object
    s: Integer[>=0]; name of a vertex in G at which to start search
    Output: graph G, with all vertices explored
    """
    stack = [G.getVertices()[s-1]]
    if calcFinishingTime:                                   #Calculate the Finishing Times of the vertices
        DFS_cFT(G,stack)
    if setLeaders:                                          #Find the sizes of the strongly connected componenets
        DFS_sL(G,stack,l)                     
    return G


def DFS_cFT(G,stack):
    """
    Graph Integer -> Graph
    G: Graph object
    stack: Stack (a list), passed from parent DFS function
    Produces the graph G, with all vertices explored, while also calculating finishing times for FindSCCs
    """
    global t
    while not stack == []:
        u = stack[-1]
        explore_value = u.getExplored()
        if explore_value == 1:
            finisher = stack.pop()
            finisher.addExplored(1)
            t += 1
            finishingTimes[t] = finisher.getName()
        elif explore_value > 1:
            stack.pop()
        else:
            u.addExplored(1)                                #We consider a vertex explored if it has added its edges to the stack
            for to_vertex in u.getEdges():
                w = G.getVertices()[to_vertex-1]
                if (w.getExplored() == 0):
                    stack.append(w)
                    
def DFS_sL(G,stack,l):
    """
    Graph Integer -> Graph
    G: Graph object
    stack: Stack (a list), passed from parent DFS function
    Produces the graph G, with all vertices explored, while also calculating the SCCs of a leader l
    """
    leaders[l] = 1
    while not stack == []:
        u = stack.pop()
        u.addExplored(1)
        for to_vertex in u.getEdges():
            w = G.getVertices()[to_vertex-1]
            if (w.getExplored() == 0):
                w.addExplored(1)
                stack.append(w)
                leaders[l] = leaders[l] + 1
                
def FindSCCs(G):
    """
    Graph -> ListOfIntegers
    Produces the size, in decreasing order, of the
    Strongly Connected Components of G
    """
    G.selfReverse()                                         #Reverse the edges in G + initalize edges as unexplored
    global t                                                #Number of nodes processed so far
    global finishingTimes                                   #dictionary to keep track of node finishing times
    global l                                                #Current Source Vertex (called leader)
    global leaders                                          #Keeps track of how much nodes are strongly connected to a leader
    t = 0
    finishingTimes = {}
    l = None
    leaders = {}
    limit = G.getNumVertices()
    for i in reversed(range(0,limit)):                      #Calculate the finishing time for each vertex
        if G.getVertices()[i].getExplored() == 0:
            DFS(G,i+1,True,False)                           
    G.selfReverse()                                         #Restore the edges in G to their original order + reset them as unexplored
    for i in reversed(range(1,limit+1)):                    #Calculate the sizes of the strongly connected components in G
        l = finishingTimes[i]                               
        if G.getVertices()[l-1].getExplored() == 0:
            DFS(G,l,False,True)
    answer = list(leaders.values())
    answer.sort(reverse=True)
    return answer


