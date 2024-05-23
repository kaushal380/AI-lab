import math
# tree = {
#     'A': ['B', 'C'],
#     'B': ['D', 'E'],
#     'C': ['F', 'G'],
#     'D': [1,4],
#     'E': [7,2],
#     'F': [3,0],
#     'G': [6,5]
# }
tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [2,3],
    'E': [5,4],
    'F': [0,1],
    'G': [7,5]
}
# [3, 5, 6, 9, 1, 2, 0, -1]

def gameSearch(root, tree, alpha = (-1*math.inf), beta = math.inf,maximizing = True):
    # print(alpha, beta)

    if(maximizing):
        
        children = tree[root]
        
        try:
            
            mx = max(max(list(map(int, children))),alpha)
            if(mx >= beta):

                return alpha, beta, True
            
            return mx,beta, False
        except:
            pass
        
        alpha1, beta1 = alpha, beta
        for child in children:
            # print(child)
            alpha1, beta1, pruned = gameSearch(child, tree, alpha=alpha1, beta=beta1,maximizing=False)
            # print(alpha1, beta1)
            if(pruned):
                return alpha1, beta1, False
            alpha1 = beta1
            beta1 = beta
            if(alpha1>=beta1):
                return alpha, beta, True

            
        
        
        return alpha1,beta1, False
    
    else:
        children = tree[root]
        try:
            
            min = min(min(list(map(int, children))), beta)

            return alpha,min
        except:
            pass
        
        alpha1, beta1 = alpha, beta

        for child in children:

            alpha1, beta1, pruned = gameSearch(child, tree, alpha=alpha1, beta=beta1,maximizing=True)
            
            if(pruned):
                return alpha1, beta1, False
            beta1 = alpha1
            alpha1=alpha
            if(alpha1>=beta1):
                return alpha, beta, True


        
        # print(alpha1, beta1)
        return alpha1,beta1,False


optimalVal = gameSearch('A', tree)
print(optimalVal[0])