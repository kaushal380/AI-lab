import math

### intializing Astar taking source and destination as 
def Astaralgo(src, dest):
    ### initializing open list with source node
    openList = {src: heuristic(src)}

    ### initializing an empty closed node
    closedList = {}

    ### looping till open list is empty
    while len(openList) > 0:

        ### finding the minimum path in the current openList
        min = math.inf
        minPath = ""
        for i in openList:
            if(openList[i] < min):
                min = openList[i]
                minPath = i

        ### if goal state is acheived at a minimum cost already, return the path
        if(minPath[-1] == dest):
            print("final path is: ")
            print(minPath)
            print("the cost took:")
            print(min)
            return

        ### exploring the end node and expanding it's children by finding the cost        
        nodes = Graph_nodes[minPath[-1]]
        for node in nodes:
            str = minPath+node[0]

            costVal = 0
            for i in range(1,len(str)):
                prev = str[i-1]
                curr = str[i]

                upcomingNodes = Graph_nodes[prev]
                
                for n in upcomingNodes:
                    if(curr == n[0]):
                        costVal+=n[1]
            costVal+=heuristic(str[-1])

            openList.update({str:costVal})
        
        closedList.update({minPath: min})
        openList.pop(minPath)



    print("no path exists")
    return


### giving the heuristic values
def heuristic(n):
    H_dist = { 'A': 11,
    'B': 6,
    'C': 99,
    'D': 1,
    'E': 7,
    'G': 0,
    }
    return H_dist[n] 

### creating a graph
Graph_nodes = { 'A': [('B', 2), ('E', 3)],
'B': [('C', 1),('G', 9)],
'C': [('A', 10)], 
'E': [('D', 6)],
'D': [('G', 1)],
}

### calling Astar algo
Astaralgo('A', 'G')