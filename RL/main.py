import gymnasium as gym
# initialize the env.
env = gym.make("LunarLander-v3", render_mode="human") 
observation, info = env.reset(seed=42)

# episode_over = False
for _ in range(1000):
    #we insert our policy here.
    action=env.action_space.sample()

    # step through the env with action
    observation,reward,terminated, truncated,info=env.step(action)

    if terminated or truncated:
        observation,info=env.reset()
env.close()