import numpy as np
import mdptoolbox

S = 0.1  # Probability of success for finding a block - does not end up being relevant
W = 0.6 # Fork win probability
A = 0.6  # Proportion of hash power controlled by the attacker
F = -0.5  # How much to punish when you publish while behind
DISCOUNT_RATE = 0.8  # How much to discount future rewards
EPS = 0.01  # If delta value between time steps is less than epsilon, assume convergence
MAX_ITER = 1000  # Max # of times VI iterates

P = np.array([[[1-S*A,0,0,0,0,0,0,S*A,0,0,0,0,0,0,0,0,0,0],
               [S*(1-A),1-S,0,0,0,0,0,0,S*A,0,0,0,0,0,0,0,0,0],
               [0,S*(1-A),1-S,0,0,0,0,0,0,S*A,0,0,0,0,0,0,0,0],
               [0,0,S*(1-A),1-S,0,0,0,0,0,0,S*A,0,0,0,0,0,0,0],
               [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,1-S*A,0,0,0,0,0,0,S*A,0,0,0,0],
               [0,0,0,0,0,0,S*(1-A),1-S,0,0,0,0,0,0,S*A,0,0,0],
               [0,0,0,0,0,0,0,S*(1-A),1-S,0,0,0,0,0,0,S*A,0,0],
               [0,0,0,0,0,0,0,0,S*(1-A),1-S,0,0,0,0,0,0,S*A,0],
               [0,0,0,0,0,0,0,0,0,S*(1-A),1-S,0,0,0,0,0,0,S*A],
               [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,1-S*A,S*A,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,S*(1-A),1-S,S*A,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,S*(1-A),1-S,S*A,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,S*(1-A),1-S,S*A,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,S*(1-A),1-S,S*A],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,S*(1-A),1-S*(1-A)]],

             [[0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],
               [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]])

R = np.array([[0,F],
              [0,F],
              [0,F],
              [0,(1-W)+W*F],
              [0,0],
              [0,0],
              [0,F],
              [0,F],
              [0,F],
              [0,(1-W)+W*F],
              [0,1],
              [0,0],
              [0,F],
              [0,F],
              [0,F],
              [0,(1-W)+W*F],
              [0,1],
              [S*A*0.1,2]])


MDP = mdptoolbox.mdp.ValueIteration(transitions=P, reward=R, discount=DISCOUNT_RATE, epsilon=EPS,
                                    max_iter=MAX_ITER, initial_value=0)

MDP.run()

print "Optimal policy by state:"
print MDP.policy  # Print policy
print "Value by state: "
print MDP.V  # Print value