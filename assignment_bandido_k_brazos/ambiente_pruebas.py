from Maquinas import Maquina,Casino_noestacionaria
from Bandit_alpha import Bandido_alpha
from Bandit_greedy_epsilonGreedy import Bandido
import matplotlib.pyplot as plt
import numpy as np

if __name__=="__main__":

    num_episodes = 1000
    maquinas_estacionarias = Maquina().maquinas(10,num_episodes) # 10 máquinas estacionarias
    maquinitas_noestacionarias = Casino_noestacionaria().maquinas(10) # 10 máquinas no estacionarias
    
    bandido_greedy = Bandido(
                        maquinas=maquinas_estacionarias, 
                        estacionarias=True, 
                        epsilon=0,
                        optimismo=0
                    ).run(num_episodes)
    
    bandido_epsilon_greedy= Bandido(
                        maquinas=maquinas_estacionarias, 
                        estacionarias=True, 
                        epsilon=0.1,
                        optimismo=10
                    ).run(num_episodes)
    
    bandido_alpha = Bandido_alpha(
                    maquinas=maquinas_estacionarias,
                    estacionarias=True,
                    epsilon=0.1,
                    optimismo=10,
                    alpha=0.1
                    ).run(num_episodes)


    # escenario no estacionario
    bandido_greedy_ne = Bandido(
                        maquinas=maquinitas_noestacionarias, 
                        estacionarias=False, 
                        epsilon=0,
                        optimismo=0
                        ).run(num_episodes)
    
    bandido_epsilon_greedy_ne = Bandido(
                        maquinas=maquinitas_noestacionarias, 
                        estacionarias=False, 
                        epsilon=0.1,
                        optimismo=10
    ).run(num_episodes)

    bandido_alpha_ne = Bandido_alpha(
                    maquinas=maquinitas_noestacionarias,
                    estacionarias=False,
                    epsilon=0.1,
                    optimismo=10,
                    alpha=0.1
                    ).run(num_episodes)

    x = np.linspace(0, num_episodes, num_episodes)
    # plot definition
    fig, ax = plt.subplots()
    plt.title("Bandits average reward stationary")
    plt.xlabel("Iterations")
    plt.ylabel("Average reward")
    
    ax.plot(x, bandido_greedy, linewidth=1.0, label=f'bandido_greedy')
    ax.plot(x, bandido_epsilon_greedy, linewidth=1.0, label=f'bandido_epsilon_greedy')
    ax.plot(x, bandido_alpha, linewidth=1.0, label=f'bandido_alpha')
    ax.legend()
    plt.show()

    fig, ax = plt.subplots()
    plt.title("Bandits average non-stationary")
    plt.xlabel("Iterations")
    plt.ylabel("Average reward")
    
    ax.plot(x, bandido_greedy_ne, linewidth=1.0, label=f'bandido_greedy_ne')
    ax.plot(x, bandido_epsilon_greedy_ne, linewidth=1.0, label=f'bandido_epsilon_greedy_ne')
    ax.plot(x, bandido_alpha_ne, linewidth=1.0, label=f'bandido_alpha_ne')
    ax.legend()
    plt.show()
