from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import tkinter
import os
from student import Student
from train import Train
from face_recognition import Face_Recognition

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
   
        #first image
        img=Image.open(r"images\im.jpg")
        img=img.resize((460,130))
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=460,height=130)

        #second image 
        img1=Image.open(r"images\eryh.jpeg")
        img1=img1.resize((460,130))
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=460,y=0,width=460,height=130)


        #third image
        img2=Image.open(r"images\hghg.jpeg")
        img2=img2.resize((460,130))
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=920,y=0,width=460,height=130)

        #bg image
        img3=Image.open(r"images\dfhf.jpeg")
        img3=img3.resize((1400,600))
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1400,height=600)



        #title lebel
        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDENCE SYSTEM SOFTWARE",font=("times new roman",30,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1400,height=45)
        


        #student button
        img4=Image.open(r"images\ffgh.jpeg")
        img4=img4.resize((220,220))
        self.photoimg4=ImageTk.PhotoImage(img4)


        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")  
        b1.place(x=130,y=65,width=200,height=200)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=130,y=250,width=200,height=40)



        #Detect face
        img5=Image.open(r"images\hghtgg.jpeg")
        img5=img5.resize((220,220))
        self.photoimg5=ImageTk.PhotoImage(img5)


        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=430,y=65,width=200,height=200)

        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=430,y=250,width=200,height=40)



        #Attendance
        img6=Image.open(r"images\attend.jpeg")
        img6=img6.resize((220,220))
        self.photoimg6=ImageTk.PhotoImage(img6)


        b1=Button(bg_img,image=self.photoimg6,cursor="hand2")
        b1.place(x=730,y=65,width=200,height=200)

        b1_1=Button(bg_img,text="Attendance",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=730,y=250,width=200,height=40)




        #help desk
        img7=Image.open(r"images\help.png")
        img7=img7.resize((220,220))
        self.photoimg7=ImageTk.PhotoImage(img7)


        b1=Button(bg_img,image=self.photoimg7,cursor="hand2")
        b1.place(x=1030,y=65,width=200,height=200)

        b1_1=Button(bg_img,text="Help Desk",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1030,y=250,width=200,height=40)


        #train face button
        img8=Image.open(r"images\train.jpeg")
        img8=img8.resize((220,220))
        self.photoimg8=ImageTk.PhotoImage(img8)


        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=130,y=315,width=200,height=200)

        b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=130,y=500,width=200,height=40)


         #Photos button
        img9=Image.open(r"images\photo.jpeg")
        img9=img9.resize((220,220))
        self.photoimg9=ImageTk.PhotoImage(img9)


        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=430,y=315,width=200,height=200)

        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=430,y=500,width=200,height=40)



 #Developer button
        img10=Image.open(r"images\dev.jpeg")
        img10=img10.resize((220,220))
        self.photoimg10=ImageTk.PhotoImage(img10)


        b1=Button(bg_img,image=self.photoimg10,cursor="hand2")
        b1.place(x=730,y=315,width=200,height=200)

        b1_1=Button(bg_img,text="Developer",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=730,y=500,width=200,height=40)



         #Exit button
        img11=Image.open(r"images\ex.jpeg")
        img11=img11.resize((220,220))
        self.photoimg11=ImageTk.PhotoImage(img11)


        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.WExit)
        b1.place(x=1030,y=315,width=200,height=200)

        b1_1=Button(bg_img,text="Exit",cursor="hand2",command=self.WExit,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1030,y=500,width=200,height=40)



    def open_img(self):
        os.startfile("data")


    def WExit(self):
        self.WExit=tkinter.messagebox.askyesno("Face Recognition System","Are You Sure To Exit This Window",parent=self.root)
        if self.WExit>0:
            self.root.destroy()
        else:
            return



        #***********************Function Buttons************************
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    
        #***********************train Button************************
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)


    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

        









if __name__ =="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
