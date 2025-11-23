import heuristics


# The function accepts a string that represents a final state and returns nothing.
# The string that is returned represents only the visible colors, a string of integers
# The assumption that the string comes in a number-separated format is (comma-separated spaces or spaces).
def init_goal_for_search(goal_blocks):
    color_blocks_state.final_state = []

    parts = clean_String_helper(goal_blocks)

    for part in parts:
        color_blocks_state.final_state.append(int(part))


# helper functions:
def clean_String_helper(str):
    clean_str = str.replace('(', ' ').replace(')', ' ').replace(',', ' ')
    return clean_str.split()  # ['5', '2', '1', '3']


def convert_list_to_str(block_list):
    return ",".join([f"({x},{y})" for x, y in block_list])


class color_blocks_state:  # represents the possible state of the tower

    final_state = []  # [x, ...., y] #Only what you see - static because it is a situation common to all growers

    # constractor which convert a given string to tuples=state
    def __init__(self, blocks_str, **kwargs):
        # you can use the init function for several purposes

        self.state = []  # [(top_cube), (second_cube), ..., (bottom_cube)], (top_cube)=(X,Y)

        if isinstance(blocks_str, list):
            self.state = list(blocks_str)

        else:
            color_list = clean_String_helper(blocks_str)

            for i in range(0, len(color_list), 2):
                self.state.append((int(color_list[i]), int(color_list[i + 1])))  # covert to int as well

    @staticmethod
    # A static function that receives a color_blocks_state object  and
    # returns true if the state is final and false otherwise.
    def is_goal_state(_color_blocks_state):

        current_tower = _color_blocks_state.state
        for block, goal in zip(current_tower, color_blocks_state.final_state):
            if block[0] != goal:
                return False
        return True

    # The function takes no input and returns a list of tuples such that each one has
    # an object of type color_blocks_state representing one of the neighbors and the
    # cost of moving to that neighbor.
    def get_neighbors(self):
        # 2n-1 neighbors
        # n spins
        # n-1 flips

        neighbors_list = []

        # new neighbors cause by spin:
        for i in range(len(self.state)):
            # spin the block in place i:
            new_block = (self.state[i][1], self.state[i][0])

            new_neighbor = self.state[:i] + [new_block] + self.state[i + 1:]

            neighbors_list.append(
                (color_blocks_state(new_neighbor),1))  # add the neighbor to the neighbors' list, spin always cost 1

        # new neighbors cause by flip:
        for i in range(len(self.state) - 1):
            new_neighbor = self.state[:i] + self.state[i:][::-1]  # flip it
            neighbors_list.append(
                (color_blocks_state(new_neighbor), 1))  # flip also cost 1 dua to the forom

        return neighbors_list

    def __hash__(self):
        return hash(tuple(self.state))  # convert the list to mutable and using hash method of tuples

    def __eq__(self, other):

        if not isinstance(other, color_blocks_state):
            return False

        return self.state == other.state

    # for debugging states
    def get_state_str(self):
        return str(self.state)
