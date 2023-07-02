#import dictionary for graph
from collections import defaultdict

#ADD EDGE TO GRAPG - FUNCTION
graph = defaultdict(list)
def addEdge(graph,u,v):
    graph[u].append(v)
#FUNCTION DESCRIPITION
def generate_edges(graph):
    edges=[]
    #For each node in graph
    for node in graph:
        #For each neighbour node of a single node
        for neighbour in graph[node]:
            #if edge exists then append
            edges.append((node,neighbour))
    return edges
#Declaring-graph as dictionary
addEdge(graph,'a','c')
addEdge(graph,'b','c')
addEdge(graph,'b','e')
addEdge(graph,'c','d')
addEdge(graph,'c','e')
addEdge(graph,'c','a')
addEdge(graph,'c','b')
addEdge(graph,'e','b')
addEdge(graph,'d','c')
addEdge(graph,'e','c')
#PRINTING GRAPH
print(generate_edges(graph))

















