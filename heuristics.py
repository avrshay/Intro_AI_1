from color_blocks_state import color_blocks_state

# you can add helper functions and params
goal_state = ""


def init_goal_for_heuristics(goal_blocks):
    global goal_state
    goal_state = goal_blocks

def base_heuristic(_color_blocks_state):
    list_state = _color_blocks_state.get_state()
    sum_fun = 0
    for i in range(len(list_state)-1):
        if (abs(list_state[i][0]-list_state[i+1][0]) != 1) and (abs(list_state[i][0]-list_state[i+1][1]) != 1):
            if (abs(list_state[i][1]-list_state[i+1][0]) != 1) and (abs(list_state[i][1]-list_state[i+1][1]) != 1):
                sum_fun = sum_fun+1
    return sum_fun

def advanced_heuristic(_color_blocks_state):
    return 0

המחלקה של החיפוש:
from search_node import search_node
from color_blocks_state import color_blocks_state
import heapq
open_heap = []
update={}

def create_open_set():
    global open_heap
    global update
    return open_heap

def create_closed_set():
    close_set = set()
    return close_set


def add_to_open(vn, open_set):
    heapq.heappush(open_heap, (vn.f, vn))
    update[vn] = vn.f


def open_not_empty(open_set):
    if len(open_heap) > 0:
        return True
    else:
        return False