import random 

class Bandit_epsilon_decay:

    class Maquina():
        def recompensa(self):
            # return random.uniform(-3,3)
            return random.gauss(0,1)
        

    def __init__(self,nummaquinas=10,epsilon=0.1):
        self.epsilon = epsilon
        self.occurrences = [0]*nummaquinas
        self.Q = [0]*nummaquinas
        self.maquinas = [self.Maquina() for _ in range(nummaquinas)]
        self.retorno = 0

    def choose_arm(self):
        
        maxQ = max(self.Q)

        if random.random()<=(1-self.epsilon): 
            ## Elegir la acción codiciosa
            IndicesmaxQ = [i for i,x in enumerate(self.Q) if x == maxQ ]  # Indices o 'acciones' con el mayor Q
            i_brazo = random.choice(IndicesmaxQ) ## en caso de empate se elige aleatoriamente
        else: 
            ## No ser codicioso
            indicesnomaximos = [i for i,x in enumerate(self.Q) if x != maxQ]
            i_brazo = random.choice(indicesnomaximos)

        recompensa = self.maquinas[i_brazo].recompensa()
        self.occurrences[i_brazo] += 1
        self.Q[i_brazo] = self.Q[i_brazo] + (1/self.occurrences[i_brazo])*(recompensa-self.Q[i_brazo])
        self.retorno += recompensa
        return max(self.Q)

    def run(self):

        episodes = 10
        bandit = Bandit_epsilon_decay()
        expected_reward = [0 for _ in range(episodes)]
        for i in range(0,episodes):
            expected_reward[i] = bandit.choose_arm()
        
        return expected_reward

if __name__=='__main__':
    b = Bandit_epsilon_decay()
    hist_expectreward = b.run()
    for i in hist_expectreward:
        print("----------------------")
        print(i)