# # Python3 program to print the path from root 
# # node to destination node for N*N-1 puzzle 
# # algorithm using Branch and Bound
# # The solution assumes that instance of 
# # puzzle is solvable

# # Importing copy for deepcopy function
# import copy

# # Importing the heap functions from python 
# # library for Priority Queue
# from heapq import heappush, heappop

# # This variable can be changed to change
# # the program from 8 puzzle(n=3) to 15 
# # puzzle(n=4) to 24 puzzle(n=5)...
# n = 3

# # bottom, left, top, right
# row = [ 1, 0, -1, 0 ]
# col = [ 0, -1, 0, 1 ]

# # A class for Priority Queue
# class priorityQueue:
	
# 	# Constructor to initialize a
# 	# Priority Queue
# 	def __init__(self):
# 		self.heap = []

# 	# Inserts a new key 'k'
# 	def push(self, k):
# 		heappush(self.heap, k)

# 	# Method to remove minimum element 
# 	# from Priority Queue
# 	def pop(self):
# 		return heappop(self.heap)

# 	# Method to know if the Queue is empty
# 	def empty(self):
# 		if not self.heap:
# 			return True
# 		else:
# 			return False

# # Node structure
# class node:
	
# 	def __init__(self, parent, mat, empty_tile_pos,
# 				cost, level):
					
# 		# Stores the parent node of the 
# 		# current node helps in tracing 
# 		# path when the answer is found
# 		self.parent = parent

# 		# Stores the matrix
# 		self.mat = mat

# 		# Stores the position at which the
# 		# empty space tile exists in the matrix
# 		self.empty_tile_pos = empty_tile_pos

# 		# Stores the number of misplaced tiles
# 		self.cost = cost

# 		# Stores the number of moves so far
# 		self.level = level

# 	# This method is defined so that the 
# 	# priority queue is formed based on 
# 	# the cost variable of the objects
# 	def __lt__(self, nxt):
# 		return self.cost < nxt.cost

# # Function to calculate the number of 
# # misplaced tiles ie. number of non-blank
# # tiles not in their goal position
# def calculateCost(mat, final) -> int:
	
# 	count = 0
# 	for i in range(n):
# 		for j in range(n):
# 			if ((mat[i][j]) and
# 				(mat[i][j] != final[i][j])):
# 				count += 1
				
# 	return count

# def newNode(mat, empty_tile_pos, new_empty_tile_pos,
# 			level, parent, final) -> node:
				
# 	# Copy data from parent matrix to current matrix
# 	new_mat = copy.deepcopy(mat)

# 	# Move tile by 1 position
# 	x1 = empty_tile_pos[0]
# 	y1 = empty_tile_pos[1]
# 	x2 = new_empty_tile_pos[0]
# 	y2 = new_empty_tile_pos[1]
# 	new_mat[x1][y1], new_mat[x2][y2] = new_mat[x2][y2], new_mat[x1][y1]

# 	# Set number of misplaced tiles
# 	cost = calculateCost(new_mat, final)

# 	new_node = node(parent, new_mat, new_empty_tile_pos,
# 					cost, level)
# 	return new_node

# # Function to print the N x N matrix
# def printMatrix(mat):
	
# 	for i in range(n):
# 		for j in range(n):
# 			print("%d " % (mat[i][j]), end = " ")
			
# 		print()

# # Function to check if (x, y) is a valid
# # matrix coordinate
# def isSafe(x, y):
	
# 	return x >= 0 and x < n and y >= 0 and y < n

# # Print path from root node to destination node
# def printPath(root):
	
# 	if root == None:
# 		return
	
# 	printPath(root.parent)
# 	printMatrix(root.mat)
# 	print()

# # Function to solve N*N - 1 puzzle algorithm
# # using Branch and Bound. empty_tile_pos is
# # the blank tile position in the initial state.
# def solve(initial, empty_tile_pos, final):
	
# 	# Create a priority queue to store live
# 	# nodes of search tree
# 	pq = priorityQueue()

# 	# Create the root node
# 	cost = calculateCost(initial, final)
# 	root = node(None, initial, 
# 				empty_tile_pos, cost, 0)

# 	# Add root to list of live nodes
# 	pq.push(root)

# 	# Finds a live node with least cost,
# 	# add its children to list of live 
# 	# nodes and finally deletes it from 
# 	# the list.
# 	while not pq.empty():

# 		# Find a live node with least estimated
# 		# cost and delete it from the list of 
# 		# live nodes
# 		minimum = pq.pop()

# 		# If minimum is the answer node
# 		if minimum.cost == 0:
			
# 			# Print the path from root to
# 			# destination;
# 			printPath(minimum)
# 			return

# 		# Generate all possible children
# 		for i in range(4):
# 			new_tile_pos = [
# 				minimum.empty_tile_pos[0] + row[i],
# 				minimum.empty_tile_pos[1] + col[i], ]
				
# 			if isSafe(new_tile_pos[0], new_tile_pos[1]):
				
# 				# Create a child node
# 				child = newNode(minimum.mat,
# 								minimum.empty_tile_pos,
# 								new_tile_pos,
# 								minimum.level + 1,
# 								minimum, final,)

# 				# Add child to list of live nodes
# 				pq.push(child)

# # Driver Code

# # Initial configuration
# # Value 0 is used for empty space
# initial = [ [ 1, 2, 3 ], 
# 			[ 5, 6, 0 ], 
# 			[ 7, 8, 4 ] ]

# # Solvable Final configuration
# # Value 0 is used for empty space
# final = [ [ 1, 2, 3 ], 
# 		[ 4, 5, 6 ], 
# 		[ 7, 8, 0 ] ]

# # Blank tile coordinates in 
# # initial configuration
# empty_tile_pos = [ 1, 2 ]

# # Function call to solve the puzzle
# solve(initial, empty_tile_pos, final)

# # This code is contributed by Kevin Joshi




import heapq
import numpy as np

class PuzzleNode:
    def __init__(self, state, parent=None, cost=0):
        self.state = state
        self.parent = parent
        self.cost = cost
        self.heuristic = self.manhattan_distance()

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

    def manhattan_distance(self):
        goal_state = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
        distance = 0
        for i in range(3):
            for j in range(3):
                if self.state[i][j] != 0:
                    goal_position = np.where(goal_state == self.state[i][j])
                    distance += abs(i - goal_position[0][0]) + abs(j - goal_position[1][0])
        return distance

    def generate_successors(self):
        successors = []
        zero_position = np.where(self.state == 0)
        zero_row, zero_col = zero_position[0][0], zero_position[1][0]
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # right, left, down, up
        for move in moves:
            new_row, new_col = zero_row + move[0], zero_col + move[1]
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_state = self.state.copy()
                new_state[zero_row][zero_col], new_state[new_row][new_col] = new_state[new_row][new_col], 0
                successors.append(PuzzleNode(new_state, self, self.cost + 1))
        return successors

def a_star(initial_state):
    initial_node = PuzzleNode(initial_state)
    open_list = [initial_node]
    closed_list = set()

    while open_list:
        current_node = heapq.heappop(open_list)
        if np.array_equal(current_node.state, np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])):
            return get_solution_path(current_node)
        closed_list.add(tuple(map(tuple, current_node.state)))
        successors = current_node.generate_successors()
        for successor in successors:
            if tuple(map(tuple, successor.state)) not in closed_list:
                heapq.heappush(open_list, successor)
    return None  # No solution found

def get_solution_path(node):
    path = []
    while node:
        path.append(node.state)
        node = node.parent
    return path[::-1]

# Example usage:
initial_state = np.array([[1, 0, 3], [4, 2, 5], [6, 7, 8]])
solution_path = a_star(initial_state)
if solution_path:
    print("Solution found!")
    for i, state in enumerate(solution_path):
        print(f"Step {i}:")
        print(state)
else:
    print("No solution found for the given initial state.")
