from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2




class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        #**************Variables*****************
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        self.var_radio1=StringVar()
        
        

        


        #first image
        img=Image.open(r"F:\face racognition system\images\st.jpeg")
        img=img.resize((460,130))
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=460,height=130)

        #second image 
        img1=Image.open(r"F:\face racognition system\images\stud.jpeg")
        img1=img1.resize((460,130))
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=460,y=0,width=460,height=130)


        #third image
        img2=Image.open(r"F:\face racognition system\images\stu.jpeg")
        img2=img2.resize((460,130))
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=920,y=0,width=460,height=130)


          #bg image
        img3=Image.open(r"F:\face racognition system\images\dfhf.jpeg")
        img3=img3.resize((1400,600))
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1400,height=600)

        #title lebel
        title_lbl=Label(bg_img,text="Student Management System",font=("times new roman",30,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1400,height=45)

        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=10,y=55,width=1350,height=510)

        #left lebel frame 
        Left_frame=LabelFrame(main_frame,bd=2,bg="white", relief=RIDGE,text="Students Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=0,width=660,height=505)


      
        img_left=Image.open(r"F:\face racognition system\images\stud.jpeg")
        img_left=img_left.resize((650,130))
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=650,height=80)


         #current course info
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white", relief=RIDGE,text="Current Course Info",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=50,width=650,height=110)
        #Department
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="readonly")
        dep_combo['values']=("Select Department","Computer Science","IT","Civil","Mechanical","Pharmacy")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)



      #Course
        course_label=Label(current_course_frame,text="Course",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),state="readonly")
        course_combo['values']=("Select course","B.Tech","Bsc IT","BCA","MCA","B.Com")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)



         #Year 
        year_label=Label(current_course_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="readonly")
        year_combo['values']=("Select Year","2020-21","2021-22","2022-23","2023-24","2024-25")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)



         #Semester
        sem_label=Label(current_course_frame,text="Semester",font=("times new roman",12,"bold"),bg="white")
        sem_label.grid(row=1,column=2,padx=10,sticky=W)

        sem_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),state="readonly")
        sem_combo['values']=("Select semester","I","II","III","IV","V","VI","VII","VIII")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)




         #class student  info
        class_Student_frame=LabelFrame(Left_frame,bd=2,bg="white", relief=RIDGE,text="Class Student Info",font=("times new roman",12,"bold"))
        class_Student_frame.place(x=5,y=160,width=650,height=320)

        #student ID
        studentId_label=Label(class_Student_frame,text="StudentID:",font=("times new roman",12,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)
          
        
        studentID_entry=ttk.Entry(class_Student_frame,textvariable=self.var_std_id,width=20,font=("times new roman",13,"bold"))
        studentID_entry.grid(row=0,column=1,padx=5,pady=5,sticky=W)



        #student name
        studentname_label=Label(class_Student_frame,text="Student Name:",font=("times new roman",12,"bold"),bg="white")
        studentname_label.grid(row=0,column=2,padx=5,pady=5,sticky=W)
          
        
        studentname_entry=ttk.Entry(class_Student_frame,textvariable=self.var_std_name,width=20,font=("times new roman",13,"bold"))
        studentname_entry.grid(row=0,column=3,padx=5,pady=5,sticky=W)



        #class division
        class_div_label=Label(class_Student_frame,text="Class Division:",font=("times new roman",12,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=5,pady=5,sticky=W)
        

        
        div_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_div,font=("times new roman",12,"bold"),state="readonly")
        div_combo['values']=("A","B","C")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)



        #roll no
        roll_no_label=Label(class_Student_frame,text="Roll No:",font=("times new roman",12,"bold"),bg="white")
        roll_no_label.grid(row=1,column=2,padx=5,pady=5,sticky=W)
          
        
        roll_no_entry=ttk.Entry(class_Student_frame,textvariable=self.var_roll,width=20,font=("times new roman",13,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=5,pady=5,sticky=W)



         #gender
        gender_label=Label(class_Student_frame,text="Gender:",font=("times new roman",12,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=5,pady=5,sticky=W)
          
        
        

        gender_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),state="readonly")
        gender_combo['values']=("Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=2,pady=10,sticky=W)




         #DOB
        dob_label=Label(class_Student_frame,text="DOB:",font=("times new roman",12,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=5,pady=5,sticky=W)
          
        
        dob_entry=ttk.Entry(class_Student_frame,textvariable=self.var_dob,width=20,font=("times new roman",13,"bold"))
        dob_entry.grid(row=2,column=3,padx=5,pady=5,sticky=W)




         #email
        email_label=Label(class_Student_frame,text="Email:",font=("times new roman",12,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=5,pady=5,sticky=W)
          
        
        email_entry=ttk.Entry(class_Student_frame,textvariable=self.var_email,width=20,font=("times new roman",13,"bold"))
        email_entry.grid(row=3,column=1,padx=5,pady=5,sticky=W)


        #phone number
        phone_label=Label(class_Student_frame,text="Phone No:",font=("times new roman",12,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=5,pady=5,sticky=W)
          
        
        phone_entry=ttk.Entry(class_Student_frame,textvariable=self.var_phone,width=20,font=("times new roman",13,"bold"))
        phone_entry.grid(row=3,column=3,padx=5,pady=5,sticky=W)



        #address
        addres_label=Label(class_Student_frame,text="Address:",font=("times new roman",12,"bold"),bg="white")
        addres_label.grid(row=4,column=0,padx=5,pady=5,sticky=W)
          
        
        addres_entry=ttk.Entry(class_Student_frame,textvariable=self.var_address,width=20,font=("times new roman",13,"bold"))
        addres_entry.grid(row=4,column=1,padx=5,pady=5,sticky=W)



        #Teacher name
        teacher_label=Label(class_Student_frame,text="Teacher Name:",font=("times new roman",12,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=5,pady=5,sticky=W)
          
        
        teacher_entry=ttk.Entry(class_Student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",13,"bold"))
        teacher_entry.grid(row=4,column=3,padx=5,pady=5,sticky=W)
       
        #radio buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=6,column=0)
        
        
        radiobtn2=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn2.grid(row=6,column=1)


        #buttons frame
        btn_frame=Frame(class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=215,width=645,height=37)


       #save btn
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)



        #update btn
        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)



        #delete btn
        Delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        Delete_btn.grid(row=0,column=2)




        #reset btn
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

      #buttons1 frame
        btn_frame1=Frame(class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=252,width=645,height=40)
        
        
        #take photo sample btn
        take_photo_btn=Button(btn_frame1,command=self.generate_dataset,text="Take Photo Sample",width=31,font=("times new roman",13,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0)



        #update btn
        update_photo_btn=Button(btn_frame1,text="Update Photo Sample",width=31,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=0,column=1)


        #right lebel frame 
        Right_frame=LabelFrame(main_frame,bd=2,bg="white", relief=RIDGE,text="Students Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=680,y=0,width=660,height=490)

        img_right=Image.open(r"F:\face racognition system\images\hghg.jpeg")
        img_right=img_right.resize((650,130))
        self.photoimg_right=ImageTk.PhotoImage(img_right)


        f_lbl=Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=650,height=80)



        #*****************Search System********************
       #search frame
        search_frame=LabelFrame(Right_frame,bd=2,bg="white", relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        search_frame.place(x=5,y=80,width=650,height=70)


        search_label=Label(search_frame,text="Search By:",font=("times new roman",12,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)



        search_combo=ttk.Combobox(search_frame,font=("times new roman",12,"bold"),state="readonly",width="15")
        search_combo['values']=("Select","Roll No","Phone No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)


        search_entry=ttk.Entry(search_frame,width=18,font=("times new roman",13,"bold"))
        search_entry.grid(row=0,column=2,padx=5,pady=5,sticky=W)


        #search btn
        search_btn=Button(search_frame,text="Search",width=10,font=("times new roman",13,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=2)




        #show all btn
        show_all_btn=Button(search_frame,text="Search All",width=10,font=("times new roman",13,"bold"),bg="blue",fg="white")
        show_all_btn.grid(row=0,column=4)


          #************table frame*****************
        table_frame=Frame(Right_frame,bd=2,bg="white", relief=RIDGE)
        table_frame.place(x=5,y=155,width=650,height=310)

        #scroll bar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)


        self.student_table=ttk.Treeview(table_frame,column=("Dep","Course","Year","Sem","ID","Name","Div","Roll No","Gender","DOB","Email","Phone No","Address","Teacher","Photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)


        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)


        self.student_table.heading("Dep",text="Department")
        self.student_table.heading("Course",text="Course")
        self.student_table.heading("Year",text="Year")
        self.student_table.heading("Sem",text="Semester")
        self.student_table.heading("ID",text="StudentId")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Div",text="Division")
        self.student_table.heading("Roll No",text="Roll No")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("DOB",text="DOB")
        self.student_table.heading("Email",text="Email")
        self.student_table.heading("Phone No",text="Phone No")
        self.student_table.heading("Address",text="Address")
        self.student_table.heading("Teacher",text="Teacher")
        self.student_table.heading("Photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"


        self.student_table.column("Dep",width=100)
        self.student_table.column("Course",width=100)
        self.student_table.column("Year",width=100)
        self.student_table.column("Sem",width=100)
        self.student_table.column("ID",width=100)
        self.student_table.column("Name",width=100)
        self.student_table.column("Div",width=100)
        self.student_table.column("Roll No",width=100)
        self.student_table.column("Gender",width=100)
        self.student_table.column("DOB",width=100)
        self.student_table.column("Email",width=100)
        self.student_table.column("Phone No",width=100)
        self.student_table.column("Address",width=100)
        self.student_table.column("Teacher",width=100)
        self.student_table.column("Photo",width=100)
        

        


        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
  
      #****************function declaration*******************
    def add_data(self):
        if self.var_dep.get=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are Required",parent=self.root)
        else:
          try:
            conn=mysql.connector.connect(host="localhost",username="root",password="Khil@9105.gy",database="face_recognition_system")
            my_cursor=conn.cursor()
            my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                            self.var_dep.get(),
                                                                                                            self.var_course.get(),
                                                                                                            self.var_year.get(),
                                                                                                            self.var_semester.get(),
                                                                                                            self.var_std_id.get(),
                                                                                                            self.var_std_name.get(),
                                                                                                            self.var_div.get(),
                                                                                                            self.var_roll.get(),
                                                                                                            self.var_gender.get(),
                                                                                                            self.var_dob.get(),
                                                                                                            self.var_email.get(),
                                                                                                            self.var_phone.get(),
                                                                                                            self.var_address.get(),
                                                                                                            self.var_teacher.get(),
                                                                                                            self.var_radio1.get()

                                                                                                        ))
            
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success","Student Details has been added successfully",parent=self.root)
          except Exception as es:
            messagebox.showerror("Error",f"Due To: {str(es)}",parent=self.root)



#************************fetch data***************************
    def fetch_data(self):
      conn=mysql.connector.connect(host="localhost",username="root",password="Khil@9105.gy",database="face_recognition_system")
      my_cursor=conn.cursor()
      my_cursor.execute("select * from student")
      data=my_cursor.fetchall()


      if len(data)!=0:
        self.student_table.delete(*self.student_table.get_children())
        for i in data:
          self.student_table.insert("",END,values=i)
          conn.commit()
      conn.close()




      #**************************get cursor for update*******************
    def get_cursor(self,event=""):
      cursor_focus=self.student_table.focus()
      content=self.student_table.item(cursor_focus)
      data=content["values"]

      self.var_dep.set(data[0]),
      self.var_course.set(data[1]),
      self.var_year.set(data[2]),
      self.var_semester.set(data[3]),
      self.var_std_id.set(data[4]),
      self.var_std_name.set(data[5]),
      self.var_div.set(data[6]),
      self.var_roll.set(data[7]),
      self.var_gender.set(data[8]),
      self.var_dob.set(data[9]),
      self.var_email.set(data[10]),
      self.var_phone.set(data[11]),
      self.var_address.set(data[12]),
      self.var_teacher.set(data[13]),
      self.var_radio1.set(data[14])



      #******************Update funcion**********************
    def update_data(self):
      if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
        messagebox.showerror("Error","All Fields are Required",parent=self.root)
      else:
        try:
          Upadate=messagebox.askyesno("Upad te","Do You Want To Update Student Details",parent=self.root)
          if Upadate>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="Khil@9105.gy",database="face_recognition_system")
            my_cursor=conn.cursor()
            my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                                                                                                                                                                self.var_dep.get(),
                                                                                                                                                                self.var_course.get(),
                                                                                                                                                                self.var_year.get(),
                                                                                                                                                                self.var_semester.get(),
                                                                                                                                                                self.var_std_name.get(),
                                                                                                                                                                self.var_div.get(),
                                                                                                                                                                self.var_roll.get(),
                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                self.var_dob.get(),
                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                self.var_phone.get(),
                                                                                                                                                                self.var_address.get(),
                                                                                                                                                                self.var_teacher.get(),
                                                                                                                                                                self.var_radio1.get(),
                                                                                                                                                                self.var_std_id.get()
                                                                                                                                                            ))
          else:
            if not Upadate:
              return
          messagebox.showinfo("Success","Student Details Updated Successfully",parent=self.root)
          conn.commit()
          self.fetch_data()
          conn.close()
        except Exception as es:
          messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

  #*****************Delete function*******************
    def delete_data(self):
      if self.var_std_id.get()=="":
        messagebox.showerror("Error","Student id must be required",parent=self.root)
      else:
        try:
          delete=messagebox.askyesno("Student Delete Page","Do You Want To Delete This Student",parent=self.root)
          if delete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="Khil@9105.gy",database="face_recognition_system")
            my_cursor=conn.cursor()
            sql="delete from student where Student_id=%s"
            val=(self.var_std_id.get(),)
            my_cursor.execute(sql,val)
          else:
            if not delete:
              return
          conn.commit()
          self.fetch_data()
          conn.close()
          messagebox.showinfo("Delete","Successfully delete student details",parent=self.root)
        except Exception as es:
          messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)



          #*************Reset Button**************
    def reset_data(self):
      self.var_dep.set("Select Department")
      self.var_course.set("Select Course")
      self.var_year.set("Select Year")
      self.var_semester.set("Select Semester")
      self.var_std_id.set("")
      self.var_std_name.set("")
      self.var_div.set("Select division")
      self.var_roll.set("")
      self.var_gender.set("Male")
      self.var_dob.set("")
      self.var_email.set("")
      self.var_phone.set("")
      self.var_address.set("")
      self.var_teacher.set("")
      self.var_radio1.set("")


      # Generating dataset taking photo sample
    def generate_dataset(self):
      if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
        messagebox.showerror("Error","All Fields are Required",parent=self.root)
      else:
        try:
          conn=mysql.connector.connect(host="localhost",username="root",password="Khil@9105.gy",database="face_recognition_system")
          my_cursor=conn.cursor()
          my_cursor.execute("select * from Student")
          myresult=my_cursor.fetchall()
          id=0
          for x in myresult:
            id+=1
          my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                                                                                                                                                                self.var_dep.get(),
                                                                                                                                                                self.var_course.get(),
                                                                                                                                                                self.var_year.get(),
                                                                                                                                                                self.var_semester.get(),
                                                                                                                                                                self.var_std_name.get(),
                                                                                                                                                                self.var_div.get(),
                                                                                                                                                                self.var_roll.get(),
                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                self.var_dob.get(),
                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                self.var_phone.get(),
                                                                                                                                                                self.var_address.get(),
                                                                                                                                                                self.var_teacher.get(),
                                                                                                                                                                self.var_radio1.get(),
                                                                                                                                                                self.var_std_id.get()==id+1
                                                                                                                                                            ))
          conn.commit()
          self.fetch_data()
          self.reset_data()
          conn.close()

          ###=====================================###
          face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

          def face_cropped(img):
            gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            faces=face_classifier.detectMultiScale(gray,1.3,5)
            #scaling factor=1.3
            #Minimum Neighbor=5
            for (x,y,w,h) in faces:
              face_cropped=img[y:y+h,x:x+w]
              return face_cropped
          cap=cv2.VideoCapture(0)
          img_id=0
          while True:
            ret,my_frame=cap.read()
            if face_cropped(my_frame) is not None:
              img_id+=1
              face=cv2.resize(face_cropped(my_frame),(450,450))
              face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
              file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
              cv2.imwrite(file_name_path,face)
              cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
              cv2.imshow("Crooped Face",face)

            if cv2.waitKey(1)==13 or int(img_id)==100:
              break
          cap.release()
          cv2.destroyAllWindows()
          messagebox.showinfo("Result","Generating data sets compled!!!!!!")


        except Exception as es:
          messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
      


            





if __name__ =="__main__":
  root=Tk()
  obj=Student(root)
  root.mainloop()