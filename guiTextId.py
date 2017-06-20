
from tkinter import *
from PIL import Image, ImageTk

from textId import *

class GuiTextId(Frame):
    def getMaster(self):
        return self.master

    def getFrame(self):
        return self.frame

    def clearFrame(self):
        frame = self.getFrame()
        for widget in frame.winfo_children():
            widget.destroy()
        return
 
    def createStatusFrame(self, master):
        self.statusFrame = Frame(master, width = 600, height = 30)
        self.statusFrame.grid(row = 2, column = 0, sticky = (S, E))
        
        if self.current_text == '':
            sh_run = ' ' * 130
        else:
            sh_run = self.current_text+ ' ' * (130 - len(self.current_text))
        self.status = Label(self.statusFrame, text = sh_run, bd = 3, relief = SUNKEN, 
                            anchor = W, fg = 'light green', bg = 'dark green', font = 'Helvetica 16 bold')
        self.status.pack(side = LEFT, fill = X) 


    def refreshStatus(self, master):
        if self.status == None:
            LOGGER.info('Status bar is not created yet')
            return

        self.status.destroy()
        self.logo.destroy()

        self.createStatusFrame(master)

        return


    def createMenuFrame(self, master):
        self.frame = Frame(master, width = 600, height = 200)
        #self.frame.pack(fill=BOTH, expand = 1)
        self.frame.grid(row = 1, column = 0, sticky = (N, E, W))
        mu = Menu(master)
        master.config(menu = mu)
        subMenu1 = Menu(mu)
        mu.add_cascade(label = "Train Model", menu = subMenu1)
        subMenu1.add_command(label = "Train Model1", command = self.load_train1)
        subMenu1.add_separator()
        subMenu1.add_command(label = "Train Model2", command = self.load_train2)

        subMenu2 = Menu(mu)
        mu.add_cascade(label = "Load Mystery Text", menu = subMenu2)
        subMenu2.add_command(label = "Mystery Text", command = self.load_text)

        subMenu3 = Menu(mu)
        mu.add_cascade(label = "Analyze", menu = subMenu3)
        subMenu3.add_command(label = "Analyze Text", command = self.analyze_text)
    

    def do_load_train1(self):
        file_name = self.fileEntry.get()
        
        print(" +++++++++++ Model1 +++++++++++ ")
        self.trained_tm1 = TextModel( "Model1" )
        text1 = self.trained_tm1.readTextFromFile( file_name )
        self.trained_tm1.createAllDictionaries(text1)  # provided in hw description

    def load_train1(self):
        self.clearFrame()

        fileLabel = Label(self.frame, text = 'Please enter train model1 file name:', fg='black', bg='light blue')
        fileLabel.grid(row = 1, column = 1, sticky = E)
        self.fileEntry = Entry(self.frame, width=50)
        self.fileEntry.insert(END, './TestRound1/train1.txt')
        self.fileEntry.grid(row = 1, column = 2, columnspan = 5, sticky = E)

        submitButton = Button(self.frame, text='Load', command = self.do_load_train1)
        submitButton.grid(row = 5, column = 2)
        return

    def do_load_train2(self):
        file_name = self.fileEntry.get()
        
        print(" +++++++++++ Model2 +++++++++++ ")
        self.trained_tm2 = TextModel( "Model2" )
        text1 = self.trained_tm2.readTextFromFile( file_name )
        self.trained_tm2.createAllDictionaries(text1)  # provided in hw description

    def load_train2(self):
        self.clearFrame()

        fileLabel = Label(self.frame, text = 'Please enter train model2 file name:', fg='black', bg='light blue')
        fileLabel.grid(row = 1, column = 1, sticky = E)
        self.fileEntry = Entry(self.frame, width=50)
        self.fileEntry.insert(END, './TestRound1/train2.txt')
        self.fileEntry.grid(row = 1, column = 2, columnspan = 5, sticky = E)

        submitButton = Button(self.frame, text='Load', command = self.do_load_train2)
        submitButton.grid(row = 5, column = 2)
        return
        
    def do_load_text(self):
        file_name = self.fileEntry.get()
        
        print(" +++++++++++ Unknown text +++++++++++ ")
        self.unknown_tm = TextModel( "Unknown (trial)" )
        text_unk = self.unknown_tm.readTextFromFile( "TestRound1/unknown.txt" )
        self.unknown_tm.createAllDictionaries(text_unk)  # provided in hw description

    def load_text(self):
        self.clearFrame()

        fileLabel = Label(self.frame, text = 'Please enter mystery text1 file name:', fg='black', bg='light blue')
        fileLabel.grid(row = 1, column = 1, sticky = E)
        self.fileEntry = Entry(self.frame, width=50)
        self.fileEntry.insert(END, './TestRound1/unknown.txt')
        self.fileEntry.grid(row = 1, column = 2, columnspan = 5, sticky = E)

        submitButton = Button(self.frame, text='Load', command = self.do_load_text)
        submitButton.grid(row = 5, column = 2)
        return

    def analyze_text(self):
        result = self.unknown_tm.compareTextWithTwoModels(self.trained_tm1, self.trained_tm2)

        self.clearFrame()
        
        t = Text(self.getFrame(), bg = 'light blue', fg = 'black', height = 30)
        t.pack(fill=BOTH, expand = 1)
        t.insert(END, result)  
        self.result = result
        return


    def __init__(self, master=None):
        self.current_text = ''
        self.trained_tm1 = None
        self.trained_tm2 = None
        self.unknown_tm = None
        self.result = ''

        self.master = master
        self.master.minsize(width = 500, height = 300)       
        self.master.rowconfigure(0, weight = 1)
        self.master.rowconfigure(1, weight = 8)
        self.master.rowconfigure(2, weight = 1)

        self.frame = None
        self.createMenuFrame(master)

        self.fileEntry = None
        self.lstbox = None

        self.statusFrame = None
        self.status = None
        self.logo = None
        #self.createStatusFrame(master)


root = Tk()
root.title("Text Identification")
app = GuiTextId(master=root)
root.mainloop()
root.destroy()