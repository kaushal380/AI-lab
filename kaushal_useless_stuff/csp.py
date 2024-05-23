from simpleai.search import CspProblem, backtrack 


def constraint_function(names, values):

    for i in range(0, len(values)-1):
        for j in range(i+1, len(values)):
            if(values[i] == values[j]):
                return False
    
    return True

colorList = ['Red',	'Green', 'White', 'Blue','Orange','Black','Yellow','Purple','Silver','Brown','Gray','Pink','Olive',	'Maroon','Violet','Charcoal','Magenta','Bronze','Cream','Gold','Tan','Teal','Mustard','Navy Blue']

graph = {
    'a': ['b', 'd'],
    'b':['e','c', 'a'],
    'c': ['b', 'd'],
    'd': ['a','c'],
    'e': ['b']
}

verteces = graph.keys()
colors = dict((vertex, colorList) for vertex in verteces)



def formConstraints():
    constraints = []
    for vertex in verteces:
        
        cords = graph[vertex]

        vertixList = [vertex] + cords

        tup = tuple(vertixList)
        valToappend = (tup, constraint_function)
        constraints.append(valToappend)

    return constraints

constraints = formConstraints()

problem = CspProblem(verteces, colors, constraints) 
output = backtrack(problem)

print("graph vertices: ", list(verteces))
for i in output.keys():
    val = output[i]
    print(i, " ==> ", val)