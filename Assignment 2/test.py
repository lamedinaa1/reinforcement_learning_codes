from environment import *


board = [
        ['s' ,''  ,''  ,''  ,''  ,''    ,''    ,''   ,''   ,''],
        [''  ,''  ,''  ,''  ,''  ,''    ,''    ,''   ,''   ,''],
        [''  ,'#' ,'#' ,'#' ,'#' ,''    ,'#'   ,'#'  ,'#'  ,''],
        [''  ,''  ,''  ,''  ,'#' ,''    ,''    ,''   ,''   ,''],
        [''  ,''  ,''  ,''  ,'#' ,'-1'  ,''    ,''   ,''   ,''],
        [''  ,''  ,''  ,''  ,'#' ,'1'   ,''    ,''   ,''   ,''],
        [''  ,''  ,''  ,''  ,'#' ,''    ,''    ,''   ,''   ,''],
        [''  ,''  ,''  ,''  ,'#' ,'-1'  ,'-1'  ,''   ,''   ,''],
        [''  ,''  ,''  ,''  ,''  ,''    ,''    ,''   ,''   ,''],
        [''  ,''  ,''  ,''  ,''  ,''    ,''    ,''   ,''   ,''],
    ]


env = Environment(board)
print(
    env.initial_state
)
print(
    env.current_state
)
print(
    env.casillasprohibidas
)
print(
     env.rewards
)
print('--------')
print(env.initial_state)
re,current_state = env.do_action('up')
print(re,current_state)

re,current_state = env.do_action('down')
print(re,current_state)

re,current_state = env.do_action('down')
print(re,current_state)

re,current_state = env.do_action('right')
print(re,current_state)

re,current_state = env.do_action('left')
print(re,current_state)

print('-------')
re,current_state = env.do_action('right')
re,current_state = env.do_action('right')
re,current_state = env.do_action('right')
re,current_state = env.do_action('right')
re,current_state = env.do_action('right')

print(current_state)
re,current_state = env.do_action('down')
print(current_state)
re,current_state = env.do_action('down')
print(current_state)
re,current_state = env.do_action('down')
re,current_state = env.do_action('down')

print(current_state)
print(env.is_terminal())
print(re)
print(env.rewards)