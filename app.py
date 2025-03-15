

def addstudent():

    def submitadd():
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        addedtime = time.strftime("%H:%M:%S")
        addeddate = time.strftime("%d/%m/%y")

        try:
            sql = "INSERT INTO studentdetail (id,name,mobile,email,address,gender,dob,date,time) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            val =(id,name,mobile,email,address,gender,dob,addedtime,addeddate)
            mycursor.execute(sql, val)
            con.commit()
            res = messagebox.askyesno('Notifications','Data save Sucessfully \nDo you want to clear the form ?')
            if (res == True):
                idval.set('')
                nameval.set('')
                mobileval.set('')
                emailval.set('')
                addressval.set('')
                genderval.set('')
                dobval.set('')
        except:
            messagebox.showinfo('Notifications','unable to add record')

        strr = 'select * from studentdetail'
        mycursor.execute(strr)
        datas = mycursor.fetchall()

        studenttable.delete(*studenttable.get_children())
        for i in datas:
            vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
            studenttable.insert('',END,values=vv)
    #------------------------------------------------    
    addroot = Toplevel(master=DataEntryFrame)
    addroot.grab_set()
    addroot.geometry('470x470+220+200')
    addroot.title('Add New Student')
    addroot.config(bg='blue')
    addroot.resizable(False,False)

    #-------------------------------------------Labes
    idlabel = Label(addroot,text="Enter Id :",bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    idlabel.place(x=10,y=10)

    namelabel = Label(addroot,text="Enter Name :",bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    namelabel.place(x=10,y=70)
 
    mobilelabel = Label(addroot,text="Enter Mobile No :",bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    mobilelabel.place(x=10,y=130)
    
    emaillabel = Label(addroot,text="Enter Email :",bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    emaillabel.place(x=10,y=190)
    
    addresslabel = Label(addroot,text="Enter Address :",bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    addresslabel.place(x=10,y=250)
    
    genderlabel = Label(addroot,text="Enter Gender :",bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    genderlabel.place(x=10,y=310)
    
    doblabel = Label(addroot,text="Enter DOB :",bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    doblabel.place(x=10,y=370)

    #-------------------------------------------Textbox
    idval = StringVar()
    identry = Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=250,y=10)

    nameval = StringVar()
    nameentry = Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=nameval)
    nameentry.place(x=250,y=70)

    mobileval = StringVar()
    mobileentry = Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=mobileval)
    mobileentry.place(x=250,y=130)

    emailval = StringVar()
    emailentry = Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=emailval)
    emailentry.place(x=250,y=190)

    addressval = StringVar()
    addressentry = Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=addressval)
    addressentry.place(x=250,y=250)

    genderval = StringVar()
    genderentry = Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=genderval)
    genderentry.place(x=250,y=310)

    dobval = StringVar()
    dobentry = Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=dobval)
    dobentry.place(x=250,y=370)

    #-------------------------------------------Button
    submitbtn = Button(addroot,text='Submit',font=('roman',14,'bold'),bg='red',width=20,activebackground='blue',activeforeground='white',command=submitadd)
    submitbtn.place(x=130,y=420)
  
    addroot.mainloop()



#-------------------------------------------------------------------------------------------------------------------------------------------------------------



def searchstudent():
    
    def search():
        id = idval.get()
        name = nameval.get()
        addedtime = time.strftime("%H:%M:%S")
        addeddate = time.strftime("%d/%m/%y")

        try:


            sql = "SELECT * FROM studentdetail WHERE id = %s and name = %s"
            val = (id,name)
            mycursor.execute(sql,val)              
            datas = mycursor.fetchall()

            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                studenttable.insert('',END,values=vv)
            
        except:
            messagebox.showinfo('Notifications','unable to fetch record')

        
    #-------------------------------------------------------------------------------------------------------------------------------------    
    searchroot = Toplevel(master=DataEntryFrame)
    searchroot.grab_set()
    searchroot.geometry('470x200+220+200')
    searchroot.title('Search Student')
    searchroot.config(bg='blue')
    searchroot.resizable(False,False)

    #-------------------------------------------Labes
    idlabel = Label(searchroot,text="Enter Id :",bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    idlabel.place(x=10,y=10)

    namelabel = Label(searchroot,text="Enter Name :",bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    namelabel.place(x=10,y=70)

    
    #-------------------------------------------Textbox
    idval = StringVar()
    identry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=250,y=10)

    nameval = StringVar()
    nameentry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=nameval)
    nameentry.place(x=250,y=70)
    
    #-------------------------------------------Button
    submitbtn = Button(searchroot,text='Submit',font=('roman',14,'bold'),bg='red',width=20,activebackground='blue',activeforeground='white',command=search)
    submitbtn.place(x=130,y=140)
  
    searchroot.mainloop()



#-------------------------------------------------------------------------------------------------------------------------------------------------------------


def deletestudent():
    def delete():
        id = idval.get()
        name = nameval.get()
        addedtime = time.strftime("%H:%M:%S")
        addeddate = time.strftime("%d/%m/%y")

        try:


            sql = "DELETE FROM studentdetail WHERE id = %s and name = %s"
            val = (id,name)
            mycursor.execute(sql,val)              
            con.commit()
            res = messagebox.askyesno('Notifications','Data Delete Sucessfully \nDo you want to clear the form ?')
        except:
            messagebox.showinfo('Notifications','unable to delete record')


        strr = 'select * from studentdetail'
        mycursor.execute(strr)
        datas = mycursor.fetchall()

        studenttable.delete(*studenttable.get_children())
        for i in datas:
            vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
            studenttable.insert('',END,values=vv)



    #--------------------------------------------------------
    deleteroot = Toplevel(master=DataEntryFrame)
    deleteroot.grab_set()
    deleteroot.geometry('470x200+220+200')
    deleteroot.title('Delete Student')
    deleteroot.config(bg='blue')
    deleteroot.resizable(False,False)

    #----------------------------------------------------------------------------------------------------------------------------------------------------Labes
    idlabel = Label(deleteroot,text="Delete Id :",bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    idlabel.place(x=10,y=10)

    namelabel = Label(deleteroot,text="Delete Name :",bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    namelabel.place(x=10,y=70)
 
    #----------------------------------------------------------------------------------------------------------------------------------------------------------------Textbox
    idval = StringVar()
    identry = Entry(deleteroot,font=('roman',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=250,y=10)

    nameval = StringVar()
    nameentry = Entry(deleteroot,font=('roman',15,'bold'),bd=5,textvariable=nameval)
    nameentry.place(x=250,y=70)

    #---------------------------------------------------------------------------------------------------------------------------------------------------------------Button
    submitbtn = Button(deleteroot,text='Submit',font=('roman',14,'bold'),bg='red',width=20,activebackground='blue',activeforeground='white',command=delete)
    submitbtn.place(x=130,y=140)
  
    deleteroot.mainloop()




#-------------------------------------------------------------------------------------------------------------------------------------------------------------



def updatestudent():
    
    def update():
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        addedtime = time.strftime("%H:%M:%S")
        addeddate = time.strftime("%d/%m/%y")

        try:
            sql = "update studentdetail SET name = %s, mobile = %s, email = %s, address = %s, gender = %s, dob = %s where id = %s"
            val =(name,mobile,email,address,gender,dob,id)
            mycursor.execute(sql, val)
            con.commit()
            res = messagebox.askyesno('Notifications','Data save Sucessfully \nDo you want to clear the form ?')
            if (res == True):
                idval.set('')
                nameval.set('')
                mobileval.set('')
                emailval.set('')
                addressval.set('')
                genderval.set('')
                dobval.set('')
        except:
            messagebox.showinfo('Notifications','unable to update record')

        strr = 'select * from studentdetail'
        mycursor.execute(strr)
        datas = mycursor.fetchall()

        studenttable.delete(*studenttable.get_children())
        for i in datas:
            vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
            studenttable.insert('',END,values=vv)
    #----------------------------------------------------------------------------------------------------------         
    updateroot = Toplevel(master=DataEntryFrame)
    updateroot.grab_set()
    updateroot.geometry('470x470+220+200')
    updateroot.title('Update Student')
    updateroot.config(bg='blue')
    updateroot.resizable(False,False)

    #----------------------------------------------------------------------------------------------------------------------------------------------------Labes
    idlabel = Label(updateroot,text="Update Id :",bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    idlabel.place(x=10,y=10)

    namelabel = Label(updateroot,text="Update Name :",bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    namelabel.place(x=10,y=70)
 
    mobilelabel = Label(updateroot,text="Update Mobile No :",bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    mobilelabel.place(x=10,y=130)
    
    emaillabel = Label(updateroot,text="Update Email :",bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    emaillabel.place(x=10,y=190)
    
    addresslabel = Label(updateroot,text="Update Address :",bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    addresslabel.place(x=10,y=250)
    
    genderlabel = Label(updateroot,text="Update Gender :",bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    genderlabel.place(x=10,y=310)
    
    doblabel = Label(updateroot,text="Update DOB :",bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    doblabel.place(x=10,y=370)

    #----------------------------------------------------------------------------------------------------------------------------------------------------------------Textbox
    idval = StringVar()
    identry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=250,y=10)

    nameval = StringVar()
    nameentry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=nameval)
    nameentry.place(x=250,y=70)

    mobileval = StringVar()
    mobileentry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=mobileval)
    mobileentry.place(x=250,y=130)

    emailval = StringVar()
    emailentry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=emailval)
    emailentry.place(x=250,y=190)

    addressval = StringVar()
    addressentry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=addressval)
    addressentry.place(x=250,y=250)

    genderval = StringVar()
    genderentry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=genderval)
    genderentry.place(x=250,y=310)

    dobval = StringVar()
    dobentry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=dobval)
    dobentry.place(x=250,y=370)
    #---------------------------------------------------------------------------------------------------------------------------------------------------------------Button
    submitbtn = Button(updateroot,text='Submit',font=('roman',14,'bold'),bg='red',width=20,activebackground='blue',activeforeground='white',command=update)
    submitbtn.place(x=130,y=420)
  
    updateroot.mainloop()






#-------------------------------------------------------------------------------------------------------------------------------------------------------------



def showstudent():
    strr = 'select * from studentdetail'
    mycursor.execute(strr)
    datas = mycursor.fetchall()

    studenttable.delete(*studenttable.get_children())
    for i in datas:
        vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
        studenttable.insert('',END,values=vv)




#-------------------------------------------------------------------------------------------------------------------------------------------------------------
def exportstudent():
    ff = filedialog.asksaveasfilename(filetypes=[('.xlsx','*.xlsx'),('Text file','*.txt'),('CSV','*.csv'),('All File','*.*')])
    gg = studenttable.get_children()
    id,name,mobile,email,address,gender,dob,addeddate,addedtime=[],[],[],[],[],[],[],[],[]
    for i in gg:
        content = studenttable.item(i)
        pp = content['values']
        id.append(pp[0]),name.append(pp[1]),mobile.append(pp[2]),email.append(pp[3]),address.append(pp[4]),gender.append(pp[5]),
        dob.append(pp[6]),addeddate.append(pp[7]),addedtime.append(pp[8])
    dd = ['Id','Name','Mobile','Email','Address','Gender','D.O.B','Added Date','Added Time']
    df = pandas.DataFrame(list(zip(id,name,mobile,email,address,gender,dob,addeddate,addedtime)),columns=dd)
    paths = r'{}.csv'.format(ff)
    df.to_csv(paths,index=False)
    messagebox.showinfo('Notifications', 'Student data is Saved {}'.format(paths))
    


#-------------------------------------------------------------------------------------------------------------------------------------------------------------
def exitstudent():
    res = messagebox.askyesno('notification','Do you want to exit?')
    if(res==True):
        root.destroy()



#--------------------------------------------------------------------------------------------------------------------------------------------------------------

def Connectdb():
    
    def submitdb():
        global con
        global mycursor
        host = hostval.get()
        user = userval.get()
        password = passwordval.get()
        try:

            con = pymysql.connect(host=host,user=user,password=password)
            mycursor = con.cursor()
        except:
            messagebox.showerror('Notifications','Invalid Data try again')
            return

        try:
            strr = 'create database IF NOT EXISTS studentmanagmentsystem'
            mycursor.execute(strr)
            strr = 'use studentmanagmentsystem'
            mycursor.execute(strr)
            strr = 'create table IF NOT EXISTS studentdetail(id int primary key,name varchar(20),mobile varchar(12),email varchar(20),address varchar(100),gender varchar(50),dob varchar(50),date varchar(50),time varchar(50))'
            mycursor.execute(strr)
            messagebox.showinfo('Notifications','Database Connectd successfully')
        except:
            messagebox.showinfo('Notifications','unable to connect')



        strr = 'select * from studentdetail'
        mycursor.execute(strr)
        datas = mycursor.fetchall()

        studenttable.delete(*studenttable.get_children())
        for i in datas:
            vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
            studenttable.insert('',END,values=vv)
    
    
    dbroot = Toplevel()
    dbroot.grab_set()
    dbroot.geometry('420x250+800+230')
    dbroot.resizable(False,False)
    dbroot.config(bg='blue')
    dbroot.title('Connect To Database')

    #----------------------------------------------------------------------------
    hostlabel = Label(dbroot,text="Enter Host :",bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    hostlabel.place(x=10,y=10)

    userlabel = Label(dbroot,text="Enter User :",bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    userlabel.place(x=10,y=70)

    passwordlabel = Label(dbroot,text="Enter Password :",bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    passwordlabel.place(x=10,y=130)

    #----------------------------------------------------------------------------
    hostval = StringVar()
    userval = StringVar()
    passwordval = StringVar()

    hostentry = Entry(dbroot,font=('roman',14,'bold'),bd=5,textvariable=hostval)
    hostentry.place(x=225,y=10)

    userentry = Entry(dbroot,font=('roman',14,'bold'),bd=5,textvariable=userval)
    userentry.place(x=225,y=70)

    passwordentry = Entry(dbroot,font=('roman',14,'bold'),bd=5,textvariable=passwordval)
    passwordentry.place(x=225,y=130)

    #----------------------------------------------------------------------------
    submitbutton = Button(dbroot,text='Submit',font=('roman',14,'bold'),bg='red',width=20,
                          activebackground='blue',activeforeground='white',command=submitdb)
    submitbutton.place(x=150,y=190)

    
    dbroot.mainloop()




#--------------------------------------------------------------------------------------------------------------------------------------------------------------
def tick():
    date_string = time.strftime("%d/%m/%y")
    time_string = time.strftime("%H:%M:%S")
    clock.config(text='Date :' +date_string + '\n' +'Time :'+time_string)
    clock.after(200,tick)


def IntroLabelTick():
    global count,text
    if(count>=len(ss)):
        count=0
        text=''
    else:
        text = text+ss[count]
        count+=1
    SliderLabel.config(text=text)
    SliderLabel.after(200,IntroLabelTick)



#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
from tkinter import *
from tkinter import Toplevel,messagebox,filedialog
from tkinter.ttk import Treeview
from tkinter import ttk
import pymysql
import pandas
import time

root = Tk()
root.title("Student Management System")
root.config(bg ='gold2')
root.geometry('1174x700+200+50')
root.resizable(False,False)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
DataEntryFrame = Frame(root,bg='gold2',relief=GROOVE,borderwidth=5)
DataEntryFrame.place(x=10 ,y=80 ,width=500, height=600)

frontlabel = Label(DataEntryFrame,text="----------welcome----------",width=30,font=('arial',22,'italic bold'),bg='gold2')
frontlabel.pack(side=TOP,expand=True)


addbtn = Button(DataEntryFrame,text='1. Add Student',width=25,font=('chiller',20,'italic bold'),relief=RIDGE,bd=6,bg='skyblue3'
                       ,activebackground='blue',activeforeground='white',command=addstudent)
addbtn.pack(side=TOP,expand=True)


searchbtn = Button(DataEntryFrame,text='2. Search Student',width=25,font=('chiller',20,'italic bold'),relief=RIDGE,bd=6,bg='skyblue3'
                       ,activebackground='blue',activeforeground='white',command=searchstudent)
searchbtn.pack(side=TOP,expand=True)


deletebtn = Button(DataEntryFrame,text='3. Delete Student',width=25,font=('chiller',20,'italic bold'),relief=RIDGE,bd=6,bg='skyblue3'
                       ,activebackground='blue',activeforeground='white',command=deletestudent)
deletebtn.pack(side=TOP,expand=True)


updatebtn = Button(DataEntryFrame,text='4. Update Student',width=25,font=('chiller',20,'italic bold'),relief=RIDGE,bd=6,bg='skyblue3'
                       ,activebackground='blue',activeforeground='white',command=updatestudent)
updatebtn.pack(side=TOP,expand=True)


showbtn = Button(DataEntryFrame,text='5. Show All',width=25,font=('chiller',20,'italic bold'),relief=RIDGE,bd=6,bg='skyblue3'
                       ,activebackground='blue',activeforeground='white',command=showstudent)
showbtn.pack(side=TOP,expand=True)


exportbtn = Button(DataEntryFrame,text='6. Export Data',width=25,font=('chiller',20,'italic bold'),relief=RIDGE,bd=6,bg='skyblue3'
                       ,activebackground='blue',activeforeground='white',command=exportstudent)
exportbtn.pack(side=TOP,expand=True)



exitbtn = Button(DataEntryFrame,text='7. Exit',width=25,font=('chiller',20,'italic bold'),relief=RIDGE,bd=6,bg='skyblue3'
                       ,activebackground='blue',activeforeground='white',command=exitstudent)
exitbtn.pack(side=TOP,expand=True)




#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------


ShowDataFrame = Frame(root,bg='gold2',relief=GROOVE,borderwidth=5)
ShowDataFrame.place(x=550 ,y=80 ,width=620, height=600)



style = ttk.Style()
style.configure('Treeview.Heading',font=('chiller',20,'bold'),foreground='blue')
style.configure('Treeview',font=('times',15,'bold'),foreground='black',background='cyan')


scroll_x = Scrollbar(ShowDataFrame,orient=HORIZONTAL)
scroll_y = Scrollbar(ShowDataFrame,orient=VERTICAL)
studenttable = Treeview(ShowDataFrame,columns=('ID','NAME','MOBILE NO','EMAIL','ADDRESS','GENDER','DOB','ADDED DATE','ADDED TIME')
                        ,yscrollcommand=scroll_y ,xscrollcommand=scroll_x)
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x.config(command=studenttable.xview)
scroll_y.config(command=studenttable.yview)

studenttable.heading('ID',text='ID')
studenttable.heading('NAME',text='NAME')
studenttable.heading('MOBILE NO',text='MOBILE NO')
studenttable.heading('EMAIL',text='EMAIL')
studenttable.heading('ADDRESS',text='ADDRESS')
studenttable.heading('GENDER',text='GENDER')
studenttable.heading('DOB',text='DOB')
studenttable.heading('ADDED DATE',text='ADDED DATE')
studenttable.heading('ADDED TIME',text='ADDED TIME')

studenttable['show'] = 'headings'

studenttable.column('ID',width=100)
studenttable.column('NAME',width=200)
studenttable.column('MOBILE NO',width=200)
studenttable.column('EMAIL',width=200)
studenttable.column('ADDRESS',width=300)
studenttable.column('GENDER',width=100)
studenttable.column('DOB',width=150)
studenttable.column('ADDED DATE',width=150)
studenttable.column('ADDED TIME',width=150)

studenttable.pack(fill=BOTH,expand=1)



#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
ss = 'welcome to student management system'
count = 0
text=''

SliderLabel = Label(root,text=ss,font=('chiller',30,'italic bold'),relief=RIDGE,borderwidth=2,width=35,bg='cyan')
SliderLabel.place(x=260,y=0)
IntroLabelTick()   


clock = Label(root,font=('times',14,'bold'),relief=RIDGE,borderwidth=4,bg='lawn green')
clock.place(x=0,y=0)
tick()

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

connectbutton = Button(root,text='Connect To Database',width=23,font=('chiller',19,'italic bold'),relief=RIDGE,borderwidth=4,bg='green2'
                       ,activebackground='blue',activeforeground='white',command=Connectdb)
connectbutton.place(x=930,y=0)

root.mainloop()






