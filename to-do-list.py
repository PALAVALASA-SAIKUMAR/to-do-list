from tkinter import *
rt = Tk()
tasks_list = []
def opentaskfile():
     try:
         global tasks_list
         with open("tasklist.txt","r") as taskfile:
             tasks = taskfile.readlines()
         for task in tasks:
            if task != "\n":
                tasks_list.append(task)
                taskbox.insert(END,task)
     except:
        file=open("tasklist.txt","w")
        file.close()
def add():
    task = taske.get()
    taske.delete(0,END)
    if task:
        with open("tasklist.txt","a") as taskfile:
            taskfile.write(f"\n{task}")
            tasks_list.append(task)
            taskbox.insert(END,task)
def delete():
    task = str(taskbox.get(ANCHOR))
    if task in  tasks_list:
        tasks_list.remove(task)
        with open("tasklist.txt","w") as taskfile:
            for task in tasks_list:
                taskfile.write(task+"\n")
        taskbox.delete(ANCHOR)
rt.title("TO-DO-LIST")
rt.geometry("400x650+400+100")
rt.resizable(False,False)

Label(rt,text = "🎫     ▪▪▪TASKS▪▪▪     📜 ",font = ("Times",30,"bold"),bg = "#32405b",fg = "#cb410b").grid(row = 0,column= 0)
fr = Frame(rt,width = 418,height = 120,bg = "grey")
fr.grid(row = 1,column = 0)
tasks = StringVar()
taske = Entry(fr,width = 30,font = ("Courier New",20),bd = 0,bg = "#AFAEEE")
taske.place(x= 0,y = 20)
taske.focus()
Button(fr,text = "ADD",bg = "#002366",fg = "black",font = ("Courier New",20,"bold"),command = lambda :add()).place(x = 160,y = 60)
fr1 = Frame(rt,width = 418,height = 380,bg = "grey")
fr1.grid(row = 2,column = 0)
taskbox = Listbox(fr1,font = ("Courier New",20),bg = "#b2beb5",fg = "dark green",width = 22,height = 12,cursor = "hand2",selectbackground = "grey")
taskbox.pack(side = LEFT,fill = BOTH,padx = 2)
scroll = Scrollbar(fr1)
scroll.pack(side = RIGHT,fill = BOTH)
taskbox.config(yscrollcommand = scroll.set)
scroll.config(command = taskbox.yview)
opentaskfile()
Button(rt,text= "🗑",font= ( "ariel",20,"bold" ),fg = "red",bg  = "#b2beb5",command = lambda : delete()).grid(row = 4)
