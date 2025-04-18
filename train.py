from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np




class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face_recognition System")
         
         
         #Title
        title_lbl=Label(self.root,text="TRAIN DATA SET",font=("times new roman",30,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1400,height=45)


   #top image
        
        img_top=Image.open(r"F:\face racognition system\images\im.jpg")
        img_top=img_top.resize((1400,280))
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=50,width=1400,height=280)


        #train Button
        b1_1=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman",15,"bold"),bg="red",fg="white")
        b1_1.place(x=0,y=330,width=1400,height=70)


     #bottom image
          
        img_bottom=Image.open(r"F:\face racognition system\images\hghtgg.jpeg")
        img_bottom=img_bottom.resize((1400,280))
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=0,y=400,width=1400,height=280)


    def train_classifier(self):
      data_dir=("data")
      path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
      
      faces=[]
      ids=[]

      for image in path:
        img=Image.open(image).convert('L')  #grayscale conversion of image
        imageNp=np.array(img,'uint8')  #datatype uint8
        id=int(os.path.split(image)[1].split('.')[1])
        
        faces.append(imageNp)
        ids.append(id)
        cv2.imshow("Training",imageNp)
        cv2.waitKey(1)==13
      ids=np.array(ids)

      #==================Train the classifier and save===================  
      clf=cv2.face.LBPHFaceRecognizer_create()
      clf.train(faces,ids)
      clf.write("classifier.xml")
      cv2.destroyAllWindows()
      messagebox.showinfo("Result","Training Dataset Completed")



      





if __name__ =="__main__":
  root=Tk()
  obj=Train(root)
  root.mainloop()