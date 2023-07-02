graph={
    '5':['3','7'],
    '3':['2','4'],
    '7':['8'],
    '2':[],
    '4':['8'],
    '8':[]
}
#BFS-we use Queue
visited=[]#List for visited nodes
queue=[] #Initialize a queue
def bfs(visited,graph,node):
    visited.append(node)
    queue.append(node)

    while queue:            #Creating loop to visit elements
        m=queue.pop(0)
        print(m,end=" ")

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
                
bfs(visited,graph,'5')          #function call     
