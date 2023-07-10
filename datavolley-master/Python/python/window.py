#import main
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
        self.window.geometry('%dx%d' % (self.window.winfo_screenwidth()*2/3, self.window.winfo_screenheight()*2/3)) 
        #self.window.rowconfigure(index=0, weight=1) 
        #self.window.columnconfigure(index=0, weight=1)


        self.lbl = tkinter.Label(self.window, text="Добро пожаловать в приложение DataVolley Master!", font=("Arial Bold", 16))  
        self.lbl.pack(fill='x')
        
        self.btnExit = tkinter.Button(self.window, text="Выход", command=self.window.destroy)
        self.btnExit.pack(fill='x', side='bottom')
        self.btnOpen = tkinter.Button(self.window, text="Сохранить файл", command=self.saveFile)
        self.btnOpen.pack(fill='x', side='bottom')
        self.btnOpen = tkinter.Button(self.window, text="Открыть файл", command=self.openFile)
        self.btnOpen.pack(fill='x', side='bottom')

        
        self.text = tkinter.StringVar()
        self.output = tkinter.Label(self.window, textvariable=self.text, font=("Arial Bold", 12))
        self.output.pack(fill='x')


        self.cols = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27') 

        self.listBox = tkinter.ttk.Treeview(self.window, columns=self.cols, show='headings', selectmode="extended")
        self.scrollbar = ttk.Scrollbar(orient='vertical', command=self.listBox.yview)
        self.listBox.configure(yscroll=self.scrollbar.set) 
        self.scrollbar.pack(side='right', fill='both')
        for col in self.cols:
            self.listBox.heading(col, text=col)

        self.listBox.pack(fill='y', expand=1)






        tkinter.mainloop()

    def openFile(self):
        status = False 
        self.listBox.delete(*self.listBox.get_children())
        self.file = filedialog.askopenfilename()
        load.importFile(self.file)
        self.text.set(self.file)
        for line in load.dvwGame[3]:
            self.listBox.insert("", "end", values=line)
            status = True
    
        if status:
            tkinter.messagebox.showinfo('DataVolley Master', 'Загружено успешно')
        else:
            tkinter.messagebox.showerror('DataVolley Master', 'Ошибка загрузки')
    
    def saveFile(self):
        status = False 
        filepath = filedialog.asksaveasfilename()
        if filepath != "":
            with open(filepath, "w") as f:
                f.write(str(load.dvwGame))
        