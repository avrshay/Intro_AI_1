import heuristics

#The function accepts a string that represents a final state and returns nothing.
#המחרוזת שמתקבלת מייצגת רק את הצבעים הגלויים, מחרוזת של מספרים שלמים
#ההנחה היא שהמחרוזת מגיעה בפורמט של מספרים מופרדים (למשל בפסיקים או רווחים).
def init_goal_for_search(goal_blocks):

    color_blocks_state.final_state = [] #איפוס מבנה קודם כמו שהיה כתוב בהנחיות

    parts=clean_String_helper(goal_blocks)

    for part in parts:
        color_blocks_state.final_state.append(int(part))


#helper functions
def clean_String_helper(str):
    clean_str = str.replace('(', ' ').replace(')', ' ').replace(',', ' ')
    return clean_str.split()  # ['5', '2', '1', '3']


class color_blocks_state: #מייצג את מצב אפשרי של המגדל

    final_state=[] #[x, ...., y] #רק את מה שרואים - סטטי כי זה מצב שמשותף לכל המגדלים

    #constractor which convert a given string to tuples=state
    def __init__(self, blocks_str, **kwargs):
       # you can use the init function for several purposes
        self.state = []# [(top_cube), (second_cube), ..., (bottom_cube)], (top_cube)=(X,Y)

        color_list=clean_String_helper(blocks_str)

        for i in range(0, len(color_list), 2):
            self.state.append((int(color_list[i]), int(color_list[i + 1]))) #covert to int as well

    @staticmethod
    #A static function that receives a color_blocks_state object  and
    # returns true if the state is final and false otherwise.
    def is_goal_state(_color_blocks_state):

        current_tower = _color_blocks_state.state
        for block, goal in zip(current_tower, color_blocks_state.final_state): #רץ במקביל על 2 הרשימות
            if block[0] != goal:
                return False
        return True


    #The function takes no input and returns a list of tuples such that each one has
    # an object of type color_blocks_state representing one of the neighbors and the
    # cost of moving to that neighbor.
    def get_neighbors(self):


        # you can change the body of the function if you want
        # def __hash__(self):

        # you can change the body of the function if you want
        # def __eq__(self, other):
        # you can change the body of the function if you want

    # for debugging states
    def get_state_str(self):
        return str(self.state)

    #you can add helper functions
