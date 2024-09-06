
import random
from typing import Sequence
import matplotlib.pyplot as plt
import numpy as np
from Maquinas import Maquina

class Bandido:

    def __init__(self,maquinas,estacionarias,epsilon,optimismo):
        self.occurrences = [0]*len(maquinas)
        self.Q = [optimismo]*len(maquinas)
        self.cumulative_reward = 0
        self.maquinas = maquinas
        self.epsilon = epsilon
        self.optimismo = optimismo
        self.estacionarias = estacionarias

    def choose_arm(self):
        
        maxQ = max(self.Q)

        if random.uniform(0,1)<=(1-self.epsilon): 
            ## Elegir la acción codiciosa
            IndicesmaxQ = [i for i,x in enumerate(self.Q) if x == maxQ ]  # Indices o 'acciones' con el mayor Q
            # i_brazo = random.choice(IndicesmaxQ) ## en caso de empate se elige aleatoriamente
            i_brazo = IndicesmaxQ[random.randint(0,len(IndicesmaxQ)-1)]
        else: 
            ## No ser codicioso
            indicesnomaximos = [i for i,x in enumerate(self.Q) if x != maxQ]
            # i_brazo = random.choice(indicesnomaximos)
            if len(indicesnomaximos) == 0: 
                i_brazo = random.randint(0,len(self.Q)-1)
            else:
                i_brazo = indicesnomaximos[random.randint(0,len(indicesnomaximos)-1)]

        if self.estacionarias:
            recompensa = self.maquinas[i_brazo][self.occurrences[i_brazo]]
        else:
            recompensa = self.maquinas[i_brazo].reward(sum(self.occurrences))

        self.occurrences[i_brazo] += 1

        #se ajusta la media Q_k = Q_k + (1/k)[R_k - Qk]
        self.Q[i_brazo] = self.Q[i_brazo] + (1/self.occurrences[i_brazo])*(recompensa-self.Q[i_brazo])
        # se acumula la recompensa obtenida
        self.cumulative_reward += recompensa
        return self.cumulative_reward/sum(self.occurrences) # promedio de la recompensa acumulada
    

    def run(self,num_episodes):
        Bandid = Bandido(self.maquinas,self.estacionarias,self.epsilon,self.optimismo)
        expected_reward = [0]*num_episodes
        for i in range(num_episodes):
            expected_reward[i] = Bandid.choose_arm()
        
        return expected_reward


if __name__=="__main__":

    num_episodes = 1000
    maquinitas = Maquina().maquinas(10,num_episodes) # 10 máquinas y 1000 juegos por máquina
    Bandido_greedy = Bandido(maquinitas,0,0).run(num_episodes)
    Bandido_epsilon_greedy = Bandido(maquinitas,0.1,10).run(num_episodes)
    Bandido_0_5 =  Bandido(maquinitas,0.01,10).run(num_episodes)
    

    x = np.linspace(0, num_episodes, num_episodes)
    # plot definition
    fig, ax = plt.subplots()
    plt.title("Bandit average reward")
    plt.xlabel("Iterations")
    plt.ylabel("Average reward")
    
    ax.plot(x, Bandido_greedy, linewidth=1.0, label=f'bandit Bandido_greedy')
    ax.plot(x, Bandido_epsilon_greedy, linewidth=1.0, label=f'bandit Bandido_epsilon_greedy')
    ax.plot(x, Bandido_0_5, linewidth=1.0, label=f'bandit Bandido_0_5')
    ax.legend()
    plt.show()

