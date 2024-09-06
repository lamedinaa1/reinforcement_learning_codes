import random 

class Bandit_greedy:

    class Maquina(): 
        def recompensa(self):
            return random.uniform(-3,3)

    def __init__(self,arms=10): 
        self.arms = arms
        self.ocurrences = [0 for i in range(self.arms)]
        self.Q = [0 for _ in range(self.arms)]    # Q = [Q(0),Q(1),....Q(9)]    
        self.retorno = 0    
        self.maquinas = [self.Maquina() for _ in range(self.arms)]



    def choose_arm(self):
        ## selección de la acción más codiciosa
        maxQ = max(self.Q)
        IndicesmaxQ = [i for i,x in enumerate(self.Q) if x == maxQ ]  # Indices o 'acciones' con el mayor Q
        ## en caso de empate se elige aleatoriamente
        i_brazo = random.choice(IndicesmaxQ)
        # se toma la recompensa de la i-ésimo brazo
        recompensa = self.maquinas[i_brazo].recompensa()
        # calculando la media para el i-ésimo brazo
        self.ocurrences[i_brazo] += 1
        self.Q[i_brazo] = self.Q[i_brazo] + (1/self.ocurrences[i_brazo])*(recompensa-self.Q[i_brazo]) 
        # calculando la recompensa acumulada
        self.retorno += recompensa
        # return [self.Q[i_brazo],i_brazo,IndicesmaxQ,self.ocurrences]
        return self.retorno 

    def run(self):
        episodes = 1000
        bandit = Bandit_greedy()
        expected_reward = [0 for _ in range(episodes)]
        for i in range(0,episodes):
            expected_reward[i] = bandit.choose_arm()
        
        return expected_reward
    


if __name__== '__main__':
    b = Bandit_greedy()
    hist_expectreward = b.run()
    for i in hist_expectreward:
        print("----------------------")
        print(i)
