# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 02:35:15 2022

@author: TiaaUser
"""
from tkinter import *
import sqlite3
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox

def User():
    
    root = Tk()
    root.title("Duplicate index")
    root.geometry('1150x600')
    root.config(bg="#AEB6BF")

    PLAN = StringVar()
    TASK = StringVar()
    NAME = StringVar()
    RVDDATE = StringVar()
    STATUS = StringVar()
    ENROLL = StringVar()
    ALLOC = StringVar()
    ROLL = StringVar()
    LOAN = StringVar()
    DISTR = StringVar()
    PYB = StringVar()

    List = ["Plan No", "Task id", "User", "Received date", "Status", "Enrollments", "Allocations", "Rollovers", "Loans","Distributions","Plan Year End"]
    

    def Database():
        with sqlite3.connect("Duplicate.db") as conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM `duplicate` ORDER BY `PLAN` ASC")
            fetch = cur.fetchall()
            for data in fetch:
                tree.insert('', 'end', values=(data))            

        
    # Search data by id     
    def SearchData():
        
        if PLAN.get() == "":
            tkMessageBox.showwarning('', 'Please enter the plan number', icon="warning")
        else:
            tree.delete(*tree.get_children())
            with sqlite3.connect("Duplicate.db") as conn:
                cur = conn.cursor()
                cur.execute("SELECT * FROM duplicate WHERE PLAN=?",(PLAN.get(),))
                fetch = cur.fetchall()
                for data in fetch:
                    tree.insert('', 'end', values=(data))
    


    # refreshing page
    def RefreshData():
        tree.delete(*tree.get_children())
        try: 
            with sqlite3.connect("Duplicate.db") as conn:
                cur = conn.cursor()
                cur.execute("UPDATE `duplicate` SET `PLAN` = ?, `TASK` = ?, `NAME` =?, `RVDDATE` = ?,  `STATUS` = ?, `ENROLL` = ?, `ALLOC` = ?, `ROLL` = ?, `LOAN` = ?, `DISTR` = ?, `PYB` = ? WHERE `TASK` = ?", (str(PLAN.get()), str(TASK.get()), str(NAME.get()), str(RVDDATE.get()), str(STATUS.get()), str(ENROLL.get()),str(ALLOC.get()),str(ROLL.get()),str(LOAN.get()),str(DISTR.get()),str(PYB.get()),str(TASK.get())))
                conn.commit()
                cur.execute("SELECT * FROM `duplicate` ORDER BY `PLAN` ASC")
                fetch = cur.fetchall()
                for data in fetch:
                    tree.insert('', 'end', values=(data))  
        except sqlite3.OperationalError :
             tkMessageBox.showwarning('', 'Please wait database is refreshing',  icon="warning")           
        PLAN.set("")
        TASK.set("")
        NAME.set("")
        RVDDATE.set("")
        STATUS.set("")
        ENROLL.set("")
        ALLOC.set("")
        ROLL.set("")
        LOAN.set("")
        DISTR.set("")
        PYB.set("")
    
   
    # Serach window by plan
    def SearchWindow():
        global SearchWindow
        PLAN.set("")
        SearchWindow = Toplevel()
        SearchWindow.title("Search Data")
        width = 400
        height = 150
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = ((screen_width/2) - 455) - (width/2)
        y = ((screen_height/2) + 20) - (height/2)
        SearchWindow.geometry("%dx%d+%d+%d" % (width, height, x, y))

        #===================FRAMES==============================
        FormTitle = Frame(SearchWindow)
        FormTitle.pack(side=TOP)
        ContactForm = Frame(SearchWindow)
        ContactForm.pack(side=TOP, pady=10)

        #===================LABELS==============================
        lbl_title = Label(FormTitle, text="Search by Plan Number", font=('arial', 16), bg="#AEB6BF",  width = 300)
        lbl_title.pack(fill=X)
        lbl_User_id = Label(ContactForm, text=List[0], font=('arial', 14), bd=5)
        lbl_User_id.grid(row=0, sticky=W)

        #===================ENTRY===============================
        user = Entry(ContactForm, textvariable=PLAN, font=('arial', 14))
        user.grid(row=0, column=1) 
        #==================BUTTONS==============================
        btn_addcon = Button(ContactForm, text="Search", width=50, command=SearchData) #SubmitData
        btn_addcon.grid(row=4, columnspan=2, pady=10)  

    def OnSelected(event):
        global mem_id, UpdateWindow
        curItem = tree.focus()
        contents =(tree.item(curItem))
        selecteditem = contents['values']
        #IDX_ID = selecteditem[0]
        #PLAN= selecteditem[0]
        PLAN.set("")
        TASK.set("")
        NAME.set("")
        RVDDATE.set("")
        STATUS.set("")
        ENROLL.set("")
        ALLOC.set("")
        ROLL.set("")
        LOAN.set("")
        DISTR.set("")
        PYB.set("")
        PLAN.set(selecteditem[0])
        TASK.set(selecteditem[1])
        NAME.set(selecteditem[2])
        RVDDATE.set(selecteditem[3])
        STATUS.set(selecteditem[4])
        ENROLL.set(selecteditem[5])
        ALLOC.set(selecteditem[6])
        ROLL.set(selecteditem[7])
        LOAN.set(selecteditem[8])
        DISTR.set(selecteditem[9])
        PYB.set(selecteditem[10])
        UpdateWindow = Toplevel()
        UpdateWindow.title("Update Window")
        width = 400
        height = 450
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = ((screen_width/2) + 450) - (width/2)
        y = ((screen_height/2) + 20) - (height/2)
        UpdateWindow.geometry("%dx%d+%d+%d" % (width, height, x, y))
        if 'NewWindow' in globals():
            tkMessageBox.showerror(title=None, message="Close existing window", icon="warning")

        #===================FRAMES==============================
        FormTitle = Frame(UpdateWindow)
        FormTitle.pack(side=TOP)
        ContactForm = Frame(UpdateWindow)
        ContactForm.pack(side=TOP, pady=10)

        #===================LABELS==============================
        lbl_title = Label(FormTitle, text="Updating Task Details", font=('arial', 16), bg="silver",  width = 300)
        lbl_title.pack(fill=X)

        for i in range(0,len(List)):
            lbl_User_id = Label(ContactForm, text=List[i], font=('arial', 14), bd=5)
            lbl_User_id.grid(row=(i), sticky=W)
        plans = Entry(ContactForm, textvariable=PLAN, font=('arial', 14))
        plans.grid(row=0, column=1)
        tasks = Entry(ContactForm, textvariable=TASK, font=('arial', 14))
        tasks.grid(row=1, column=1)
        names = Entry(ContactForm, textvariable=NAME, font=('arial', 14))
        names.grid(row=2, column=1)
        rvddate = Entry(ContactForm, textvariable=RVDDATE,  font=('arial', 14))
        rvddate.grid(row=3, column=1)
        statuss = Entry(ContactForm, textvariable=STATUS,  font=('arial', 14))
        statuss.grid(row=4, column=1)
        enrolls= Entry(ContactForm, textvariable=ENROLL,  font=('arial', 14))
        enrolls.grid(row=5, column=1)
        allocs = Entry(ContactForm, textvariable=ALLOC,  font=('arial', 14))
        allocs.grid(row=6, column=1)
        rolls = Entry(ContactForm, textvariable=ROLL,  font=('arial', 14))
        rolls.grid(row=7, column=1)
        loans = Entry(ContactForm, textvariable=LOAN,  font=('arial', 14))
        loans.grid(row=8, column=1)
        distr = Entry(ContactForm, textvariable=DISTR,  font=('arial', 14))
        distr.grid(row=9, column=1)
        pybs = Entry(ContactForm, textvariable=PYB,  font=('arial', 14))
        pybs.grid(row=10, column=1)
        

    Top = Frame(root, width=500, bd=1, relief=SOLID)
    Top.pack(side=TOP)
    Mid = Frame(root, width=0,  bg="#AEB6BF")
    Mid.pack(side=TOP)
    MidLeft = Frame(Mid, width=50)
    MidLeft.pack(side=LEFT, pady=10)
    MidLeftPadding = Frame(Mid, width=370, bg="#AEB6BF")
    MidLeftPadding.pack(side=LEFT)
    MidRight = Frame(Mid, width=50)
    MidRight.pack(side=RIGHT, pady=10)
    TableMargin = Frame(root, width=500)
    TableMargin.pack(side=TOP)
    lbl_title = Label(Top, text="Plan Audit Duplicate Index", font=('arial', 16), width=500)
    lbl_title.pack(fill=X)


    #============================TABLES======================================
    scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
    scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
    tree = ttk.Treeview(TableMargin, columns=("ID", "User_Id", "Plan No", "Task id", "User", "Received date", "Status", "Enrollments", "Allocations", "Rollovers", "Loans","Distributions","Plan Year End"), height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    style = ttk.Style()
    
    Database()
    btn_Refresh = Button(MidLeft, text="REFRESH", bg="#AEB6BF",width=10, command=RefreshData) #DeleteData
    btn_Refresh.pack(side=LEFT)
 
    
    btn_add = Button(MidRight, text="SEARCH", bg="#AEB6BF",width=10, command=SearchWindow) #AddNewWindow
    btn_add.pack(side=LEFT)
    
 

    style.configure("Treeview", lightcolor="#AEB6BF", bordercolor="#AEB6BF",darkcolor="#000000")
    style.map("Treeview",background = [('selected','#000000')])
    style.theme_use("clam")
    style.configure("Treeview.Heading", background="#F0F8FF",foreground='blue',  bordercolor="sie",darkcolor="#ffc61e")
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    for i in range(len(List)):
        tree.heading(i, text=List[i], anchor=CENTER)
        if i == 0:
            tree.column('#0', stretch=NO, minwidth=0, width=0, anchor=CENTER)
        else:
            tree.column(f'#{i}', stretch=NO, minwidth=0, width=95, anchor=CENTER)
    tree.pack()
    tree.bind('<Double-Button-1>',OnSelected) # OnSelected