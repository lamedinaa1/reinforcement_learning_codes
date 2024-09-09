from environment import Environment
from value_iteration import PolicyEvaluation
from policy_improvement import Policy_improvement
import numpy as np 
import pandas as pd
from iteracy_policy import Iteracy_policy

def set_next_state(state,action,nrows,ncols):
        nrows = nrows-1 
        ncols = ncols-1 
        if action == 'up':
            next_state = (state[0] + 1,state[1]) if state[0] != 0 else state
        elif action == 'down': 
            next_state = (state[0]-1,state[1]) if state[0] != -nrows else state
        elif action == 'right': 
            next_state = (state[0],state[1] + 1) if state[1] != ncols else state
        elif action == 'left':
            next_state = (state[0],state[1] - 1) if state[1] != 0 else state
    
        return next_state

if __name__=='__main__':
    print('testing...')

    #### Gridworld
    board = [
        ['s' ,''  ,''  ,''  ,''  ,''    ,''    ,''   ,''   ,''],
        [''  ,''  ,''  ,''  ,''  ,''    ,''    ,''   ,''   ,''],
        [''  ,'#' ,'#' ,'#' ,'#' ,''    ,'#'   ,'#'  ,'#'  ,''],
        [''  ,''  ,''  ,''  ,'#' ,''    ,''    ,''   ,''   ,''],
        [''  ,''  ,''  ,''  ,'#' ,'-1'  ,''    ,''   ,''   ,''],
        [''  ,''  ,''  ,''  ,'#' ,'1'   ,''    ,''   ,''   ,''],
        [''  ,''  ,''  ,''  ,'#' ,''    ,''    ,''   ,''   ,''],
        [''  ,''  ,''  ,''  ,'#' ,'-1'  ,'-1'  ,''   ,''   ,''],
        [''  ,''  ,''  ,''  ,''  ,''    ,''    ,''   ,''   ,''],
        [''  ,''  ,''  ,''  ,''  ,''    ,''    ,''   ,''   ,''],
    ]

    env = Environment(board)
    value_states = np.zeros((10,10))   ## values for all state terminal and nonterminals
    
     # deterministic policy for nonterminal states
    policy = {}
    for statenonterminal in env.get_state_nonterminals():
        policy[statenonterminal] = 'up'


    iteracy_policy = Iteracy_policy(
        environment= env,
        values_state_ini=value_states, # zeros
        policy_ini= policy
    )

    policy = iteracy_policy.policy_iteration(disccount_factor=0.9)
    print(policy)

    state = (0,0)
    for i in range(0,12):
        print(f'state: {state}, policy: {policy[state]}')
        state = set_next_state(state,policy[state],10,10)



