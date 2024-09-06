import random
from typing import Sequence
import numpy as np

class Maquina():
    
    def reward(self)->float: 
        return random.uniform(-3,3)
    
    def reward_sequences(self,num_secuences)->Sequence[float]:
        media = 0
        return [media+self.reward() for _ in range(0,num_secuences)]


    def maquinas(self,nummaquinas,num_secuences):
        return [Maquina().reward_sequences(num_secuences) for _ in range(nummaquinas)]
    

class Casino_noestacionaria():

    class Maquina_noestacionaria():
        def __init__(self,valorinicial):
            self.valorinicial = valorinicial

        def reward(self,step): 
            return self.valorinicial + np.sin(self.valorinicial*step)

    def __init__(self):
        pass
    
    def maquinas(self,nummaquinas):
        return [self.Maquina_noestacionaria(random.uniform(1,nummaquinas)) for _ in range(nummaquinas)]



