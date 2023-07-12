import settings
import load
import tkinter
from tkinter import filedialog
from tkinter import ttk
from tkinter import Menu

load.init()
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
        menu_item = Menu(menu, tearoff=0)
        menu_item.add_command(label='Open', command=self.openFile)
        menu_item.add_separator()
        menu_item.add_command(label='Save As', command=self.saveFile)
        menu_item.add_separator()
        menu_item.add_command(label='Exit', command=self.window.destroy)
        menu.add_cascade(label='File', menu=menu_item)
        self.window.config(menu=menu)


        self.lbl = tkinter.Label(self.window, text="Добро пожаловать в приложение DataVolley Master!", font=("Arial Bold", 16))  
        self.lbl.pack(fill='x')
        
        #self.btnExit = tkinter.Button(self.window, text="Выход", command=self.window.destroy)
        #self.btnExit.pack(fill='x', side='bottom')
        #self.btnOpen = tkinter.Button(self.window, text="Сохранить файл", command=self.saveFile)
        #self.btnOpen.pack(fill='x', side='bottom')
        self.btnOpen = tkinter.Button(self.window, text="Обновить", command=self.updateData)
        self.btnOpen.pack(fill='x', side='bottom')
        #self.btnOpen = tkinter.Button(self.window, text="Открыть файл", command=self.openFile)
        #self.btnOpen.pack(fill='x', side='bottom')

        self.text = tkinter.StringVar()
        self.output = tkinter.Label(self.window, textvariable=self.text, font=("Arial Bold", 12))
        self.output.pack(fill='x')

        self.tab_control = tkinter.ttk.Notebook(self.window)  
        self.tab1 = tkinter.ttk.Frame(self.tab_control)  
        self.tab2 = tkinter.ttk.Frame(self.tab_control)  
        #self.tab3 = tkinter.ttk.Frame(self.tab_control) 
        self.tab_control.add(self.tab1, text='Игра')  
        self.tab_control.add(self.tab2, text='Код') 
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


        self.outputtextGame = tkinter.Label(self.tab1, textvariable=self.textGame, font=("Arial Bold", 12))
        self.outputtextResult = tkinter.Label(self.tab1, textvariable=self.textResult, font=("Arial Bold", 12))
        self.outputtextDate = tkinter.Label(self.tab1, textvariable=self.textDate, font=("Arial Bold", 12))
        self.outputtextTime = tkinter.Label(self.tab1, textvariable=self.textTime, font=("Arial Bold", 12))
        self.outputtextSeason = tkinter.Label(self.tab1, textvariable=self.textSeason, font=("Arial Bold", 12))
        self.outputtextLeague = tkinter.Label(self.tab1, textvariable=self.textLeague, font=("Arial Bold", 12))
        self.outputtextPhase = tkinter.Label(self.tab1, textvariable=self.textPhase, font=("Arial Bold", 12))
        self.outputtextCity = tkinter.Label(self.tab1, textvariable=self.textCity, font=("Arial Bold", 12))
        self.outputtextScout = tkinter.Label(self.tab1, textvariable=self.textScout, font=("Arial Bold", 12))


        self.outputtextGame.pack()
        #self.outputtextResult.pack()
        self.outputtextDate.pack()
        self.outputtextTime.pack()
        self.outputtextSeason.pack()
        self.outputtextLeague.pack()
        self.outputtextPhase.pack()
        self.outputtextCity.pack()
        self.outputtextScout.pack()
        

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

        self.listBox2 = tkinter.ttk.Treeview(self.tab2, columns=self.cols2, show='headings', selectmode="extended")
        self.scrollbar2 = ttk.Scrollbar(self.tab2, orient='vertical', command=self.listBox2.yview)
        self.listBox2.configure(yscroll=self.scrollbar2.set) 
        self.scrollbar2.pack(side='right', fill='both')
        for col in self.cols2:
            self.listBox2.heading(col, text=col)

        self.listBox2.pack(fill='y', expand=1)


        tkinter.mainloop()

    def openFile(self):

        #self.listBox.delete(*self.listBox.get_children())
        self.listBox2.delete(*self.listBox2.get_children())
        self.file = filedialog.askopenfilename()
        load.importFile(self.file)
        self.text.set("Открыт файл: "+self.file)
        self.getMatchInfo()
        self.updateData()
        
        if load.statusLoad:
            tkinter.messagebox.showinfo('DataVolley Master', 'Загружено успешно')
        else:
            tkinter.messagebox.showerror('DataVolley Master', 'Ошибка загрузки')

    def getMatchInfo(self):
        self.textGame.set(str(load.Teams[0][1])  + ' - ' + str(load.Teams[1][1]) + ' ( ' + str(load.Teams[0][2]) + ' - ' + str(load.Teams[1][2]) +' )')
        self.textDate.set('Date '+str(load.Match[0][0]))
        self.textTime.set('Time '+str(load.Match[0][1]))
        self.textSeason.set('Season '+str(load.Match[0][2]))
        self.textLeague.set('League '+str(load.Match[0][3]))
        self.textPhase.set('Phase '+str(load.Match[0][4]))
        self.textCity.set('City '+str(load.More[0][3]))
        self.textScout.set('Scout '+str(load.More[0][5]))
        self.textResult.set(str(load.Teams[0][2]) + ' - ' + str(load.Teams[1][2]))
    
    def updateData(self):
        #self.listBox.delete(*self.listBox.get_children())
        self.listBox2.delete(*self.listBox2.get_children())
        status = False 
        for i in range(1,6):
            for line in load.dvwGame[i]:
                #self.listBox.insert("", "end", values=line)
                status = True
        for line in load.codeCategory:
            self.listBox2.insert("", "end", values=line)
            status = True


    
    def saveFile(self):
        status = False 
        filepath = filedialog.asksaveasfilename()
        if filepath != "":
            with open(filepath, "w", encoding=load.text_encoding) as f:
                for item in load.technical:
                    f.write("%s\n" % str(item))
                for item in load.set1+load.set2+load.set3+load.set4+load.set5+load.set6:
                    f.write( ";".join(str(a) for a in item) +"\n")
                status = True
        if status:
            tkinter.messagebox.showinfo('DataVolley Master', 'Сохранено')
        else:
            tkinter.messagebox.showerror('DataVolley Master', 'Ошибка при сохранении')