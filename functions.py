from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import pymysql

class ConnectorDB:
    def __init__(self, root):
        self.root = root
        self.root.geometry("850x590+300+100")
        self.root.title("Students Management System")
        self.root.resizable(width=False, height=False)
        self.root.iconbitmap("C:\python\Student Management system\icon.ico")

        def addstu():
            if stuID.get()=="" or fname.get()=="" or lname.get()=="":
                tkinter.messagebox.showerror("Students Management System", "Invalid input! please enter correct details")
            else:
                sqlCon = pymysql.connect(host="localhost", user="root", password="5gg9s4f*", database="students")
                cur = sqlCon.cursor()
                cur.execute("insert into students values(%s, %s, %s, %s, %s)",(fname.get(), lname.get(), stuID.get(), phone.get(), address.get()))
                sqlCon.commit()
                sqlCon.close()
                tkinter.messagebox.showinfo("Students Management System", "Record Entered Successfully!")

        def display():
            sqlCon = pymysql.connect(host="localhost", user="root", password="5gg9s4f*", database="students")
            cur = sqlCon.cursor()
            cur.execute("select * from students")
            result = cur.fetchall()
            if len(result) != 0:
                self.student_records.delete(*self.student_records.get_children())
                for row in result:
                    self.student_records.insert('', END, values=row)
                sqlCon.commit()
            sqlCon.close()

        def studentInfo(ev):
            viewInfo = self.student_records.focus()
            studentData = self.student_records.item(viewInfo)
            row = studentData["values"]
            fname.set(row[0])
            lname.set(row[1])
            stuID.set(row[2])
            phone.set(row[3])
            address.set(row[4])

        def update():
            sqlCon = pymysql.connect(host="localhost", user="root", password="5gg9s4f*", database="students")
            cur = sqlCon.cursor()
            cur.execute("update students set fname=%s, lname=%s, phone=%s, address=%s where stuID=%s", (fname.get(), lname.get(), phone.get(), address.get(), stuID.get()))
            sqlCon.commit()
            display()
            sqlCon.close()
            tkinter.messagebox.showinfo("Students Management System", "Record updated Successfully!")


        def delete():
            sqlCon = pymysql.connect(host="localhost", user="root", password="5gg9s4f*", database="students")
            cur = sqlCon.cursor()
            cur.execute("delete from students where stuID=%s", stuID.get())
            sqlCon.commit()
            display()
            sqlCon.close()
            tkinter.messagebox.showinfo("Students Management System", "Record deleted Successfully!")
            reset()


        def search():
            try:
                sqlCon = pymysql.connect(host="localhost", user="root", password="5gg9s4f*", database="students")
                cur = sqlCon.cursor()
                cur.execute("select * from students where stuID=%s", stuID.get())
                row = cur.fetchone()
                fname.set(row[0])
                lname.set(row[1])
                stuID.set(row[2])
                phone.set(row[3])
                address.set(row[4])
                sqlCon.commit()
            except:
                tkinter.messagebox.showinfo("Students Management System", "Not found!")
                reset()
            sqlCon.close()

        def reset():
            self.fname_entry.delete(0, END)
            self.lname_entry.delete(0, END)
            self.id_entry.delete(0, END)
            self.phone_entry.delete(0, END)
            self.address_entry.delete(0, END)

        def exitprogram():
            exitprogram = tkinter.messagebox.askyesno("Students Management System", "Do you really want to exit?")
            if exitprogram > 0:
                root.destroy()
                return

        mainFrame = Frame(self.root, bg="midnight blue", width=770, height=700, relief=RIDGE, bd=10)
        mainFrame.grid()

        titleFrame = Frame(mainFrame, bg="midnight blue", width=770, height=100, relief=RIDGE, bd=7)
        titleFrame.grid(row=0, column=0)

        topFrame = Frame(mainFrame, bg="midnight blue", width=770, height=500, relief=RIDGE, bd=5)
        topFrame.grid(row=1, column=0)

        leftFrame = Frame(topFrame, bg="midnight blue", width=770, height=400, relief=RIDGE, bd=5, padx=2)
        leftFrame.pack(side=LEFT)
        leftFrame1 = Frame(leftFrame, bg="midnight blue", width=600, height=180, relief=RIDGE, bd=5, padx=2, pady=4)
        leftFrame1.pack(side=TOP, padx=0, pady=0)

        rightFrame = Frame(topFrame, bg="midnight blue", width=100, height=400, relief=RIDGE, bd=5, padx=2)
        rightFrame.pack(side=RIGHT)
        rightFrame1 = Frame(rightFrame, bg="midnight blue", width=90, height=300, relief=RIDGE, bd=5, padx=2, pady=2)
        rightFrame1.pack(side=TOP)

        fname = StringVar()
        lname = StringVar()
        stuID = StringVar()
        phone = StringVar()
        address = StringVar()


        self.title_label = Label(titleFrame, text="Students Management System", font=("Arial Bold", 25), bg="midnight blue", fg="white", bd=7)
        self.title_label.grid(row=0, column=0, padx=165)

        self.fname_label = Label(leftFrame1, text="First name:", font=("Arial", 15), bg="midnight blue", fg="white", bd=7)
        self.fname_label.grid(row=1, column=0, sticky=W, padx=5)
        self.lname_label = Label(leftFrame1, text="Last name:", font=("Arial", 15), bg="midnight blue", fg="white", bd=7)
        self.lname_label.grid(row=2, column=0, sticky=W, padx=5)
        self.id_label = Label(leftFrame1, text="Student ID:", font=("Arial", 15), bg="midnight blue", fg="white", bd=7)
        self.id_label.grid(row=3, column=0, sticky=W, padx=5)
        self.phone_label = Label(leftFrame1, text="Phone number:", font=("Arial", 15), bg="midnight blue", fg="white", bd=7)
        self.phone_label.grid(row=4, column=0, sticky=W, padx=5)
        self.address_label = Label(leftFrame1, text="Address:", font=("Arial", 15), bg="midnight blue", fg="white", bd=7)
        self.address_label.grid(row=5, column=0, sticky=W, padx=5)

        self.fname_entry = Entry(leftFrame1, width=44, bd=5, fg="midnight blue", font=("times new roman", 15), justify="left", textvariable=fname)
        self.fname_entry.grid(row=1, column=1, sticky=W, padx=5)
        self.lname_entry = Entry(leftFrame1, width=44, bd=5, fg="midnight blue", font=("times new roman", 15), justify="left", textvariable=lname)
        self.lname_entry.grid(row=2, column=1, sticky=W, padx=5)
        self.id_entry = Entry(leftFrame1, width=44, bd=5, fg="midnight blue", font=("times new roman", 15), justify="left", textvariable=stuID)
        self.id_entry.grid(row=3, column=1, sticky=W, padx=5)
        self.phone_entry = Entry(leftFrame1, width=44, bd=5, fg="midnight blue", font=("times new roman", 15), justify="left", textvariable=phone)
        self.phone_entry.grid(row=4, column=1, sticky=W, padx=5)
        self.address_entry = Entry(leftFrame1, width=44, bd=5, fg="midnight blue", font=("times new roman", 15), justify="left", textvariable=address)
        self.address_entry.grid(row=5, column=1, sticky=W, padx=5)

        scroll_y = Scrollbar(leftFrame, orient=VERTICAL)
        self.student_records = ttk.Treeview(leftFrame, height=12, columns=("fname", "lname", "stuID", "phone", "address"), yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)

        self.student_records.heading("fname", text="First name")
        self.student_records.heading("lname", text="Last name")
        self.student_records.heading("stuID", text="Student ID")
        self.student_records.heading("phone", text="Phone number")
        self.student_records.heading("address", text="Address")

        self.student_records["show"] = "headings"

        self.student_records.column("fname", width=100)
        self.student_records.column("lname", width=100)
        self.student_records.column("stuID", width=100)
        self.student_records.column("phone", width=100)
        self.student_records.column("address", width=100)

        self.student_records.pack(fill=BOTH, expand=1)
        self.student_records.bind("<ButtonRelease-1>", studentInfo)

        #buttons
        self.add_btn = Button(rightFrame1, text="Add", font=("Arial", 15), bg="midnight blue", fg="white", width=8, height=2, bd=4, pady=1, padx=24, command=addstu)
        self.add_btn.grid(row=0, column=0, padx=1)
        self.display_btn = Button(rightFrame1, text="Display", font=("Arial", 15), bg="midnight blue", fg="white", width=8, height=2, bd=4, pady=1, padx=24, command=display)
        self.display_btn.grid(row=1, column=0, padx=1)
        self.update_btn = Button(rightFrame1, text="Update", font=("Arial", 15), bg="midnight blue", fg="white", width=8, height=2, bd=4, pady=1, padx=24, command=update)
        self.update_btn.grid(row=2, column=0, padx=1)
        self.del_btn = Button(rightFrame1, text="Delete", font=("Arial", 15), bg="midnight blue", fg="white", width=8, height=2, bd=4, pady=1, padx=24, command=delete)
        self.del_btn.grid(row=3, column=0, padx=1)
        self.search_btn = Button(rightFrame1, text="Search", font=("Arial", 15), bg="midnight blue", fg="white", width=8, height=2, bd=4, pady=1, padx=24, command=search)
        self.search_btn.grid(row=4, column=0, padx=1)
        self.reset_btn = Button(rightFrame1, text="Reset", font=("Arial", 15), bg="midnight blue", fg="white", width=8, height=2, bd=4, pady=1, padx=24, command=reset)
        self.reset_btn.grid(row=5, column=0, padx=1)
        self.exit_btn = Button(rightFrame1, text="Exit", font=("Arial", 15), bg="midnight blue", fg="white", width=8, height=2, bd=4, pady=1, padx=24, command=exitprogram)
        self.exit_btn.grid(row=6, column=0, padx=1)