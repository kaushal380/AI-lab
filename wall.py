import numpy as np

# Define the grid world with walls represented by -1, goal state by +10, penalty state by -10
grid_world = np.array([
    [0, 0, 0, 0, -1],
    [0, -1, 0, 0, -1],
    [0, 0, 0, 0, -1],
    [0, -1, -1, 0, 10],
    [0, 0, 0, 0, -10]
])

# Define the actions: 0=up, 1=down, 2=left, 3=right
actions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

def is_valid_state(state, grid_world):
    """
    Check if the state is valid within the grid world.
    """
    rows, cols = grid_world.shape
    x, y = state
    return 0 <= x < rows and 0 <= y < cols and grid_world[x, y] != -1

def get_possible_states(state, action, grid_world):
    """
    Get possible next states and corresponding probabilities for a given action in a given state.
    """
    possible_states = []
    rows, cols = grid_world.shape
    for dx, dy in actions:
        new_x, new_y = state[0] + dx, state[1] + dy
        if is_valid_state((new_x, new_y), grid_world):
            possible_states.append(((new_x, new_y), 0.8 if (dx, dy) == action else 0.1))
        else:
            possible_states.append((state, 0.8 if (dx, dy) == action else 0.1))
    return possible_states

def value_iteration(grid_world, gamma=0.9, theta=1e-5):
    """
    Value Iteration Algorithm to solve MDP for the given grid world.
    
    :param grid_world: Grid world representation.
    :param gamma: Discount factor.
    :param theta: Convergence threshold.
    :return: Optimal value function, Optimal policy
    """
    num_rows, num_cols = grid_world.shape
    num_states = num_rows * num_cols

    # Initialize value function
    V = np.zeros((num_rows, num_cols))

    while True:
        delta = 0
        for i in range(num_rows):
            for j in range(num_cols):
                v = V[i, j]
                if grid_world[i, j] in [10, -10]:
                    continue
                max_q = -np.inf
                for action_index, action in enumerate(actions):
                    possible_states = get_possible_states((i, j), action, grid_world)
                    q_value = sum(prob * (grid_world[new_i, new_j] + gamma * V[new_i, new_j]) for ((new_i, new_j), prob) in possible_states)
                    max_q = max(max_q, q_value)
                V[i, j] = max_q
                delta = max(delta, np.abs(v - V[i, j]))
        if delta < theta:
            break

    # Extract policy
    policy = np.zeros((num_rows, num_cols), dtype=np.int)
    for i in range(num_rows):
        for j in range(num_cols):
            if grid_world[i, j] in [10, -10]:
                continue
            max_q = -np.inf
            best_action = None
            for action_index, action in enumerate(actions):
                possible_states = get_possible_states((i, j), action, grid_world)
                q_value = sum(prob * (grid_world[new_i, new_j] + gamma * V[new_i, new_j]) for ((new_i, new_j), prob) in possible_states)
                if q_value > max_q:
                    max_q = q_value
                    best_action = action_index
            policy[i, j] = best_action

    return V, policy

# Solve the MDP for the grid world
optimal_value_function, optimal_policy = value_iteration(grid_world)
print("Optimal value function:")
print(optimal_value_function)
print("\nOptimal policy (0=up, 1=down, 2=left, 3=right):")
print(optimal_policy)
