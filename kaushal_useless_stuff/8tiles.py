import math

def getBlank(block):

    keys = block.keys()

    for i in keys:
        if(block[i] == 0):
            return i


def generateChildren(block):
    possiblities = []

    blank = getBlank(block)
    

    ## ruless
    swaps = []

    if (blank%3 == 0): ## if the blank is at end
        swaps = [blank-1, blank+3, blank-3]
    elif((blank-1) % 3 == 0): ## if the blank is at beginning
        swaps = [blank+1, blank+3, blank-3]
    else: ## if the blank is at beginning
        swaps = [blank+1, blank-1, blank+3, blank-3]

 
    for i in swaps:
        
        try:
            temp = {}
            temp.update(block)
            temp[i], temp[blank] = temp[blank], temp[i]
            if(temp not in selectedChildren):
                possiblities.append(temp)
        except:
            pass
    
    return possiblities


def printblocks(children):
    for child in children:
        
        for i in range(1,10,3):
            for j in range(3):
                print(child[i+j], end = " ")
            print()

        print()

def getHeuristicValue(children):
    heuristic = []
    for child in children:
        hstic = 0
        for i in range(1,10):
            if(child[i] != goal[i]):
                hstic+=1
            else:
                hstic+=0
                continue
            
            if(i%3 == 0): ## if the current val is at end
                if(child[i] == goal[i-1]):
                    hstic+=1
                    continue
                try:
                    if(child[i] == goal[i+3]):
                        hstic+=1
                        continue
                except:
                    pass

                try:
                    if(child[i] == goal[i-3]):
                        hstic+=1
                        continue
                except:
                    pass
            
            elif((i-1)%3 == 0): ## if current val is at beg
                if(child[i] == goal[i+1]):
                    hstic+=1
                    continue
                try:
                    if(child[i] == goal[i+3]):
                        hstic+=1
                        continue
                except:
                    pass
                try:
                    if(child[i] == goal[i-3]):
                        hstic+=1
                        continue
                except:
                    pass
            
            else:
                if(child[i] == goal[i-1]):
                    hstic+=1
                    continue
                if(child[i] == goal[i+1]):
                    hstic+=1
                    continue                
                try:
                    if(child[i] == goal[i+3]):
                        hstic+=1
                        continue
                except:
                    pass
                try:
                    if(child[i] == goal[i-3]):
                        hstic+=1
                        continue
                except:
                    pass
            
            hstic+=3




            
        heuristic.append([child,hstic])


    lestChild = None
    leasthstc = math.inf

    for record in heuristic:
        if(record[1] < leasthstc):
            leasthstc = record[1]
            lestChild = record[0]
    
    return (heuristic, lestChild)



# initial = {1:2, 2:1, 3:3, 4:4, 5:6, 6:0, 7:5, 8:7, 9:8}
initial = {1:1, 2:0, 3:3, 4:4, 5:2, 6:6, 7:7, 8:5, 9:8}
goal = {1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:0}

counter = 0
selectedChildren = [initial]
while (initial != goal):

    if(counter == 15):
        break
    print("initial:: ")
    printblocks([initial])
    poss = generateChildren(initial)
    print(" children ")

    printblocks(poss)

    hstcChild = getHeuristicValue(poss)
    selectedChildren.append(hstcChild[1])
    print("selected:: ")
    printblocks([hstcChild[1]])
    initial = hstcChild[1]
    print()
    counter+=1
    