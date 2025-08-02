from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog


mydata = []
class Attendance:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #================variables=======================
        self.var_attendance_ID=StringVar()
        self.var_attendance_Enroll=StringVar()
        self.var_attendance_Name=StringVar()
        self.var_attendance_Department=StringVar()
        self.var_attendance_Time=StringVar()
        self.var_attendance_Date=StringVar()
        self.var_attendance_Attendance=StringVar()



        #first image
        img = Image.open(r"C:\Users\nandi\OneDrive\Desktop\Face Recognization Attendance System\College Images\attendance1.jpg")
        img = img.resize((800,200),Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image = self.photoimg)
        f_lbl.place(x=0,y=0,width=800, height=200)

        #second image
        img1 = Image.open(r"C:\Users\nandi\OneDrive\Desktop\Face Recognization Attendance System\College Images\attendance2.jpg")
        img1 = img1.resize((800,200),Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image = self.photoimg1) 
        f_lbl.place(x=800,y=0,width=800, height=200)

        #background image
        img3 = Image.open(r"C:\Users\nandi\OneDrive\Desktop\Face Recognization Attendance System\College Images\blue background.jpg")
        img3 = img3.resize((1530,710),Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image = self.photoimg3)
        bg_img.place(x=0,y=200,width=1530, height=710)

        title_lbl = Label(bg_img,text="ATTENDANCE MANAGEMENT SYSTEM",font=("times new roman",35, "bold"),bg = "white",fg= "red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame = Frame(bg_img,bd =2)
        main_frame.place(x=20,y=55,width = 1500,height=600)

        # Left Label Frame
        Left_frame = LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Attendance Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=730,height=580)

        img_left = Image.open(r"C:\Users\nandi\OneDrive\Desktop\Face Recognization Attendance System\College Images\class.jpg")
        img_left = img_left.resize((800,130),Image.Resampling.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image = self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720, height=130)

        left_insideframe = Frame(Left_frame,bd =2,relief=RIDGE,bg="white")
        left_insideframe.place(x=0,y=135,width = 720,height=370)

        # Labels Entry

        # Attendance id
        AttendanceID_Label = Label(left_insideframe,text="AttendanceID: ",font="comicsansns 11 bold",bg="white")
        AttendanceID_Label.grid(row =0,column=0,padx=10,pady=5,sticky=W)

        AttendanceID_Entry= ttk.Entry(left_insideframe,width=20,textvariable=self.var_attendance_ID,font=("times new roman",13,"bold"))
        AttendanceID_Entry.grid(row=0,column=1,padx=10,pady=5,sticky=W) 

        # Enroll
        Enroll_Label = Label(left_insideframe,text="Enroll No: ",font="comicsansns 11 bold",bg="white")
        Enroll_Label.grid(row =0,column=2,padx=4,pady=8)

        Enroll_Entry= ttk.Entry(left_insideframe,width=20,textvariable=self.var_attendance_Enroll,font="comicsansns 11 bold")
        Enroll_Entry.grid(row=0,column=3,pady=8)

        # Name
        Name_Label = Label(left_insideframe,text="Name: ",font="comicsansns 11 bold",bg="white")
        Name_Label.grid(row =1,column=0)

        Name_Entry= ttk.Entry(left_insideframe,width=20,textvariable=self.var_attendance_Name,font=("times new roman",13,"bold"))
        Name_Entry.grid(row=1,column=1,pady=8) 

        

        # Department
        Department_Label = Label(left_insideframe,text="Department: ",font="comicsansns 11 bold",bg="white")
        Department_Label.grid(row =1,column=2)

        Department_Entry= ttk.Entry(left_insideframe,width=20,textvariable=self.var_attendance_Department,font=("times new roman",13,"bold"))
        Department_Entry.grid(row=1,column=3,pady=8)

        # Time
        Time_Label = Label(left_insideframe,text="Time: ",font="comicsansns 11 bold",bg="white")
        Time_Label.grid(row =2,column=0)

        Time_Entry= ttk.Entry(left_insideframe,width=20,textvariable=self.var_attendance_Time,font=("times new roman",13,"bold"))
        Time_Entry.grid(row=2,column=1,pady=8)

        #Date
        Date_Label = Label(left_insideframe,text="Time: ",font="comicsansns 11 bold",bg="white")
        Date_Label.grid(row =2,column=2)

        Date_Entry= ttk.Entry(left_insideframe,width=20,textvariable=self.var_attendance_Date,font=("times new roman",13,"bold"))
        Date_Entry.grid(row=2,column=3,pady=8)

        #attendance
        attendanceLabel =Label(left_insideframe,text="Attendance Status",bg="white",font="comicsansns 11 bold")
        attendanceLabel.grid(row=3,column=0)

        self.attendance_status = ttk.Combobox(left_insideframe,width=20,textvariable=self.var_attendance_Attendance,font="comicsansns 11 bold",state="readonly")
        self.attendance_status["values"]=("Status","Present","Absent")
        self.attendance_status.grid(row=3,column=1,pady=8)
        self.attendance_status.current(0)


        # Button frame
        Button_frame = Frame(left_insideframe,bd=2,relief=RIDGE,bg="white")
        Button_frame.place(x=0,y=300,width=715,height=35)

        Save_Button = Button(Button_frame,text="Import csv",command=self.importCsv,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        Save_Button.grid(row=0,column=0)

        Update_Button = Button(Button_frame,text="Export csv",command=self.exportCsv,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        Update_Button.grid(row=0,column=1)

        Delete_Button = Button(Button_frame,text="Update",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        Delete_Button.grid(row=0,column=2)

        Reset_Button = Button(Button_frame,text="Reset",width=17,command=self.reset_data,font=("times new roman",13,"bold"),bg="blue",fg="white")
        Reset_Button.grid(row=0,column=3)



        # Right Label Frame
        Right_frame = LabelFrame(main_frame,bd=2,relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=750,y=10,width=720,height=580)

        table_frame = Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=700,height=455)

        #================================Scroll bar table======================================

        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable= ttk.Treeview(table_frame, column=("ID","Enroll","Name","Department","Time","Date","Attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("ID",text="Attendance ID")
        self.AttendanceReportTable.heading("Enroll",text=" Enroll")
        self.AttendanceReportTable.heading("Name",text="Name")
        self.AttendanceReportTable.heading("Department",text="Department")
        self.AttendanceReportTable.heading("Time",text="Time")
        self.AttendanceReportTable.heading("Date",text="Date")
        self.AttendanceReportTable.heading("Attendance",text="Attendance")

        self.AttendanceReportTable["show"] = "headings"   #table ke samne ka space remove krta h 
        
        self.AttendanceReportTable.column("ID",width=100)
        self.AttendanceReportTable.column("Enroll",width=100)
        self.AttendanceReportTable.column("Name",width=100)
        self.AttendanceReportTable.column("Department",width=100)
        self.AttendanceReportTable.column("Time",width=100)
        self.AttendanceReportTable.column("Date",width=100)
        self.AttendanceReportTable.column("Attendance",width=100)
    
        

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

        #==================================fetch data====================================

    def fetchData(self, rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)

    def importCsv(self):
        global mydata
        mydata.clear()
        filename = filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV", filetypes=(("CSV File", "*.csv"),("All File","*.*")),parent=self.root)
        with open(filename) as myfile:
            csvread = csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    #Export csv
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data found to export",parent=self.root)
                return False
            filename = filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV", filetypes=(("CSV File", "*.csv"),("All File","*.*")),parent=self.root)
            with open(filename,mode="w",newline="") as myfile:
                export_write = csv.writer(myfile,delimiter=",")
                for i in mydata:
                    export_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to "+os.path.basename(filename)+" successfully")
        except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

    def get_cursor(self,event=""):
        cursor_row= self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        row = content['values']
        self.var_attendance_ID.set(row[0])
        self.var_attendance_Enroll.set(row[1])
        self.var_attendance_Name.set(row[2])
        self.var_attendance_Department.set(row[3])
        self.var_attendance_Time.set(row[4])
        self.var_attendance_Date.set(row[5])
        self.var_attendance_Attendance.set(row[6])

    def reset_data(self):
        self.var_attendance_ID.set("")
        self.var_attendance_Enroll.set("")
        self.var_attendance_Name.set("")
        self.var_attendance_Department.set("")
        self.var_attendance_Time.set("")
        self.var_attendance_Date.set("")
        self.var_attendance_Attendance.set("")



if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()