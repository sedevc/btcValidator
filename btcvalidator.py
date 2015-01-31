from bitcoinaddress import validate
from Tkinter import *

class MyController():
    def __init__(self,parent):
        self.parent = parent
        self.model = MyModel(self)
        self.view = MyView(self)
        self.view.setEntry_text('Bitcoin address')
        self.view.setLabel_text('Validate')
    def quitButtonPressed(self):
        self.parent.destroy()
    def validateButtonPressed(self):
        self.view.setLabel_text(self.view.entry_text.get() + self.model.validateAddress(self.view.entry_text.get()))



class MyView(Frame):
    def loadView(self):
        entry = Entry(self.frame, width = 45, textvariable = self.entry_text).grid(row = 0, column = 0, pady = 10, padx = 10, sticky = EW)
        label = Label(self.frame,textvariable = self.label_text).grid(row = 1, column = 0, pady = 10, padx = 10, sticky = EW)
        addButton = Button(self.frame,text = "Validate", command = self.vc.validateButtonPressed).grid(row = 0, column = 1)
        quitButton = Button(self.frame,text = 'Quit', command= self.vc.quitButtonPressed).grid(row = 0,column = 2)
    def __init__(self, vc):
        self.frame = Frame()
        self.frame.grid(row = 0,column=0)
        self.vc = vc
        self.entry_text = StringVar()
        self.label_text = StringVar()
        self.loadView()
    def getEntry_text(self):
        return self.entry_text.get()
    def setEntry_text(self, text):
        self.entry_text.set(text)
    def getLabel_text(self):
        return self.label_text.get()
    def setLabel_text(self, text):
        self.label_text.set(text)

class MyModel():
    def __init__(self,vc):
        pass
    def validateAddress(self, address):
        if validate(address):
            return ' is OK'
        else:
            return ' is invalid'

def main():
    root = Tk()
    frame = Frame(root)
    root.title('Bitcoin address validator')
    root.geometry("500x100")
    app = MyController(root)
    root.mainloop()  


if __name__ == '__main__':
    main() 