class Environment: 

    def __init__(self,board):
        self.board = board
        self.ncols = None 
        self.nrows = None
        self.initial_state = None
        self.current_state = None
        self.casillasprohibidas = []
        self.rewards = []
        self._initial_parameters()
    
    def _initial_parameters(self): 
        self.nrows = len(self.board)
        self.ncols = len(self.board[0])
        for i in range(self.nrows): # no me gusta el doble for
            for j in range(self.ncols):
                state = self.board[i][j]
                if state == 's': 
                    self.initial_state = [i,j] 
                    self.current_state = self.initial_state
                elif state == '#':
                    self.casillasprohibidas.append((-i,j))
                elif state == '1':
                    self.rewards.append((-i,j,1))
                elif state == '-1':
                    self.rewards.append((-i,j,-1))

    def get_current_state(self):
        """
        que no recibe parámetros y retorna el estado actual 
        (la casilla donde se encuentra el agente)
        """
        return self.current_state
    
    def get_posible_actions(self):
        """
        que recibe el estado actual del agente como parámetro y
        retorna las acciones disponibles para dicho estado. 
        Las acciones estarán dadas por su nombre 
        ('up', 'down', 'left', 'right'). Como convención definiremos 
        que el agente siempre puede moverse en todas las direcciones, 
        donde un movimiento en dirección de un obstáculo o los límites
        del ambiente no tienen ningún efecto visible en la posición del agente
        """
        return ('up','down','left','right')
    
    def do_action(self,action):
        """
        que recibe como parámetro la acción a ejecutar y 
        retorna el valor de la recompensa y el nuevo estado del
        agente, como un pareja reward, new_state
        """
        next_state =  [0,0]
        reward = 0
        if action == 'up':
            next_state[0],next_state[1] = self.current_state[0] + 1 ,self.current_state[1]
        elif action == 'down':
            next_state[0],next_state[1] = self.current_state[0] - 1 ,self.current_state[1]
        elif action == 'right':
            next_state[0],next_state[1] =  self.current_state[0] ,self.current_state[1]+1
        elif action == 'left':
            next_state[0],next_state[1] = self.current_state[0] ,self.current_state[1]-1

        if next_state[0]>self.nrows or next_state[1]>self.ncols or next_state[0]>0 or next_state[1]<0:
            return reward,self.current_state
        
        if tuple(next_state) in set(self.casillasprohibidas):
            self.current_state = self.initial_state
            return reward,self.current_state
        
        state = [t for t in set(self.rewards) if t[0]==next_state[0] and t[1] == next_state[1]]
        if len(state)>0:     
            reward = state[0][2]
            
        self.current_state = next_state
        return reward, self.current_state
    
    def reset(self):
        """
        que no recibe parámetros y restablece el ambiente a su estado inicial.
        """
        self.current_state = self.initial_state
        return
    
    def is_terminal(self):
        """
        que no recibe parámetros y determina 
        si el agente está en el estado final o no. 
        En nuestro caso, el estado final estará determinado
        por las casillas de salida (i.e., con un valor definido).
        """
        rewards = [t for t in self.rewards 
                   if t[0] == self.current_state[0] and t[1] == self.current_state[1]]
        if len(rewards)>0:
            return True
        return False
    



