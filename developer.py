from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Developer:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root,text="DEVELOPER",font=("times new roman",35, "bold"),bg = "white",fg= "RED")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top = Image.open(r"C:\Users\nandi\OneDrive\Desktop\Face Recognization Attendance System\College Images\laptop1.jpeg")
        img_top = img_top.resize((1530,720),Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image = self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530, height=720)

        #Frame
        main_frame = Frame(f_lbl,bd =2,bg="white")
        main_frame.place(x=1000,y=0,width = 500,height=600)

         
        # img_top1 = Image.open(r"C:\Users\nandi\OneDrive\Desktop\Face Recognization Attendance System\College Images\developer1.jpg")
        # img_top1 = img_top1.resize((200,200),Image.Resampling.LANCZOS)
        # self.photoimg_top1 = ImageTk.PhotoImage(img_top1)

        # f_lbl = Label(main_frame, image = self.photoimg_top1)
        # f_lbl.place(x=300,y=0,width=200, height=200)


        # Developer Info
        department_label = Label(main_frame,text="Hello Everyone!!",font=("times new roman",20,"bold"),fg="blue",bg="white")
        department_label.place(x=0,y=5)

        department_label = Label(main_frame,text="We Nandini and Yagini developed this  ",font=("times new roman",20,"bold"),fg="blue",bg="white")
        department_label.place(x=0,y=40)

        department_label = Label(main_frame,text="Face Recognition Attendance System  ",font=("times new roman",20,"bold"),fg="blue",bg="white")
        department_label.place(x=0,y=80)

        department_label = Label(main_frame,text="project for our final year.",font=("times new roman",20,"bold"),fg="blue",bg="white")
        department_label.place(x=0,y=120)

        department_label = Label(main_frame,text="This project detects the face of the student ",font=("times new roman",20,"bold"),fg="blue",bg="white")
        department_label.place(x=0,y=160)

        department_label = Label(main_frame,text="and marks the attendance of the student  ",font=("times new roman",20,"bold"),fg="blue",bg="white")
        department_label.place(x=0,y=200)

        department_label = Label(main_frame,text="whether the student is present or not.  ",font=("times new roman",20,"bold"),fg="blue",bg="white")
        department_label.place(x=0,y=240)

        department_label = Label(main_frame,text="We developed this project using python ",font=("times new roman",20,"bold"),fg="blue",bg="white")
        department_label.place(x=0,y=280)

        department_label = Label(main_frame,text="and opencv. ",font=("times new roman",20,"bold"),fg="blue",bg="white")
        department_label.place(x=0,y=320)







        # img2 = Image.open(r"C:\Users\nandi\OneDrive\Desktop\Face Recognization Attendance System\College Images\university.jpg")
        # img2 = img2.resize((500,300),Image.Resampling.LANCZOS)
        # self.photoimg2 = ImageTk.PhotoImage(img2)

        # f_lbl = Label(main_frame, image = self.photoimg2)
        # f_lbl.place(x=0,y=210,width=500, height=300)




if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()