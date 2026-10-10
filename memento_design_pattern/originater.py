from memento import TextMemento
class TextEditor():
    def __init__(self):
        self.__text : str = ""
    
    def write(self, text : str):
        self.__text += text
    
    def get_text(self)->str:
        return self.__text
    
    def save_state(self)->TextMemento:
        return TextMemento(self.__text)
    
    def restore(self, tm : TextMemento):
        self.__text = tm.get_state()
        

    
        