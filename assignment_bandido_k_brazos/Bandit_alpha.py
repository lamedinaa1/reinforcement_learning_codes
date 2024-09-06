
import random

class Bandido_alpha:

    def __init__(self,maquinas,estacionarias,epsilon,optimismo,alpha):
        self.occurrences = [0]*len(maquinas)
        self.Q = [optimismo]*len(maquinas)
        self.cumulative_reward = 0
        self.maquinas = maquinas
        self.epsilon = epsilon
        self.optimismo = optimismo  # para inicializar Q's con optimismo e incentivar la exploración al principio
        self.alpha = alpha
        self.estacionarias = estacionarias # Booleano que indica si las máquinas son estacionarias o no. True entonces estacionarias

    def choose_arm(self):
        
        maxQ = max(self.Q)

        if random.uniform(0,1)<=(1-self.epsilon): 
            ## Elegir la acción codiciosa
            IndicesmaxQ = [i for i,x in enumerate(self.Q) if x == maxQ ]  # Indices o 'acciones' con el mayor Q
            ### en caso que hayan mas de un indice len() se elige aleatoriamente
            i_brazo = IndicesmaxQ[random.randint(0,len(IndicesmaxQ)-1)]
        else: 
            ## No ser codicioso
            indicesnomaximos = [i for i,x in enumerate(self.Q) if x != maxQ]
            if len(indicesnomaximos) == 0: 
                i_brazo = random.randint(0,len(self.Q)-1)
            else:
                i_brazo = indicesnomaximos[random.randint(0,len(indicesnomaximos)-1)]
        
        if self.estacionarias:
            recompensa = self.maquinas[i_brazo][self.occurrences[i_brazo]]
        else:
            recompensa = self.maquinas[i_brazo].reward(sum(self.occurrences))
        
        self.occurrences[i_brazo] += 1
        
        # Q = Q_k + alpha*[R_k - Q_k] 
        self.Q[i_brazo] = self.Q[i_brazo] + (self.alpha)*(recompensa-self.Q[i_brazo])
        
        self.cumulative_reward += recompensa
        return self.cumulative_reward/sum(self.occurrences)
    

    def run(self,num_episodes):
        Bandid = Bandido_alpha(self.maquinas,self.estacionarias,self.epsilon,self.optimismo,self.alpha)
        expected_reward = [0]*num_episodes
        for i in range(num_episodes):
            expected_reward[i] = Bandid.choose_arm()
        
        return expected_reward


