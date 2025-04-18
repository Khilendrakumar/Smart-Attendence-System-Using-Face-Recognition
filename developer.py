from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2




class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl=Label(self.root,text="Developer",font=("times new roman",30,"bold"),bg="white",fg="orange")
        title_lbl.place(x=0,y=0,width=1400,height=45)

        img_top=Image.open(r"F:\face racognition system\images\fgfhghghggfg.jpeg")
        
        self.photoimg_top=ImageTk.PhotoImage(img_top)






if __name__ =="__main__":
  root=Tk()
  obj=Developer(root)
  root.mainloop()