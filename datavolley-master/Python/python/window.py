import settings
import load
import tkinter
from tkinter import filedialog
from tkinter import ttk

load.init()
#main.init()

class MyGui:
    def __init__(self):
        
        self.window = tkinter.Tk()
        self.window.title("DataVolley Master")
        self.window.geometry('%dx%d+%d+%d' % (self.window.winfo_screenwidth()*2/3, self.window.winfo_screenheight()*2/3, self.window.winfo_screenwidth()/2 - self.window.winfo_screenwidth()/3, self.window.winfo_screenheight()/2 - self.window.winfo_screenheight()/3)) 
        #self.window.rowconfigure(index=0, weight=1) 
        #self.window.columnconfigure(index=0, weight=1)


        self.lbl = tkinter.Label(self.window, text="Добро пожаловать в приложение DataVolley Master!", font=("Arial Bold", 16))  
        self.lbl.pack(fill='x')
        
        self.btnExit = tkinter.Button(self.window, text="Выход", command=self.window.destroy)
        self.btnExit.pack(fill='x', side='bottom')
        self.btnOpen = tkinter.Button(self.window, text="Сохранить файл", command=self.saveFile)
        self.btnOpen.pack(fill='x', side='bottom')
        self.btnOpen = tkinter.Button(self.window, text="Обновить", command=self.updateData)
        self.btnOpen.pack(fill='x', side='bottom')
        self.btnOpen = tkinter.Button(self.window, text="Открыть файл", command=self.openFile)
        self.btnOpen.pack(fill='x', side='bottom')

        self.text = tkinter.StringVar()
        self.output = tkinter.Label(self.window, textvariable=self.text, font=("Arial Bold", 12))
        self.output.pack(fill='x')

        self.tab_control = tkinter.ttk.Notebook(self.window)  
        self.tab1 = tkinter.ttk.Frame(self.tab_control)  
        self.tab2 = tkinter.ttk.Frame(self.tab_control)  
        self.tab3 = tkinter.ttk.Frame(self.tab_control) 
        self.tab_control.add(self.tab1, text='Игра')  
        self.tab_control.add(self.tab2, text='Код') 
        self.tab_control.add(self.tab3, text='Настройки')  
        self.lbl1 = tkinter.Label(self.tab1, text='[3SCOUT]')  
        self.lbl1.pack()  
        self.lbl2 = tkinter.Label(self.tab2, text=' ')  
        self.lbl2.pack() 
        self.lbl3 = tkinter.Label(self.tab3, text='Настройки')  
        self.lbl3.pack()   
        self.tab_control.pack(expand=1, fill='both') 
        



        self.cols = ('Code', 'ps', 'rd', '4', '5', '6', '7', 'Time', 'Set', '*z', 'az', 'F', '13', '14', 'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6') #27 column must be empty

        self.listBox = tkinter.ttk.Treeview(self.tab1, columns=self.cols, show='headings', selectmode="extended")
        self.scrollbar = ttk.Scrollbar(self.tab1, orient='vertical', command=self.listBox.yview)
        self.listBox.configure(yscroll=self.scrollbar.set) 
        self.scrollbar.pack(side='right', fill='both')
        for col in self.cols:
            self.listBox.heading(col, text=col)

        self.listBox.pack(fill='y', expand=1)


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

        self.listBox.delete(*self.listBox.get_children())
        self.listBox2.delete(*self.listBox2.get_children())
        self.file = filedialog.askopenfilename()
        load.importFile(self.file)
        self.text.set("Открыт файл: "+self.file)
        self.updateData()
        
        if load.statusLoad:
            tkinter.messagebox.showinfo('DataVolley Master', 'Загружено успешно')
        else:
            tkinter.messagebox.showerror('DataVolley Master', 'Ошибка загрузки')
    
    def updateData(self):
        self.listBox.delete(*self.listBox.get_children())
        self.listBox2.delete(*self.listBox2.get_children())
        status = False 
        for i in range(1,6):
            for line in load.dvwGame[i]:
                self.listBox.insert("", "end", values=line)
                status = True
        for line in load.code:
            self.listBox2.insert("", "end", values=line)
            status = True


    
    def saveFile(self):
        status = False 
        filepath = filedialog.asksaveasfilename()
        if filepath != "":
            with open(filepath, "w", encoding='latin-1') as f:
                for item in load.technical:
                    f.write("%s\n" % str(item))
                for item in load.set1+load.set2+load.set3+load.set4+load.set5+load.set6:
                    f.write( ";".join(str(a) for a in item) +"\n")
                status = True
        if status:
            tkinter.messagebox.showinfo('DataVolley Master', 'Сохранено')
        else:
            tkinter.messagebox.showerror('DataVolley Master', 'Ошибка при сохранении')