tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [2,3],
    'E': [5,4],
    'F': [0,1],
    'G': [7,5]
    
}
# tree = {
#     'A': ['B', 'C'],
#     'B': ['D', 'E'],
#     'C': ['F', 'G'],
#     'D': [1,4],
#     'E': [7,2],
#     'F': [3,0],
#     'G': [6,5]
# }



def gameSearch(root, tree,maximizing = True):
    
    if(maximizing):
        
        max_nodes = []
        children = tree[root]

        try:

            mx = max(list(map(int, children)))
            return mx
        except:
            pass
        
        for child in children:
            max_nodes.append(gameSearch(child, tree, maximizing=False))
        
        return max(max_nodes)
    
    else:
        min_nodes = []
        children = tree[root]
        try:
            mn = min(list(map(int, children)))
            return mn
        except:
            pass
        for child in children:
            min_nodes.append(gameSearch(child, tree, maximizing=True))
        
        return min(min_nodes)


optimalVal = gameSearch('A', tree, maximizing=True)
print("optimal value is: ", optimalVal)