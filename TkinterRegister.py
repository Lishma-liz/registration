#Import Statements


from tkinter import *
import tkinter.messagebox as m
from PIL import ImageTk,Image

#function defined

def submit_form():
#Retrieves the text entered in the fields.
    
    name=name_entry.get().strip()
    password=password_entry.get().strip()
    email=email_entry.get().strip()
    contact_number=contact_number_entry.get().strip()
    address=address_entry.get().strip()
    
 #DB connection
    if name=='' or email=='' or password=='' or contact_number=='' or address=='':
        m.showwarning('error','check your fields!!!')
    else:
        import pymysql as pm
        connect=pm.connect(host="localhost",user="root",password="1234",db="auth52")
        c=connect.cursor()

# c.execute('insert into register(name,password,email,contact_number,address) values (%s, %s, %s, %s, %s)')
        c.execute("insert into register (name,password,email,contact_number,address) values (' "+name+" ',' "+password+" ',' "+email+" ',' "+contact_number+" ',' "+address+" ')")
        connect.commit()
     
        m.showinfo('good','saved!!!')
        connect.close()
    

#Prints the retrieved field to the console.
    print(f"name:{name}")
    print(f"password:{password}")
    print(f"Email:{email}")
    print(f"Contact Number:{contact_number}")
    print(f"Address:{address}")


def login():
  
    logemail=logemail_entry.get().strip()
    logpass=logpassword_entry.get().strip()
   
    
   

    import pymysql as pm
   
    connect=pm.connect(host="localhost",user="root",password="1234",db="auth52")
    c=connect.cursor()
    uq= 'UPDATE register SET email=TRIM(email),password=TRIM(password)'
    q=("select * from register where email=%s AND password=%s")
    c.execute(uq)
    
    c.execute(q,(logemail,logpass))
    re=c.fetchone()
    connect.commit()
    
    


    if re != None:
        m.showinfo('loged In','You ARE WELCOME!!!')
    else:
        m.showerror('!!!', 'You dont have account here')

    connect.close()

#GUI Setup

rt=Tk()
rt.geometry('1000x500') #width height
rt.title('Registration Form')

#Background Image
p=Image.open('C:/Users/lishm/Desktop/Profile/assets/Image/Registration.webp')
p=p.resize((1500,1500))
p=ImageTk.PhotoImage(p)
pic=Label(rt,image=p)
pic.place(x=0,y=0)



#Form Components

Button(rt,text="REGISTRATION FORM",bg='Black', fg='White',font=("Helvetica", 16, "italic")).pack(fill='x', padx=5)

Label(rt,text="Name:").place(x=20,y=60)
Label(rt,text="Password:").place(x=20,y=100)
Label(rt,text="Email:").place(x=20,y=140)
Label(rt,text="Contact No:").place(x=20,y=180)
Label(rt,text="Address").place(x=20,y=220)

#Input Fields
name_entry=Entry(rt)
password_entry=Entry(rt)
email_entry=Entry(rt)
contact_number_entry=Entry(rt)
address_entry=Entry(rt)

name_entry.place(x=120, y=60)
password_entry.place(x=120, y=100)
email_entry.place(x=120, y=140)
contact_number_entry.place(x=120, y=180)
address_entry.place(x=120, y=220)

Button(rt,text="Submit",command=submit_form,bg='Black',fg='White').place(x=140,y=280)

Label(rt,text="logEmail:").place(x=550,y=60)
Label(rt,text="logPassword:").place(x=550,y=100)

logemail_entry=Entry(rt)
logpassword_entry=Entry(rt)

logemail_entry.place(x=650, y=60)
logpassword_entry.place(x=650, y=100)

Button(rt,text="Login",command=login, bg='Black',fg='White').place(x=690,y=140)



rt.mainloop()


