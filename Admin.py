# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 02:29:38 2022

@author: TiaaUser
"""
from tkinter import *
import sqlite3
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
from tkinter import filedialog as fd
import pandas as pd
import pandas.io.sql as sql

def admin():
    
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
            cur.execute("CREATE TABLE IF NOT EXISTS `duplicate` ( PLAN INTEGER,TASK TEXT PRIMARY KEY  not null on conflict ignore ,NAME TEXT,RVDDATE INTEGER,STATUS DATE,ENROLL TEXT,ALLOC INTEGER,ROLL INTEGER,LOAN INTEGER,DISTR INTEGER,PYB DATE)" )
            cur.execute("SELECT * FROM `duplicate` ORDER BY `PLAN` ASC")
            fetch = cur.fetchall()
            for data in fetch:
                tree.insert('', 'end', values=(data))
                
    def AddNewWindow():
        global NewWindow
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
        NewWindow = Toplevel()
        NewWindow.title("Adding Records")
        width = 400
        height = 500
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = ((screen_width/2) - 455) - (width/2)
        y = ((screen_height/2) + 20) - (height/2)
        NewWindow.geometry("%dx%d+%d+%d" % (width, height, x, y))
        if 'UpdateWindow' in globals():
            UpdateWindow.destroy()

        #===================FRAMES==============================
        FormTitle = Frame(NewWindow)
        FormTitle.pack(side=TOP)
        ContactForm = Frame(NewWindow)
        ContactForm.pack(side=TOP, pady=10)

        #===================LABELS==============================
        lbl_title = Label(FormTitle, text="Adding Task Details", font=('arial', 16), bg="#AEB6BF",  width = 300)
        lbl_title.pack(fill=X)
    
        for i in range(0, len(List)):
            lbl_User_id = Label(ContactForm, text=List[i], font=('arial', 14), bd=5)
            lbl_User_id.grid(row=i, sticky=W)

        #===================ENTRY===============================
        user = Entry(ContactForm, textvariable=PLAN, font=('arial', 14))
        user.grid(row=0, column=1)
        task = Entry(ContactForm, textvariable=TASK, font=('arial', 14))
        task.grid(row=1, column=1)
        pln = Entry(ContactForm, textvariable=NAME, font=('arial', 14))
        pln.grid(row=2, column=1)
        tcount = Entry(ContactForm, textvariable=RVDDATE,  font=('arial', 14))
        tcount.grid(row=3, column=1)
        transc = Entry(ContactForm, textvariable=STATUS,  font=('arial', 14))
        transc.grid(row=4, column=1)
        enroll = Entry(ContactForm, textvariable=ENROLL,  font=('arial', 14))
        enroll.grid(row=5, column=1) 
        alloc = Entry(ContactForm, textvariable=ALLOC,  font=('arial', 14))
        alloc.grid(row=6, column=1) 
        roll = Entry(ContactForm, textvariable=ROLL,  font=('arial', 14))
        roll.grid(row=7, column=1) 
        loan = Entry(ContactForm, textvariable=LOAN,  font=('arial', 14))
        loan.grid(row=8, column=1) 
        distr = Entry(ContactForm, textvariable=DISTR,  font=('arial', 14))
        distr.grid(row=9, column=1) 
        pyb = Entry(ContactForm, textvariable=PYB,  font=('arial', 14))
        pyb.grid(row=10, column=1) 
        #==================BUTTONS==============================
        btn_addcon = Button(ContactForm, text="Save", width=50, command=SubmitData) #SubmitData
        btn_addcon.grid(row=11, columnspan=2, pady=10)

    def SubmitData():
        if  PLAN.get() == "" or TASK.get() == "" or NAME.get() == "" or RVDDATE.get() == "" or STATUS.get() == "" or ENROLL.get() == "" or ALLOC.get() == "" or ROLL.get() == "" or LOAN.get() == "" or DISTR.get() == "" or PYB.get() == "":
            tkMessageBox.showwarning('', 'Please Complete The Required Field', icon="warning")
        else:
            tree.delete(*tree.get_children())
            with sqlite3.connect("Duplicate.db") as conn:
                cur = conn.cursor()
                cur.execute("INSERT INTO `duplicate` (PLAN, TASK, NAME, RVDDATE, STATUS, ENROLL, ALLOC, ROLL, LOAN, DISTR,PYB ) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (str(PLAN.get()), str(TASK.get()), str(NAME.get()), str(RVDDATE.get()), str(STATUS.get()), str(ENROLL.get()),str(ALLOC.get()),str(ROLL.get()),str(LOAN.get()),str(DISTR.get()),str(PYB.get())))
                cur.execute("SELECT * FROM `duplicate` ORDER BY `PLAN` ASC")
                fetch = cur.fetchall()
            for data in fetch:
                tree.insert('', 'end', values=(data))
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
        tkMessageBox.showwarning('', 'Data succesuflly updated')    
        NewWindow.destroy()
        
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
    
    # Update data by id 
    def UpdateData():
        if TASK.get() == "":
            tkMessageBox.showwarning('', 'Please enter task id', icon="warning")
        elif  PLAN.get() == "":
            tkMessageBox.showwarning('', 'Please enter plan number', icon="warning")
        else:
            tree.delete(*tree.get_children())
            with sqlite3.connect("Duplicate.db") as conn:
                cur = conn.cursor()
                cur.execute("UPDATE `duplicate` SET `PLAN` = ?, `TASK` = ?, `NAME` =?, `RVDDATE` = ?,  `STATUS` = ?, `ENROLL` = ?, `ALLOC` = ?, `ROLL` = ?, `LOAN` = ?, `DISTR` = ?, `PYB` = ? WHERE `TASK` = ?", (str(PLAN.get()), str(TASK.get()), str(NAME.get()), str(RVDDATE.get()), str(STATUS.get()), str(ENROLL.get()),str(ALLOC.get()),str(ROLL.get()),str(LOAN.get()),str(DISTR.get()),str(PYB.get()),str(TASK.get())))
                conn.commit()
                cur.execute("SELECT * FROM `duplicate` ORDER BY `PLAN` ASC")
                fetch = cur.fetchall()
                for data in fetch:
                    tree.insert('', 'end', values=(data))
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
            tkMessageBox.showwarning('', 'Data succesuflly updated')
            UpdateWindow.destroy()

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
    
    
    """CSV file where csv data to be uploaded window code"""
    
    def open_file():
        # file type
        filetypes = (('csv files', '*.csv'),('Excel workbook', '*.xlsx'),('All files', '*.*'))
        # show the open file dialog
        fb = fd.askopenfile(filetypes=filetypes)
        try:
            csv_db(fb)
        except Exception as e:
            print("Something wrong with csv", e)
  
    """fetching csv data into data database"""       
    
    def csv_db(path):
        df = pd.read_csv(path, names =['PLAN', 'TASK', 'NAME', 'RVDDATE', 'STATUS', 'ENROLL', 'ALLOC', 'ROLL', 'LOAN', 'DISTR', 'PYB'])
        df.columns = df.columns.str.strip()
        
        try:
            with sqlite3.connect("Duplicate.db") as conn:
                cur = conn.cursor()
                df.to_sql('duplicate', conn, if_exists='append', index=False)
                cur.execute("SELECT * FROM `duplicate` ORDER BY `PLAN` ASC")
            tkMessageBox.showinfo(title='Window', message="Records sucessfully added")
        except sqlite3.IntegrityError:   
            tkMessageBox.showerror(title=None, message="Duplicate task id found", icon="warning")
  
    
    """Downloading data base to excel file""" 
    
    def excel_db():    
        try:
            with sqlite3.connect("Duplicate.db") as conn:
                sql_string = 'select * from duplicate'
                df = pd.read_sql(sql_string, con=conn)
                try:
                # with block automatically closes file
                    with fd.asksaveasfile(mode='w', defaultextension=".xlsx", title="Duplic") as file:
                        df.to_excel(file.name)
                except AttributeError:
                    # if user cancels save, filedialog returns None rather than a file object, and the 'with' will raise an error
                    print("The user cancelled save")
                tkMessageBox.showinfo(title='Window', message="Downloaded sucessfully...")
        except Exception:   
            tkMessageBox.showerror(title=None, message="Downloading failed", icon="warning")    
    
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
        width = 800
        height = 500
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
        lbl_title = Label(FormTitle, text="Updating Task Details", font=('arial', 16), bg="orange",  width = 300)
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
        

        #==================BUTTONS==============================
        btn_updatecon = Button(ContactForm, text="Update", width=50, command=UpdateData) #UpdateData
        btn_updatecon.grid(row=11, columnspan=2, pady=10)
    

            
    def DeleteData():
        if not tree.selection():
            result = tkMessageBox.showwarning('', 'Please select the record from table First!', icon="warning")
        else:
            result = tkMessageBox.askquestion('', 'Are you sure you want to delete this record?', icon="warning")
            if result == 'yes':
                curItem = tree.focus()
                contents =(tree.item(curItem))
                selecteditem = contents['values']
                tree.delete(curItem)
                with sqlite3.connect("Duplicate.db") as conn:
                    cur = conn.cursor()
                    cur.execute("DELETE FROM `duplicate` WHERE `PLAN` = %d" % selecteditem[0])

    Top = Frame(root, width=500, bd=1, relief=SOLID)
    Top.pack(side=TOP)
    Mid = Frame(root, width=0,  bg="#AEB6BF")
    Mid.pack(side=TOP)
    MidLeft = Frame(Mid, width=50)
    MidLeft.pack(side=LEFT, pady=10)
    MidLeftPadding = Frame(Mid, width=500, bg="#AEB6BF")
    MidLeftPadding.pack(side=LEFT)
    MidRight = Frame(Mid, width=50)
    MidRight.pack(side=RIGHT, pady=10)
    TableMargin = Frame(root, width=500)
    TableMargin.pack(side=TOP)
    lbl_title = Label(Top, text="Plan Audit Duplicate Index", font=('arial', 16), width=500)
    lbl_title.pack(fill=X)

    #============================ENTRY=======================================

    #============================BUTTONS=====================================


    #============================TABLES======================================
    scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
    scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
    tree = ttk.Treeview(TableMargin, columns=("ID", "User_Id", "Plan No", "Task id", "User", "Received date", "Status", "Enrollments", "Allocations", "Rollovers", "Loans","Distributions","Plan Year End"), height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    style = ttk.Style()
    
    # CAlling database
    Database()
    
    

    btn_add = Button(MidLeft, text="ADD", bg="#AEB6BF", width=10, command=AddNewWindow) #AddNewWindow
    btn_add.pack(side=LEFT)
    
    btn_Refresh = Button(MidLeft, text="REFRESH", bg="#AEB6BF",width=10, command=RefreshData) #DeleteData
    btn_Refresh.pack(side=LEFT)
    
    btn_add = Button(MidLeft, text="SEARCH", bg="#AEB6BF",width=10, command=SearchWindow) #AddNewWindow
    btn_add.pack(side=LEFT)
    
    
    btn_delete = Button(MidRight, text="DELETE", bg="#AEB6BF",width=10, command=DeleteData) #DeleteData
    btn_delete.pack(side=LEFT)
    
    btn_open = Button(MidRight, text="UPLOAD", bg="#AEB6BF",width=10, command=open_file) #Download_file # open_file
    btn_open.pack(side=LEFT)
    
    
    btn_open = Button(MidRight, text="EXCEL", bg="#AEB6BF",width=10, command=excel_db) #Download_file # open_file
    btn_open.pack(side=LEFT)


    style.configure("Treeview", lightcolor="#AEB6BF", bordercolor="#808080",darkcolor="#000000")
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