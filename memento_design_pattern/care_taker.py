from typing import List
from memento import TextMemento

class History():
    
    def __init__(self):
        self.__history : List[str] = []
        
    def save(self, state : TextMemento):
        self.__history.append(state)
        
    def undo(self) -> TextMemento:
        if len(self.__history)>0 :
            self.__history.pop()
            if len(self.__history):
                return self.__history[-1]
            else :
                TextMemento("")
        else :
            print("Nothing to undo")