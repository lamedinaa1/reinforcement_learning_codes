from environment import *

board = [
        ['#'   ,'-100'  ,'-100'  ,'-100'   ,'-100'  ,'-100'    ,'#'  ],
        ['s'   ,'0'     ,'0'     ,'0'      ,'0'     ,'0'       ,'100'  ],
        ['#'   ,'-100'  ,'-100'  ,'-100'   ,'-100'  ,'-100'    ,'#'  ],
    ]



env = Environment(board)


print(env.do_action('down'))
print(env.is_terminal())
print(env.reset())
print(env.get_current_state())

print(env.do_action('right'))
print(env.do_action('right'))
print(env.do_action('right'))
print(env.do_action('right'))
print(env.do_action('right'))
print(env.do_action('right'))
print(env.is_terminal())
print(env.reset())
print(env.get_current_state())