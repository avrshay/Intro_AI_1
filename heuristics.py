from color_blocks_state import color_blocks_state

# you can add helper functions and params
goal_state = ""

def init_goal_for_heuristics(goal_blocks):
    global goal_state
    goal_state = goal_blocks

def base_heuristic(_color_blocks_state):
    list_state = _color_blocks_state.state
    sum_fun = 0
    for i in range(len(list_state)-1):
        if (abs(list_state[i][0]-list_state[i+1][0]) != 1) and (abs(list_state[i][0]-list_state[i+1][1]) != 1):
            if (abs(list_state[i][1]-list_state[i+1][0]) != 1) and (abs(list_state[i][1]-list_state[i+1][1]) != 1):
                sum_fun = sum_fun+1
    return sum_fun

def advanced_heuristic(_color_blocks_state):
    return 0
