from environment import Environment
import numpy as np
import pandas as pd

class  Policy_improvement: 

    def __init__(
            self,
            environment: Environment,
            values_states: np.array,
            disccount_factor: float
            ):
        
        self.values_states = values_states
        self.environment = environment
        self.disccount_factor = disccount_factor
        return
    
    def set_next_state(self,state,action,nrows,ncols):
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
    
    def transition_probabilities(self,state,action,next_state):
        """
        action: 'up','down','right','end'
        state: (i,j) belongs to S = {(i,j): 0<=i<=2 and 0<=j<=2}
        next_state belong to S
        """
        if next_state[1]<0 or next_state[0]>0:
            return 0

        conditions = (action=='up' and next_state == (state[0]+1,state[1]))
        conditions = conditions or (action=='down' and next_state == (state[0]-1,state[1]))
        conditions = conditions or (action=='right' and next_state == (state[0],state[1]+1))
        conditions = conditions or (action=='left' and next_state == (state[0],state[1]-1))

        if conditions: 
            return 1
        return 0
    
    def value(self,state,action,nex_state):
        init_state = self.environment.set_current_state(state)
        reward, _ = self.environment.do_action(action)
        value_nextState = self.values_states[np.abs(nex_state[0]),nex_state[1]]
        transition_probaility = self.transition_probabilities(state,action,nex_state)
        value = transition_probaility*(reward + self.disccount_factor*value_nextState)
        
        # print(f"""
        # ------------------------\n
        # disccount_factor: {self.disccount_factor}\n
        # state: {state}\n
        # nex_state: {nex_state}\n
        # action: {action}\n
        # reward: {reward} \n
        # value_nextState: {value_nextState}\n
        # transition_probaility: {transition_probaility}\n
        # value: {value}
        # ------------------------\n
        # """)
        return value
    

    def policy_improvement(self):
        new_policy = {}
        nrows = self.environment.nrows
        ncols = self.environment.ncols
        for state in self.environment.get_state_nonterminals():
            values_policies = pd.Series([0,0,0,0],index=['up','down','left','right'])
            for a in self.environment.get_posible_actions():
                next_state = self.set_next_state(state,a,nrows,ncols)
                values_policies[a] = self.value(state,a,next_state)
            max_action = values_policies.idxmax()
            new_policy[state] = max_action
        
        return new_policy
    

if __name__ == '__main__':
    print('testing')

    board = [
        ['#'   ,'-100'  ,'-100'  ,'-100'   ,'-100'  ,'-100'    ,'#'  ],
        ['s'   ,'0'     ,'0'     ,'0'      ,'0'     ,'0'       ,'100'  ],
        ['#'   ,'-100'  ,'-100'  ,'-100'   ,'-100'  ,'-100'    ,'#'  ],
    ]

    env = Environment(board)
    
    policy = {(-1,0): 'up', (-1,1): 'up',(-1,2): 'up',(-1,3): 'up',(-1,4): 'up',(-1,5): 'up',(-1,6): 'up',}
    # Values for policy = {(-1,0): 'up', (-1,1): 'up',(-1,2): 'up',(-1,3): 'up',(-1,4): 'up',(-1,5): 'up',(-1,6): 'up',}
    # value_states_policy = np.array([
    #     [   0.,    0.,    0.,    0.,    0.,    0.,    0.],
    #     [   0., -100., -100., -100., -100., -100.,    0.],
    #     [   0.,    0.,    0.,    0.,    0.,    0.,    0.],
    #     ]
    # )

    value_states_policy = np.array(

        [
            [  0.,   0.,   0. ,  0.,   0.,   0.,   0.],
            [  0.,   0.,   0. ,  1.,  10., 100.,   0.],
            [  0.,   0.,   0. ,  0.,   0.,   0.,   0.],
        ]
    )
    
    pi = Policy_improvement(
        environment=env, 
        values_states=value_states_policy,
        disccount_factor=0.1
    )

    policy_improved = pi.policy_improvement()

    print(policy_improved)



                
