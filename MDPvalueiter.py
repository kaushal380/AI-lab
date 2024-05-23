import numpy as np

def value_iteration(transitions, rewards, gamma=0.9, theta=1e-5):

    num_states, num_actions, _ = np.shape(transitions)

    # Initialize value function
    V = np.zeros(num_states)

    while True:
        delta = 0
        for s in range(num_states):
            v = V[s]
            Q = np.zeros(num_actions)
            for a in range(num_actions):
                Q[a] = np.sum(transitions[s, a] * (rewards[s, a] + gamma * V))
            V[s] = np.max(Q)
            delta = max(delta, np.abs(v - V[s]))
        if delta < theta:
            break

    # Extract policy
    policy = np.zeros(num_states, dtype=np.int64)
    for s in range(num_states):
        Q = np.zeros(num_actions)
        for a in range(num_actions):
            Q[a] = np.sum(transitions[s, a] * (rewards[s, a] + gamma * V))
        policy[s] = np.argmax(Q)

    return V, policy

# Example usage:
transitions = np.array([[[0.7, 0.3], [0.1, 0.9]], [[0.4, 0.6], [0.5, 0.5]]])
rewards = np.array([[[10, 0], [5, 10]], [[0, 5], [-1, -1]]])

optimal_value_function, optimal_policy = value_iteration(transitions, rewards)
print("Optimal value function:", optimal_value_function)
print("Optimal policy:", optimal_policy)




