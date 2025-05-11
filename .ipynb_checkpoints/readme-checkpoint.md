# reinforcement-learning

- study of agents and how they learn by trial and error.
- **Terminologies:**

  - **state and observation:** state s is a complete description of world, observation is partial description
  - **action space:** valid actions in a given environment. (discrete or continous)
  - **policies:** rule by which agent decides to act(deterministic or stochasitc).
    - policy is agents brain.
  - **trajectories:** sequence of state and action in the world.
    - aka: rollout or episodes.
  - **reward function:** current state of world, action just taken, next state of world
    - different formulations of return
  - **value function:** expected return if u start in that state.

#### Resources:

1. Flappy-ai

   - `$ pip install flappy-bird-gymnasium`
   - `$ flappy_bird_gymnasium`
   - `$ flappy_bird_gymnasium --mode random`
   - `$ flappy_bird_gymnasium --mode dqn`

2. AgileRL
   - [docs](https://docs.agilerl.com/en/latest/get_started/index.html)
3. OpenAi spinning up
   - [docs](https://spinningup.openai.com/en/latest/index.html)
4. stable baseline
   - [docs](https://stable-baselines.readthedocs.io/en/master/)
5. [Book on RL](https://web.stanford.edu/class/psych209/Readings/SuttonBartoIPRLBook2ndEd.pdf)
6. [multi-agent systems](https://huggingface.co/learn/deep-rl-course/en/unit7/introduction-to-marl)
7. [RLlib](https://docs.ray.io/en/latest/rllib/index.html)
8. [tianshou](https://tianshou.org/en/stable/)
9. [godot-rl](https://huggingface.co/learn/deep-rl-course/unitbonus3/godotrl) 10.[unity ml agents](https://huggingface.co/learn/deep-rl-course/en/unit5/introduction)

   11.[ml-agents](https://github.com/Unity-Technologies/ml-agents)

   12.[RL course](https://sarthdubey.in/Reinforcement_Learning/Sections/003_A_RL_problem.html)

- **RL algos:**

  - **Model free**

    - policy optimization
    - q-learning

  - **Model based**
    - learn the model
    - given the model

Imp things:

- policies
- action value functions
- value functions
- models.

RL concepts:
Reward hypothesis:

- All goals can be described by the maximisation of expected cumulative reward.
- A RL agent’s learning process is heavily linked with the reward distribution over time, however, there is no predefined way on how to design the best reward function.
