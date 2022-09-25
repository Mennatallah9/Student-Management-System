from tkinter import *
from tkinter import ttk
from functions import ConnectorDB

if __name__=="__main__":
    root = Tk()
    application = ConnectorDB(root)

    root.mainloop()