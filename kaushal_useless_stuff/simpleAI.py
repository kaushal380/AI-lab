import gym
import numpy as np

# Define the CartPole environment
env = gym.make('CartPole-v1')

# Define Q-learning parameters
num_episodes = 1000
num_bins = (1, 1, 6, 12)  # Number of bins for each observation dimension
num_actions = env.action_space.n  # Number of possible actions
alpha = 0.1  # Learning rate
gamma = 0.99  # Discount factor
epsilon = 0.1  # Epsilon for epsilon-greedy policy

# Initialize Q-table
Q = np.zeros(num_bins + (num_actions,))

# Define observation discretization function
def discretize(observation):
    obs = []
    try:
        n = len(observation)
        obs.append(observation)
    except:
        obs.append(observation)
    upper_bounds = [env.observation_space.high[0], 0.5, env.observation_space.high[2], np.radians(50)]
    lower_bounds = [env.observation_space.low[0], -0.5, env.observation_space.low[2], -np.radians(50)]
    ratios = [(obs[i] + abs(lower_bounds[i])) / (upper_bounds[i] - lower_bounds[i]) for i in range(len(obs))]
    discretized_observation = [int(round((num_bins[i] - 1) * ratios[i])) for i in range(len(obs))]
    discretized_observation = [min(num_bins[i] - 1, max(0, discretized_observation[i])) for i in range(len(obs))]
    return tuple(discretized_observation)

# Define epsilon-greedy policy
def epsilon_greedy_policy(state):
    if np.random.random() < epsilon:
        return env.action_space.sample()  # Random action
    else:
        return np.argmax(Q[state])  # Greedy action

# Train the Q-learning agent
for episode in range(num_episodes):
    observation = env.reset()
    state = discretize(observation)
    done = False
    total_reward = 0

    while not done:
        action = epsilon_greedy_policy(state)
        next_observation, reward, done, trunc, info = env.step(action)
        next_state = discretize(next_observation)

        # Update Q-table
        Q[state][action] += alpha * (reward + gamma * np.max(Q[next_state]) - Q[state][action])

        state = next_state
        total_reward += reward

    # Print episode statistics
    print(f"Episode {episode + 1}: Total Reward = {total_reward}")

# Test the trained agent
total_rewards = []
for _ in range(100):
    observation = env.reset()
    state = discretize(observation)
    done = False
    total_reward = 0

    while not done:
        action = np.argmax(Q[state])
        observation, reward, done, _ = env.step(action)
        state = discretize(observation)
        total_reward += reward

    total_rewards.append(total_reward)

# Print average reward over 100 episodes
print(f"Average Reward over 100 Episodes: {np.mean(total_rewards)}")

# Close the environment
env.close()