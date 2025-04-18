from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np




class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face_recognition System")


         #Title
        title_lbl=Label(self.root,text="F@CE RECOGNITION",font=("times new roman",30,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1400,height=45)

#left image
        img_top=Image.open(r"F:\face racognition system\images\ff.jpg")
        img_top=img_top.resize((650,660))
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=50,width=650,height=660)

#right image
        img_right=Image.open(r"F:\face racognition system\images\mdh.webp")
        img_right=img_right.resize((900,660))
        self.photoimg_right=ImageTk.PhotoImage(img_right)

#button
        f_lbl=Label(self.root,image=self.photoimg_right)
        f_lbl.place(x=650,y=50,width=720,height=660)


        b1_1=Button(f_lbl,text="FACE RECOGNITION",cursor="hand2",command=self.face_recog,font=("times new roman",15,"bold"),bg="yellow",fg="red")
        b1_1.place(x=199,y=485,width=314,height=50)
        #========================attendence==========================
    def mark_attendence(self,i,r,n,d):
        with open("khi.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%D/%M/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")





        #=========================face recognition function=========================
    def face_recog(self):
        def draw_boundry(img, classifier, scaleFactor, minNeighbours, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Fixed cvtColor issue
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbours)

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))

                conn = mysql.connector.connect(host="localhost", username="root", password="Khil@9105.gy", database="face_recognition_system")
                my_cursor = conn.cursor()

                my_cursor.execute("select Name from student where Student_id=" + str(id))
                n = my_cursor.fetchone()
                n = "+".join(n)

                my_cursor.execute("select Roll from student where Student_id=" + str(id))
                r = my_cursor.fetchone()
                r = "+".join(r)

                my_cursor.execute("select Dep from student where Student_id=" + str(id))
                d = my_cursor.fetchone()
                d = "+".join(d)

                my_cursor.execute("select Student_id from student where Student_id=" + str(id))
                i = my_cursor.fetchone()
                i = "+".join(i)


                if confidence > 77:
                    cv2.putText(img, f"ID:{i}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 25, 255), 3)
                    cv2.putText(img, f"Roll:{r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 25, 255), 3)
                    cv2.putText(img, f"Name:{n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 25, 255), 3)
                    cv2.putText(img, f"Department:{d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 25, 255), 3)
                    self.mark_attendence(i,r,n,d)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 25, 255), 3)

                coord = [x, y, w, h]

            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundry(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        Video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = Video_cap.read()
            if not ret:
                break
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome To Face Recognition", img)

            if  cv2.waitKey(1) == 13:  # Enter key to break the loop
                break

        Video_cap.release()
        cv2.destroyAllWindows()





if __name__ =="__main__":
  root=Tk()
  obj=Face_Recognition(root)
  root.mainloop()



  