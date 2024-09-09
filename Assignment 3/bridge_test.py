from environment import Environment
from value_iteration import PolicyEvaluation
from policy_improvement import Policy_improvement
import numpy as np 
import pandas as pd
from iteracy_policy import Iteracy_policy


if __name__=='__main__':
    print('testing...')

    board = [
        ['#'   ,'-100'  ,'-100'  ,'-100'   ,'-100'  ,'-100'    ,'#'  ],
        ['s'   ,'0'     ,'0'     ,'0'      ,'0'     ,'0'       ,'100'  ],
        ['#'   ,'-100'  ,'-100'  ,'-100'   ,'-100'  ,'-100'    ,'#'  ],
    ]

    env = Environment(board)
    value_states = np.zeros((3,7))   ## values for all state terminal and nonterminals
    policy = {
        (-1,0): 'up', 
        (-1,1): 'up',
        (-1,2): 'up',
        (-1,3): 'up',
        (-1,4): 'up',
        (-1,5): 'up',
        (-1,6): 'up',
    }  # deterministic policy for nonterminal states
    

    iteracy_policy = Iteracy_policy(
        environment= env,
        values_state_ini=value_states, # zeros
        policy_ini= policy
    )

    policy = iteracy_policy.policy_iteration(disccount_factor=0.1)

    print(policy)