import time
from heuristics import *
from color_blocks_state import *
from search import *

if __name__ == '__main__':

    start_blocks = "(5,2),(1,5),(9,5),(21,1)"
    goal_blocks = "1,5,9,21"
    init_goal_for_heuristics(goal_blocks)
    init_goal_for_search(goal_blocks)
    start_state = color_blocks_state(start_blocks)
    start_time = time.time()
    search_result = search(start_state, base_heuristic)
    end_time = time.time() - start_time
    # runtime
    print(end_time)
    # solution cost
    print(search_result[-1].g)

    print(base_heuristic(start_state))

    start_time = time.time()
    search_result = search(start_state, advanced_heuristic)
    end_time = time.time() - start_time
    # runtime
    print(end_time)
    # solution cost
    print(search_result[-1].g)