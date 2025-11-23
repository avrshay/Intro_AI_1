from search_node import search_node
from color_blocks_state import color_blocks_state
import heapq


def create_open_set():
    global update_set
    update_set = {}

    open_heap = []

    return open_heap


def create_closed_set():
    close_set = set()
    return close_set


def add_to_open(vn, open_set):
    heapq.heappush(open_set, (vn.f, vn))  # according to the total f
    update_set[vn.state] = vn.g  # according to only the cost


def open_not_empty(open_set):

    while len(open_set) > 0:

        current_f, current_node = open_set[0]

        if current_node.state in update_set and current_node.g > update_set[current_node.state]:
            heapq.heappop(open_set)
        else:
            break  # the head is fine

    if len(open_set) > 0:
        return True
    else:
        return False


def get_best(open_set):
    current_f, current_node = heapq.heappop(open_set)

    return current_node


def add_to_closed(vn, closed_set):
    closed_set.add(vn.state)


# returns False if curr_neighbor state not in open_set or has a lower g from the node in open_set
# remove the node with the higher g from open_set (if exists)
def duplicate_in_open(vn, open_set):
    if vn.state not in update_set:  # For sure, it isn't in open_set
        return False

    if vn.state in update_set and vn.g >= update_set.get(
            vn.state):  # if I already found better way to arrive this state, it will be a duplicate for sure
        return True

    return False


# returns False if curr_neighbor state not in closed_set or has a lower g from the node in closed_set
# remove the node with the higher g from closed_set (if exists)
def duplicate_in_closed(vn, closed_set):
    if vn.state not in closed_set:
        return False
    if vn.g >= closed_set.get(
            vn.state):  # if I already found better way to arrive this state,  there is a duplicate for sure
        return True

    return False


# helps to debug sometimes..
def print_path(path):
    for i in range(len(path) - 1):
        print(f"[{path[i].state.get_state_str()}]", end=", ")
    print(path[-1].state.state_str)


def search(start_state, heuristic):
    open_set = create_open_set()
    closed_set = create_closed_set()
    start_node = search_node(start_state, 0, heuristic(start_state))
    add_to_open(start_node, open_set)

    while open_not_empty(open_set):

        current = get_best(open_set)

        if color_blocks_state.is_goal_state(current.state):
            path = []
            while current:
                path.append(current)
                current = current.prev
            path.reverse()
            return path

        add_to_closed(current, closed_set)

        for neighbor, edge_cost in current.get_neighbors():
            curr_neighbor = search_node(neighbor, current.g + edge_cost, heuristic(neighbor), current)
            if not duplicate_in_open(curr_neighbor, open_set) and not duplicate_in_closed(curr_neighbor, closed_set):
                add_to_open(curr_neighbor, open_set)

    return None
