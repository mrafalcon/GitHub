import settings
import custom
import read_dv
import write_dv
import datavolley
#import functions
import tkinter
from tkinter import filedialog
from tkinter import ttk
from tkinter import Menu

datavolley.init()
#main.init()



class MyGui:
    def __init__(self):
        
        self.window = tkinter.Tk()
        self.window.title("DataVolley Master")
        self.window.geometry('%dx%d+%d+%d' % (self.window.winfo_screenwidth()*2/3, self.window.winfo_screenheight()*2/3, self.window.winfo_screenwidth()/2 - self.window.winfo_screenwidth()/3, self.window.winfo_screenheight()/2 - self.window.winfo_screenheight()/3)) 
        self.window.iconbitmap('datavolley-master/Python/img/logo.ico')
        #self.window.rowconfigure(index=0, weight=1) 
        #self.window.columnconfigure(index=0, weight=1)

        menu = Menu(self.window)
        menu_item_file = Menu(menu, tearoff=0)
        menu_item_file.add_command(label='Open', command=self.openFile)
        menu_item_file.add_separator()
        menu_item_file.add_command(label='Save As', command=self.saveFile)
        menu_item_file.add_separator()
        menu_item_file.add_command(label='Exit', command=self.window.destroy)
        menu.add_cascade(label='File', menu=menu_item_file)

        menu_item_edit = Menu(menu, tearoff=0)
        menu_item_edit.add_command(label='Undo', command='')
        menu_item_edit.add_command(label='Undo All', command=self.undoAll)
        menu_item_edit.add_command(label='Redo', command='')
        menu.add_cascade(label='Edit', menu=menu_item_edit)
        
        menu_item_help = Menu(menu, tearoff=0)
        menu_item_help.add_command(label='About', command=self.about)
        menu.add_cascade(label='Help', menu=menu_item_help)

        self.window.config(menu=menu)


        self.lbl = tkinter.Label(self.window, text="Добро пожаловать в приложение DataVolley Master!", font=("Arial Bold", 16))  
        self.lbl.pack(fill='x')
        
        #self.btnExit = tkinter.Button(self.window, text="Выход", command=self.window.destroy)
        #self.btnExit.pack(fill='x', side='bottom')
        #self.btnOpen = tkinter.Button(self.window, text="Сохранить файл", command=self.saveFile)
        #self.btnOpen.pack(fill='x', side='bottom')
        #self.btnOpen = tkinter.Button(self.window, text="Undo All", command=self.undoAll)
        #self.btnOpen.pack(fill='x', side='bottom')
        #self.btnOpen = tkinter.Button(self.window, text="Открыть файл", command=self.openFile)
        #self.btnOpen.pack(fill='x', side='bottom')

        self.text = tkinter.StringVar()
        self.output = tkinter.Label(self.window, textvariable=self.text, font=("Arial Bold", 12))
        self.output.pack(fill='x')

        self.tab_control = tkinter.ttk.Notebook(self.window)  
        self.tab1 = tkinter.ttk.Frame(self.tab_control)  
        self.tab2 = tkinter.ttk.Frame(self.tab_control)  
        #self.tab3 = tkinter.ttk.Frame(self.tab_control) 
        self.tab_control.add(self.tab1, text='Game')  
        self.tab_control.add(self.tab2, text='Code') 
        #self.tab_control.add(self.tab3, text='Настройки')  
        self.lbl1 = tkinter.Label(self.tab1, text='[3INFO]')  
        self.lbl1.pack()  
        self.lbl2 = tkinter.Label(self.tab2, text='[3SCOUT]')  
        self.lbl2.pack() 
        #self.lbl3 = tkinter.Label(self.tab3, text='[3SETTINGS]')  
        #self.lbl3.pack()   
        self.tab_control.pack(expand=1, fill='both') 
        


        self.textGame = tkinter.StringVar()
        self.textResult = tkinter.StringVar()
        self.textDate = tkinter.StringVar()
        self.textTime = tkinter.StringVar()
        self.textSeason = tkinter.StringVar()
        self.textLeague = tkinter.StringVar()
        self.textPhase = tkinter.StringVar()
        self.textCity = tkinter.StringVar()
        self.textScout = tkinter.StringVar()
        self.textDocTime = tkinter.StringVar()


        self.outputtextGame = tkinter.Label(self.tab1, textvariable=self.textGame, font=("Arial Bold", 12))
        self.outputtextResult = tkinter.Label(self.tab1, textvariable=self.textResult, font=("Arial Bold", 12))
        self.outputtextDate = tkinter.Label(self.tab1, textvariable=self.textDate, font=("Arial Bold", 12))
        self.outputtextTime = tkinter.Label(self.tab1, textvariable=self.textTime, font=("Arial Bold", 12))
        self.outputtextSeason = tkinter.Label(self.tab1, textvariable=self.textSeason, font=("Arial Bold", 12))
        self.outputtextLeague = tkinter.Label(self.tab1, textvariable=self.textLeague, font=("Arial Bold", 12))
        self.outputtextPhase = tkinter.Label(self.tab1, textvariable=self.textPhase, font=("Arial Bold", 12))
        self.outputtextCity = tkinter.Label(self.tab1, textvariable=self.textCity, font=("Arial Bold", 12))
        self.outputtextScout = tkinter.Label(self.tab1, textvariable=self.textScout, font=("Arial Bold", 12))
        self.outputtextDocTime = tkinter.Label(self.tab1, textvariable=self.textDocTime, font=("Arial Bold", 12))


        self.outputtextGame.pack()
        #self.outputtextResult.pack()
        self.outputtextDate.pack()
        self.outputtextTime.pack()
        self.outputtextSeason.pack()
        self.outputtextLeague.pack()
        self.outputtextPhase.pack()
        self.outputtextCity.pack()
        self.outputtextScout.pack()
        self.outputtextDocTime.pack()
        

        '''
        self.cols = ('Code', 'ps', 'rd', '4', '5', '6', '7', 'Time', 'Set', '*z', 'az', 'F', '13', '14', 'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6') #27 column must be empty

        self.listBox = tkinter.ttk.Treeview(self.tab1, columns=self.cols, show='headings', selectmode="extended")
        self.scrollbar = ttk.Scrollbar(self.tab1, orient='vertical', command=self.listBox.yview)
        self.listBox.configure(yscroll=self.scrollbar.set) 
        self.scrollbar.pack(side='right', fill='both')
        for col in self.cols:
            self.listBox.heading(col, text=col)

        self.listBox.pack(fill='y', expand=1)
        '''

        self.cols2 = ('Main', 'Advanced', 'Extended', 'Custom') #27 column must be empty
        
        self.btnClean = tkinter.Button(self.tab2, text="Clean Custom", command=self.cleanCustom)
        self.btnServe = tkinter.Button(self.tab2, text="Serve Custom", command=self.serveCustom)
        self.listBox2 = tkinter.ttk.Treeview(self.tab2, columns=self.cols2, show='headings', selectmode="extended")
        self.scrollbar2 = ttk.Scrollbar(self.tab2, orient='vertical', command=self.listBox2.yview)
        self.listBox2.configure(yscroll=self.scrollbar2.set) 
        for col in self.cols2:
            self.listBox2.heading(col, text=col)

        self.scrollbar2.pack(side='right', fill='both')
        self.listBox2.pack(fill='y', expand=1, side='right', padx='5')
        self.btnClean.pack(padx='5')
        self.btnServe.pack(padx='5')


        tkinter.mainloop()

    def openFile(self):
        global openfilepath
        #self.listBox.delete(*self.listBox.get_children())
        self.listBox2.delete(*self.listBox2.get_children())
        openfilepath = filedialog.askopenfilename()
        read_dv.importFile(openfilepath)
        self.text.set("Открыт файл: "+ openfilepath)
        self.getMatchInfo()
        self.updateData()
        
        if read_dv.statusLoad:
            tkinter.messagebox.showinfo('DataVolley Master', 'Done')
        else:
            tkinter.messagebox.showerror('DataVolley Master', 'Error')

    def getMatchInfo(self):
        self.textGame.set(str(datavolley.Teams[0][1])  + ' - ' + str(datavolley.Teams[1][1]) + ' ( ' + str(datavolley.Teams[0][2]) + ' - ' + str(datavolley.Teams[1][2]) +' )')
        self.textDate.set('Date '+str(datavolley.Match[0][0]))
        self.textTime.set('Time '+str(datavolley.Match[0][1]))
        self.textSeason.set('Season '+str(datavolley.Match[0][2]))
        self.textLeague.set('League '+str(datavolley.Match[0][3]))
        self.textPhase.set('Phase '+str(datavolley.Match[0][4]))
        self.textCity.set('City '+str(datavolley.More[0][3]))
        self.textScout.set('Scout '+str(datavolley.More[0][5]))
        self.textResult.set(str(datavolley.Teams[0][2]) + ' - ' + str(datavolley.Teams[1][2]))
        self.textDocTime.set('Lastchange '+str(datavolley.dvwGame[0][8].split(' ')[1]) + ' '+str(datavolley.dvwGame[0][8].split(' ')[2]))
    
    def updateData(self):
        #self.listBox.delete(*self.listBox.get_children())
        self.listBox2.delete(*self.listBox2.get_children())
        status = False 
        #load.splitCategory(load.code)
        #for i in range(1,6):
            #for line in load.dvwGame[i]:
                #self.listBox.insert("", "end", values=line)
                #status = True
        datavolley.splitCategory(datavolley.dvwGame)
        for line in datavolley.codeCategory:
            self.listBox2.insert("", "end", values=line)
            status = True

    def undoAll(self):
        self.listBox2.delete(*self.listBox2.get_children())
        status = False 
        read_dv.importFile(openfilepath)
        datavolley.splitCategory(datavolley.dvwGame)
        for line in datavolley.codeCategory:
            self.listBox2.insert("", "end", values=line)
            status = True

    
    def saveFile(self):
        status = False 
        filepath = filedialog.asksaveasfilename()
        if filepath != "":
            write_dv.writeFile(filepath)
            status = True
        if status:
            self.listBox2.delete(*self.listBox2.get_children())
            read_dv.importFile(filepath)
            self.text.set("Открыт файл: "+ filepath)
            self.getMatchInfo()
            self.updateData()
            tkinter.messagebox.showinfo('DataVolley Master', 'Success')

        else:
            tkinter.messagebox.showerror('DataVolley Master', 'Error')
            self.saveFile()
    
    def about(self):
        tkinter.messagebox.showinfo('DataVolley Master', 'Version: 0.0.1')
    

    def cleanCustom(self):
        status = False
        if custom.customClean():
            status = True
        if status:
            tkinter.messagebox.showinfo('DataVolley Master', 'Clean')
            self.updateData()
        else:
            tkinter.messagebox.showerror('DataVolley Master', 'Error')
            datavolley.splitCategory(datavolley.dvwGame)
            self.undoAll()
    
    def serveCustom(self):
        status = False
        if custom.customServeNum():
            status = True
        if status:
            tkinter.messagebox.showinfo('DataVolley Master', 'Serve')
            self.updateData()
        else:
            tkinter.messagebox.showerror('DataVolley Master', 'Error')
            datavolley.splitCategory(datavolley.dvwGame)
            self.undoAll()