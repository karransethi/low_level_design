from originater import TextEditor
from care_taker import History
from memento import TextMemento

textEdit = TextEditor()
hist = History()

textEdit.write("hey")
hist.save(textEdit.save_state())
print(textEdit.get_text())

textEdit.write("Goldy")
hist.save(textEdit.save_state())

textEdit.write("How are you?")
print(textEdit.get_text())
hist.save(textEdit.save_state())

textEdit.restore(hist.undo())
print(textEdit.get_text())