class TextMemento():
    
    def __init__(self, curr_state : str):
        self.__state : str = curr_state
        
    def get_state(self):
        return self.__state