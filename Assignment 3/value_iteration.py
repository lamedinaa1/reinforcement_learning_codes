from environment import Environment
import numpy as np
class PolicyEvaluation: 

    def __init__(self,
                 environment: Environment, 
                 values_states: np.array ,  ## V(S)= 0 for all s state terminal and non-terminal
                 policy: dict,          ## A policy for s state nonterminal to be evaluated
                 disccount_factor: float,
                 ):
        
        self.values_states = values_states
        self.environment = environment
        self.policy = policy
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
        return value
    

    def iteracy_policy_evaluation(self,threshold):
        delta = float('inf')
        nrows = self.environment.nrows
        ncols = self.environment.ncols
        while delta > threshold:
            delta = 0
            for state in self.environment.get_state_nonterminals():
                value = self.values_states[np.abs(state[0])][state[1]]
                action = self.policy[state] # deterministc policy
                next_state = self.set_next_state(state,action,nrows,ncols)
                self.values_states[np.abs(state[0])][state[1]] = self.value(state,action,next_state)
                delta = np.max(
                    [
                        delta,
                        np.abs(value - self.values_states[np.abs(state[0])][state[1]])
                    ]
                    )
        return self.values_states
    
if __name__ == '__main__':
    print('testing')

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
    disccount_factor = 0.1

    p = PolicyEvaluation(
        env,
        value_states,
        policy,
        disccount_factor
    )

    value_states_policy = p.iteracy_policy_evaluation(0.9)

    print(value_states_policy)