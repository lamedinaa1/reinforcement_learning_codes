from environment import Environment
import numpy as np
class policyEvaluation: 

    def __init__(self,
                 values_states: np.array ,  ## V(S)= 0 for all s state terminal and non-terminal
                 environmemt: Environment, 
                 policy: dict,          ## A policy for s state nonterminal to be evaluated
                 disccount_factor,
                 ):
        
        self.values_states = values_states
        self.environment = environmemt
        self.policy = policy
        self.disccount_factor = disccount_factor
        return
    

    def transition_probabilitie(self,state,action,next_state):
        """
        action: 'up','down','right','end'
        state: (i,j) belongs to S = {(i,j): 0<=i<=2 and 0<=j<=2}
        next_state belong to S
        """
        conditions = (action=='up' and next_state == (state[0]+1,state[1]))
        conditions = conditions or (action=='down' and next_state == (state[0],state[1]-1))
        conditions = conditions or (action=='right' and next_state == (state[0],state[1]+1))
        conditions = conditions or (action=='left' and next_state == (state[0],state[1]-1))

        if conditions: 
            return 1
        return 0

    def value(self,state,action,nex_state):
        init_state = Environment.set_initial_state(state)
        reward, _ = Environment.do_action(action)
        value_nextState = self.values_states[nex_state[0],nex_state[1]]
        transition_probaility = self.transition_probabilitie(state,action,nex_state)
        value = transition_probaility(reward + self.disccount_factor*value_nextState)
        return value

    def iteracy_policy_evaluation(self,state):
        policy_state_action = self.policy[state] # deterministc policy
        if policy_state_action == 'up':
            next_state = (state[0] + 1,state[1])
        elif policy_state_action == 'down': 
            next_state = (state[0]-1,state[1])
        elif policy_state_action == 'right': 
            next_state = (state[0],state[1] + 1)
        elif policy_state_action == 'left':
            next_state == (state[0],state[1] - 1) 
        return self.value(state,policy_state_action,next_state)

if __name__ == '__main__':
    print("testing ..")

    m = np.zeros((3,3))
    print(m)
    print(m[0][1])
    print(type(m))