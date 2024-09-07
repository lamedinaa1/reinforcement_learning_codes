from environment import Environment
from value_iteration import PolicyEvaluation
from policy_improvement import Policy_improvement
import numpy as np 
import pandas as pd
class Iteracy_policy: 

    def __init__(
            self,
            environment: Environment, 
            # value_iteration: PolicyEvaluation, 
            # policy_improvement: Policy_improvement,
            values_state_ini: np.array,
            policy_ini: dict, 
             ):
        
        self.environment= environment 
        # self.value_iteration = value_iteration
        # self.policy_improvement = policy_improvement
        self.values_state_ini = values_state_ini
        self.policy_ini = policy_ini

        return
        

    def policy_iteration(self,disccount_factor):
        
        env = self.environment
        policy = {}
        policy_improved = self.policy_ini
        value_states = self.values_state_ini
        i=0

        condition = True # iniciar bucle
        while condition:
            
            i += 1
            policy = policy_improved
            pe = PolicyEvaluation(
                env,
                value_states,
                policy_improved,
                disccount_factor
            )

            value_states = pe.iteracy_policy_evaluation(0.9)
            print(f"values_state: {value_states}")
            
            pi = Policy_improvement(
                environment=env, 
                values_states=value_states,
                disccount_factor=0.1
            )
            policy_improved = pi.policy_improvement()
            print(f"""
                i: {i}\n
                policy: {policy}\n
                policy_improved: {policy_improved}
            """)
            condition = False
            for state in policy_improved.keys():
                if policy[state] != policy_improved[state]:
                    condition = True

        return policy
    

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
    disccount_factor = 0.1 

    iteracy_policy = Iteracy_policy(
        environment= env,
        values_state_ini=value_states, # zeros
        policy_ini= policy
    )

    policy = iteracy_policy.policy_iteration(0.1)
    print(policy)