from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #================Variables===============(Database MySql) Humko kuch bhi chiz add krni h to ispe krenge aur then current course information ke frames mein add krenge textvariable = self.var_Department
        self.var_Department = StringVar()
        self.var_Course = StringVar()
        self.var_Year = StringVar()
        self.var_Semester = StringVar()
        self.var_ID = StringVar()
        self.var_Name = StringVar()
        self.var_Admission_No = StringVar()
        self.var_Enroll = StringVar()
        self.var_Gender = StringVar()
        self.var_DOB = StringVar()
        self.var_Email = StringVar()
        self.var_Phone = StringVar()
        self.var_Address = StringVar()
        self.var_FatherName = StringVar()
        self.var_Photo = StringVar()
        self.var_radio1 = StringVar()

        #first image
        img = Image.open(r"C:\Users\nandi\OneDrive\Desktop\Face Recognization Attendance System\College Images\college.jpg")
        img = img.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image = self.photoimg)
        f_lbl.place(x=0,y=0,width=500, height=130)

        #second image
        img1 = Image.open(r"C:\Users\nandi\OneDrive\Desktop\Face Recognization Attendance System\College Images\student1.png")
        img1 = img1.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image = self.photoimg1) 
        f_lbl.place(x=500,y=0,width=500, height=130)

        #third image
        img2 = Image.open(r"C:\Users\nandi\OneDrive\Desktop\Face Recognization Attendance System\College Images\university.jpg")
        img2 = img2.resize((600,130),Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image = self.photoimg2)
        f_lbl.place(x=1000,y=0,width=550, height=130)

        #background image
        img3 = Image.open(r"C:\Users\nandi\OneDrive\Desktop\Face Recognization Attendance System\College Images\bgimage.jpg")
        img3 = img3.resize((1530,710),Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image = self.photoimg3)
        bg_img.place(x=0,y=130,width=1530, height=710)

        title_lbl = Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35, "bold"),bg = "white",fg= "red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame = Frame(bg_img,bd =2,bg="white")
        main_frame.place(x=20,y=55,width = 1480,height=600)

        # Left Label Frame

        Left_frame = LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=730,height=580)

        img_left = Image.open(r"C:\Users\nandi\OneDrive\Desktop\Face Recognization Attendance System\College Images\class.jpg")
        img_left = img_left.resize((800,130),Image.Resampling.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image = self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720, height=130)


        # Current course Information (Isme jo humare frames banre h mtlb chotu-chotu dabbe alag alag size ke)

        Current_course_frame = LabelFrame(Left_frame,bd=2,relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
        Current_course_frame.place(x=5,y=135,width=720,height=115)
        
        # Department

        department_label = Label(Current_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        department_label.grid(row = 0,column=0,padx=10)
        
        # Through this we get dropdown by combo box
        department_Combo=ttk.Combobox(Current_course_frame,textvariable=self.var_Department,font=("times new roman",12,"bold"),state="readonly") # Var_string part ko textvariable=self.var_Department se link krre hai
        department_Combo["values"]=("Select Department","Computer","IT","Civil","Mechanical") # Departments
        department_Combo.current(0)
        department_Combo.grid(row=0,column=1,padx=2,pady=10)

        # Course
        course_label = Label(Current_course_frame,text="Course",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row = 0,column=2,padx=10,sticky=W)
        # Through this we get dropdown by combo box
        course_Combo=ttk.Combobox(Current_course_frame,textvariable=self.var_Course,font=("times new roman",12,"bold"),state="readonly",width=20)
        course_Combo["values"]=("Select Course","BCA","MCA","B-Tech","M-Tech","BBA","MBA") # Departments
        course_Combo.current(0)
        course_Combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        # Year
        year_label = Label(Current_course_frame,text="Year",font=("times new roman",13,"bold"),bg="white")
        year_label.grid(row = 1,column=0,padx=10,sticky=W)
        # Through this we get dropdown by combo box
        year_Combo=ttk.Combobox(Current_course_frame,textvariable=self.var_Year,font=("times new roman",12,"bold"),state="readonly",width=20)
        year_Combo["values"]=("Select Year","2020-2021","2021-2022","2022-2023","2023-2024","2024-2025") # Departments
        year_Combo.current(0)
        year_Combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        # Semester
        Semester_label = Label(Current_course_frame,text="Semester",font=("times new roman",13,"bold"),bg="white")
        Semester_label.grid(row = 1,column=2,padx=10,sticky=W)
        # Through this we get dropdown by combo box
        Semester_Combo=ttk.Combobox(Current_course_frame,textvariable=self.var_Semester,font=("times new roman",12,"bold"),state="readonly",width=20)
        Semester_Combo["values"]=("Select Semester","Semester-1","Semester-2","Semester-3","Semester-4") # Departments
        Semester_Combo.current(0)
        Semester_Combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        # Class Student Information 
        Class_Student_frame = LabelFrame(Left_frame,bd=2,relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"))
        Class_Student_frame.place(x=5,y=250,width=720,height=300)
        
        # student id
        StudentID_Label = Label(Class_Student_frame,text="StudentID: ",font=("times new roman",13,"bold"),bg="white")
        StudentID_Label.grid(row =0,column=0,padx=10,sticky=W)

        StudentID_Entry= ttk.Entry(Class_Student_frame,textvariable=self.var_ID,width=20,font=("times new roman",13,"bold"))
        StudentID_Entry.grid(row=0,column=1,padx=10,sticky=W) # Isse entry fill bnra h student id ka

        #student name
        StudentName_Label = Label(Class_Student_frame,text="Student Name: ",font=("times new roman",13,"bold"),bg="white")
        StudentName_Label.grid(row =0,column=2,padx=10,pady=5,sticky=W)

        StudentName_Entry= ttk.Entry(Class_Student_frame,textvariable=self.var_Name,width=20,font=("times new roman",13,"bold"))
        StudentName_Entry.grid(row=0,column=3,padx=10,pady=5,sticky=W) 
        
        # Admission No.
        Admission_Label = Label(Class_Student_frame,text="Admission No: ",font=("times new roman",13,"bold"),bg="white")
        Admission_Label.grid(row =1,column=0,padx=10,pady=5,sticky=W)

        Admission_Entry= ttk.Entry(Class_Student_frame,textvariable=self.var_Admission_No,width=20,font=("times new roman",13,"bold"))
        Admission_Entry.grid(row=1,column=1,padx=10,pady=5,sticky=W) 
        
        # Enroll No
        Enroll_No_Label = Label(Class_Student_frame,text="Enroll No: ",font=("times new roman",13,"bold"),bg="white")
        Enroll_No_Label.grid(row =1,column=2,padx=10,pady=5,sticky=W)

        Enroll_No_Entry= ttk.Entry(Class_Student_frame,textvariable=self.var_Enroll,width=20,font=("times new roman",13,"bold"))
        Enroll_No_Entry.grid(row=1,column=3,padx=10,pady=5,sticky=W) 

        # Gender
        gender_Label = Label(Class_Student_frame,text="Gender: ",font=("times new roman",13,"bold"),bg="white")
        gender_Label.grid(row =2,column=0,padx=10,pady=5,sticky=W)

        # Through this we get dropdown by combo box
        gender_Combo=ttk.Combobox(Class_Student_frame,textvariable=self.var_Gender,font=("times new roman",12,"bold"),state="readonly",width=20)
        gender_Combo["values"]=("Male","Female","Other") 
        gender_Combo.current(0) 
        gender_Combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        # DOB
        DOB_Label = Label(Class_Student_frame,text="DOB: ",font=("times new roman",13,"bold"),bg="white")
        DOB_Label.grid(row =2,column=2,padx=10,pady=5,sticky=W)

        DOB_Entry= ttk.Entry(Class_Student_frame,textvariable=self.var_DOB,width=20,font=("times new roman",13,"bold"))
        DOB_Entry.grid(row=2,column=3,padx=10,pady=5,sticky=W) 
        
        # Email
        Email_Label = Label(Class_Student_frame,text="Email: ",font=("times new roman",13,"bold"),bg="white")
        Email_Label.grid(row =3,column=0,padx=10,pady=5,sticky=W)

        Email_Entry= ttk.Entry(Class_Student_frame,textvariable=self.var_Email,width=20,font=("times new roman",13,"bold"))
        Email_Entry.grid(row=3,column=1,padx=10,pady=5,sticky=W) 

        # Phone No
        phone_Label = Label(Class_Student_frame,text="Phone No: ",font=("times new roman",13,"bold"),bg="white")
        phone_Label.grid(row =3,column=2,padx=10,pady=5,sticky=W)

        phone_Entry= ttk.Entry(Class_Student_frame,textvariable=self.var_Phone,width=20,font=("times new roman",13,"bold"))
        phone_Entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        # Address
        Adress_Label = Label(Class_Student_frame,text="Address: ",font=("times new roman",13,"bold"),bg="white")
        Adress_Label.grid(row =4,column=0,padx=10,pady=5,sticky=W)

        Adress_Entry= ttk.Entry(Class_Student_frame,textvariable=self.var_Address,width=20,font=("times new roman",13,"bold"))
        Adress_Entry.grid(row=4,column=1,padx=10,pady=5,sticky=W) 

        # Father Name
        Father_Label = Label(Class_Student_frame,text="Father Name: ",font=("times new roman",13,"bold"),bg="white")
        Father_Label.grid(row =4,column=2,padx=10,pady=5,sticky=W)

        Father_Entry= ttk.Entry(Class_Student_frame,textvariable=self.var_FatherName,width=20,font=("times new roman",13,"bold"))
        Father_Entry.grid(row=4,column=3,padx=10,pady=5,sticky=W) 

        # Radio buttons
        radiobutton1= ttk.Radiobutton(Class_Student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobutton1.grid(row=6,column=0)

        
        radiobutton2= ttk.Radiobutton(Class_Student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobutton2.grid(row=6,column=1)

        # buttons frame 
        Button_frame = Frame(Class_Student_frame,bd=2,relief=RIDGE,bg="white")
        Button_frame.place(x=0,y=200,width=715,height=35)

        Save_Button = Button(Button_frame,text="Save",command=self.add_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        Save_Button.grid(row=0,column=0)

        Update_Button = Button(Button_frame,text="Update", command=self.update_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        Update_Button.grid(row=0,column=1)

        Delete_Button = Button(Button_frame,text="Delete",command=self.delete_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        Delete_Button.grid(row=0,column=2)

        Reset_Button = Button(Button_frame,text="Reset",command=self.reset_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        Reset_Button.grid(row=0,column=3)

        Button_frame1 = Frame(Class_Student_frame,bd=2,relief=RIDGE,bg="white")
        Button_frame1.place(x=0,y=235,width=715,height=35)

        Take_Photo_Button = Button(Button_frame1,command=self.generate_dataset,text="Take Photo Sample",width=35,font=("times new roman",13,"bold"),bg="blue",fg="white")
        Take_Photo_Button.grid(row=0,column=0)

        Update_Photo_Button = Button(Button_frame1,text="Update Photo Sample",width=35,font=("times new roman",13,"bold"),bg="blue",fg="white")
        Update_Photo_Button.grid(row=0,column=1)


        # Right Label Frame

        Right_frame = LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=750,y=10,width=740,height=580)

        img_right = Image.open(r"C:\Users\nandi\OneDrive\Desktop\Face Recognization Attendance System\College Images\students.jpg")
        img_right = img_right.resize((800,130),Image.Resampling.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(Right_frame, image = self.photoimg_right)
        f_lbl.place(x=5,y=0,width=720, height=130)

        #===============Search System===========================

        Search_frame = LabelFrame(Right_frame,bd=2,relief=RIDGE,text= "Search System",font=("times new roman",12,"bold"))
        Search_frame.place(x=5,y=135,width=725,height=70)

        Search_Label = Label(Search_frame,text="Search By: ",font=("times new roman",15,"bold"),bg="red",fg="white")
        Search_Label.grid(row =0,column=0,padx=10,pady=5,sticky=W)

        Search_Combo=ttk.Combobox(Search_frame,font=("times new roman",12,"bold"),state="readonly",width=20)
        Search_Combo["values"]=("Select","Student_ID","Phone No.") 
        Search_Combo.current(0)
        Search_Combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        Search_Entry= ttk.Entry(Search_frame,width=15,font=("times new roman",13,"bold"))
        Search_Entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        Search_Button = Button(Search_frame,text="Search",width=12,font=("times new roman",12,"bold"),bg="blue",fg="white")
        Search_Button.grid(row=0,column=3,padx=4)

        ShowAll_Button = Button(Search_frame,text="Show All",width=12,font=("times new roman",12,"bold"),bg="blue",fg="white")
        ShowAll_Button.grid(row=0,column=4,padx=4)


        #=====================Table Frame=============================
        Table_frame = Frame(Right_frame,bd=2,relief=RIDGE)
        Table_frame.place(x=5,y=210,width=725,height=350)

        scroll_x = ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Table_frame,orient=VERTICAL)

        self.student_table= ttk.Treeview(Table_frame,columns=("Department","Course","Year","Semester","ID","Name","Admission_No","Enroll","Gender","DOB","Email","Phone","Address","FatherName","Photo"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Department",text="Department")
        self.student_table.heading("Course",text="Course")
        self.student_table.heading("Year",text="Year")
        self.student_table.heading("Semester",text="Semester")
        self.student_table.heading("ID",text="ID")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Admission_No",text="Admission_No")
        self.student_table.heading("Enroll",text="Enroll")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("DOB",text="DOB")
        self.student_table.heading("Email",text="Email")
        self.student_table.heading("Phone",text="Phone")
        self.student_table.heading("Address",text="Address")
        self.student_table.heading("FatherName",text="FatherName")
        self.student_table.heading("Photo",text="Photo")
        self.student_table["show"]= "headings"

        self.student_table.column("Department",width=100)
        self.student_table.column("Course",width=100)
        self.student_table.column("Year",width=100)
        self.student_table.column("Semester",width=100)
        self.student_table.column("ID",width=100)
        self.student_table.column("Name",width=100)
        self.student_table.column("Admission_No",width=100)
        self.student_table.column("Enroll",width=100)
        self.student_table.column("Gender",width=100)
        self.student_table.column("DOB",width=100)
        self.student_table.column("Email",width=100)
        self.student_table.column("Phone",width=100)
        self.student_table.column("Address",width=100)
        self.student_table.column("FatherName",width=100)
        self.student_table.column("Photo",width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    #==============Function Declaration==============
    #Saves the data into the database

    def add_data(self):
        if self.var_Department.get()=="Select Department" or self.var_Name.get()=="" or self.var_ID.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="sona17@8#02NAN",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("Insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                self.var_Department.get(),
                                                                self.var_Course.get(),
                                                                self.var_Year.get(),
                                                                self.var_Semester.get(),
                                                                self.var_ID.get(),
                                                                self.var_Name.get(),
                                                                self.var_Admission_No.get(),
                                                                self.var_Enroll.get(),
                                                                self.var_Gender.get(),
                                                                self.var_DOB.get(),
                                                                self.var_Email.get(),
                                                                self.var_Phone.get(),
                                                                self.var_Address.get(),
                                                                self.var_FatherName.get(),
                                                                self.var_radio1.get()
                                    ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
            

        #================================fetch data=========================
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="sona17@8#02NAN",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #======================get cursor================================
    def get_cursor(self,event=""):
        cursor_focus= self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_Department.set(data[0])
        self.var_Course.set(data[1]),
        self.var_Year.set(data[2]),
        self.var_Semester.set(data[3]),
        self.var_ID.set(data[4]),
        self.var_Name.set(data[5]),
        self.var_Admission_No.set(data[6]),
        self.var_Enroll.set(data[7]),
        self.var_Gender.set(data[8]),
        self.var_DOB.set(data[9]),
        self.var_Email.set(data[10]),
        self.var_Phone.set(data[11]),
        self.var_Address.set(data[12]),
        self.var_FatherName.set(data[13]),
        self.var_radio1.set(data[14])

    #=================================Update function=======================

    def update_data(self):
        if self.var_Department.get() == "Select Department" or self.var_Name.get() == "" or self.var_ID.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
            return

        try:
            update = messagebox.askyesno("Update", "Do you want to update this student’s details?", parent=self.root)
            if not update:
                return

            conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="sona17@8#02NAN",
                database="face_recognizer"
            )
            my_cursor = conn.cursor()

        # Run the UPDATE query
            my_cursor.execute("""
            UPDATE student 
            SET Department=%s, Course=%s, Year=%s, Semester=%s, Name=%s, Admission_No=%s, 
                Enroll=%s, Gender=%s, DOB=%s, Email=%s, Phone=%s, Address=%s, FatherName=%s, Photo=%s 
            WHERE ID = %s
        """, (
            self.var_Department.get(),
            self.var_Course.get(),
            self.var_Year.get(),
            self.var_Semester.get(),
            self.var_Name.get(),
            self.var_Admission_No.get(),
            self.var_Enroll.get(),
            self.var_Gender.get(),
            self.var_DOB.get(),
            self.var_Email.get(),
            self.var_Phone.get(),
            self.var_Address.get(),
            self.var_FatherName.get(),
            self.var_radio1.get(),
            self.var_ID.get()
        ))

            conn.commit()
            conn.close()

            messagebox.showinfo("Success", "Student details successfully updated!", parent=self.root)
            self.fetch_data()

        except Exception as es:
            messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

    #==================Delete Function==========================

    def delete_data(self):
        if self.var_ID.get()=="":
            messagebox.showerror("Error","Student ID must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="sona17@8#02NAN",database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql = "Delete from student where ID=%s"
                    val=(self.var_ID.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

    #=========================Reset Function=====================================

    def reset_data(self):
        self.var_Department.set("Select Department")
        self.var_Course.set("Select Course")
        self.var_Year.set("Select Year")
        self.var_Semester.set("Select Semester")
        self.var_ID.set("")
        self.var_Name.set("")
        self.var_Admission_No.set("")
        self.var_Enroll.set("")
        self.var_Gender.set("Male")
        self.var_DOB.set("")
        self.var_Email.set("")
        self.var_Phone.set("")
        self.var_Address.set("")
        self.var_FatherName.set("")
        self.var_radio1.set("")

    #==========================Generate data set or take a photo samples======================

    def generate_dataset(self):
        if self.var_Department.get()=="Select Department" or self.var_Name.get()=="" or self.var_ID.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="sona17@8#02NAN",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set Department=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Admission_No=%s,Enroll=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,FatherName=%s,Photo=%s where ID = %s",(
                        self.var_Department.get(),
                        self.var_Course.get(),
                        self.var_Year.get(),
                        self.var_Semester.get(),
                        self.var_Name.get(),
                        self.var_Admission_No.get(),
                        self.var_Enroll.get(),
                        self.var_Gender.get(),
                        self.var_DOB.get(),
                        self.var_Email.get(),
                        self.var_Phone.get(),
                        self.var_Address.get(),
                        self.var_FatherName.get(),
                        self.var_radio1.get(),
                        self.var_ID.get()
                                        ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                #===========================LOAD predefined data on face frontals from opencv===============================

                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces= face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor =1.3
                    #minimum neighbour = 5

                    for (x,y,w,h) in faces:
                        face_cropped= img[y:y+h, x:x+w]
                        return face_cropped
                
                cap= cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame= cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face =cv2.resize(face_cropped(my_frame),(450,450))
                        face  =cv2.cvtColor(face,cv2.COLOR_BGR2GRAY) 
                        file_name_path= "data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets completed!!!")
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)



if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()