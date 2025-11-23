from color_blocks_state import *

# you can add helper functions and params
goal_state = None
up_goal_state = 0
tuples_set_goal = set()


def init_goal_for_heuristics(goal_blocks): #1,5,9,21
    global goal_state
    global tuples_set_goal
    global up_goal_state
    tuples_set_goal.clear()

    goal_state=clean_String_helper(goal_blocks) #[1,5,9,21] char
    goal_state = [int(x) for x in goal_state]

    up_goal_state = goal_state[0]
    for i in range(len(goal_state) - 1, 0, -1):
        tuples_set_goal.add(frozenset([goal_state[i],goal_state[i - 1]]))

    #print (tuples_set_goal)

def base_heuristic(_color_blocks_state):
    list_state = _color_blocks_state.state
    sum_fun = 0

    for i in range(len(list_state) - 1, 0, -1):
        if (frozenset([list_state[i][0], list_state[i - 1][0]]) not in tuples_set_goal) and (
                frozenset([list_state[i][0], list_state[i - 1][1]]) not in tuples_set_goal):
            if (frozenset([list_state[i][1], list_state[i - 1][0]]) not in tuples_set_goal) and (
                    frozenset([list_state[i][1], list_state[i - 1][1]]) not in tuples_set_goal):
                sum_fun = sum_fun + 1
    return sum_fun


def advanced_heuristic(_color_blocks_state):
    list_state = _color_blocks_state.state
    sum_fun = 0
    if list_state[0][0] != up_goal_state and list_state[0][1] != up_goal_state:
        sum_fun = sum_fun + 1
    for i in range(len(list_state) - 1, 0, -1):
        if frozenset[list_state[i][0], list_state[i - 1][0]] in tuples_set_goal:
            continue
        else:
            sum_fun = sum_fun + 1
    return sum_fun
