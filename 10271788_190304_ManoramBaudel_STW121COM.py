
from tkinter import *
from tkinter import ttk
import pickle
def create():
    d = {}
    my_file = open('userinfo.txt', 'ab')
    pickle.dump(d, my_file)
    my_file.close()
    e = {}
    my_file1 = open('employee.txt', 'ab')
    pickle.dump(e, my_file1)
    my_file1.close()
    dp = {}
    f = open('department.txt', 'ab')
    pickle.dump(dp, f)
    f.close()
def cmd():
    screen7.destroy()
    user_dashboard()
def exi():
    screen7.destroy()
def dep_view():
    file= open('department.txt','rb')
    load=pickle.load(file)
    for m,n in load.items():
        Label(screen7,text=n,fg='white',bg='#3333ff',font=(('samanata'),12)).pack()
    file.close()
def view_dep():
    global screen7
    global dpl
    screen3.destroy()
    screen7=Tk()
    screen7.geometry('440x580+0+0')
    screen7.configure(bg='#3333ff')
    Label(screen7, text='Departments', font=(('samanata'), 20, 'bold'), bg='white', fg='#3333ff', height=2,
          width=440).pack()
    Button(screen7, text='Back', font=(('samanata'), 10), width=8, command=cmd).place(x=20,y=520)
    Button(screen7, text='Exit', font=(('samanata'), 10), width=8, command=exi).place(x=340, y=520)
    dpl=Label(screen7,text="++Available Departments++")
    dpl.pack(padx=10,pady=10)
    dep_view()
    screen7.mainloop()
def confirm():
    d=d_id.get()
    dn=d_name.get()
    dictd={d:dn}
    fl=open('department.txt','rb+')
    c=pickle.load(fl)
    fl.close()
    if d=="":
        v.configure(text='Invalid Department ID!',fg='red')
    elif d in c:
        v.configure(text='Department ID Already Taken!',fg='red')
    elif dn=="":
        v.configure(text='Invalid Department Name!',fg='red')
    else:
        l=[]
        for i, j in c.items():
            l.append(j)
        if dn in l:
            v.configure(text='Department Already Exists!', fg='red')
        else:
            fil=open('department.txt','rb+')
            c.update(dictd)
            fil.seek(0)
            pickle.dump(c,fil)
            fil.close()
            v.configure(text='Department Created!',fg='green')
def res():
    en1.delete(0,END)
    en2.delete(0,END)
def bc():
    screen6.destroy()
    user_dashboard()
def add_department():
    global screen6
    global d_id
    global d_name
    global en1
    global en2
    global v
    screen3.destroy()
    screen6=Tk()
    screen6.geometry('440x580+0+0')
    screen6.configure(bg='#3333ff')
    d_id=StringVar()
    d_name=StringVar()
    Label(screen6, text='Employee Management', font=(('samanata'), 20, 'bold'), bg='white', fg='#3333ff', height=2,
          width=440).pack()
    Label(screen6, text='Department ID:', font=(('samanata'), 10), fg='white', bg='#3333ff').place(x=20,y=200)
    en1=Entry(screen6,textvariable=d_id)
    en1.place(x=150,y=205)
    Label(screen6, text='Department Name:', font=(('samanata'), 10), fg='white', bg='#3333ff').place(x=20, y=250)
    en2=Entry(screen6, textvariable=d_name)
    en2.place(x=150, y=255)
    Button(screen6,text='Confirm',command=confirm).place(x=180,y=300)
    Button(screen6, text='Back', font=(('samanata'), 10), width=8,command=bc).place(x=20, y=510)
    Button(screen6, text='Exit', font=(('samanata'), 10), width=8,command=screen6.destroy).place(x=330, y=510)
    Button(screen6, text='Reset', font=(('samanata'), 10), width=8, command=res).place(x=180,y=510)
    v=Label(screen6,text='')
    v.place(x=150,y=340)
    screen6.mainloop()
def search():
    em=emp_name.get()
    file= open('employee.txt','rb')
    c= pickle.load(file)
    for x,y in c.items():
        if x==em:
            s1.configure(text=em,font=(('samanata',12)))
            g=y[0]
            h=y[1]
            i=y[2]
            j=y[3]
            k=y[4]
            s2.configure(text=g,font=(('samanata',12)))
            s3.configure(text=h,font=(('samanata', 12)))
            s4.configure(text=i,font=(('samanata', 12)))
            s5.configure(text=j,font=(('samanata', 12)))
            s6.configure(text=k,font=(('samanata', 12)))
def h():
    screen5.destroy()
    user_dashboard()
def view():
    screen3.destroy()
    global screen5
    screen5 = Tk()
    screen5.geometry('440x580+0+0')
    screen5.configure(bg='#3333ff')
    global emp_name
    global s1
    global s2
    global s3
    global s4
    global s5
    global s6
    emp_name=StringVar()
    Label(screen5, text='Employee Management', font=(('samanata'), 20, 'bold'), bg='white', fg='#3333ff', height=2,
          width=440).pack()
    Label(screen5, text='',bg='#3333ff').pack()
    Label(screen5, text='',bg='#3333ff').pack()
    Label(screen5, text='',bg='#3333ff').pack()
    Label(screen5, text='',bg='#3333ff').pack()
    Label(screen5, text='',bg='#3333ff').pack()
    s1=Label(screen5, text='')
    s1.place(x=160,y=200)
    s2=Label(screen5,text='')
    s2.place(x=160,y=240)
    s3 = Label(screen5, text='')
    s3.place(x=160,y=280)
    s4 = Label(screen5, text='')
    s4.place(x=160,y=320)
    s5 = Label(screen5, text='')
    s5.place(x=160,y=360)
    s6 = Label(screen5, text='')
    s6.place(x=160,y=400)
    Label(screen5, text='Search Employee:',bg='#3333ff',fg='white').place(x=10,y=120)
    Entry(screen5,textvariable=emp_name).place(x=120,y=120)
    Button(screen5, text='Back', font=(('samanata'), 10), width=8,command=h).place(x=20,y=510)
    Button(screen5, text='Exit', font=(('samanata'), 10), width=8,command=screen5.destroy).place(x=330,y=510)
    Button(screen5, text='Search',width=8,command=search).place(x=250,y=120)
    Label(screen5, text='Name:',font=(('samanata'), 10),  bg='#3333ff', fg='white').place(x=50, y=200)
    Label(screen5, text='ID:',font=(('samanata'), 10),  bg='#3333ff', fg='white').place(x=50, y=240)
    Label(screen5, text='Age:',font=(('samanata'), 10),  bg='#3333ff', fg='white').place(x=50, y=280)
    Label(screen5, text='Address:',font=(('samanata'), 10),  bg='#3333ff', fg='white').place(x=50, y=320)
    Label(screen5, text='Contact:',font=(('samanata'), 10),  bg='#3333ff', fg='white').place(x=50, y=360)
    Label(screen5, text='Department:',font=(('samanata'), 10),  bg='#3333ff', fg='white').place(x=50, y=400)
    screen5.mainloop()
def save():
    i= id.get()
    nam=name.get()
    ag=age.get()
    adr=address.get()
    con=contact.get()
    dep=department.get()
    emp1={nam:[i,ag,adr,con,dep]}
    d_file=open('employee.txt','rb+')
    r=pickle.load(d_file)
    li=[]
    for m,n in r.items():
        li.append(n[0])
    d_file.close()
    if i=="":
        labl.configure(text='Invalid ID!',fg='red')
    elif i in li:
        labl.configure(text='ID Already Taken!', fg='red')
    elif nam=="":
        labl.configure(text='Please Check The Name!',fg='red')
    elif ag=="":
        labl.configure(text='Please Enter Valid Age!',fg='red')
    elif adr=="":
        labl.configure(text='Please Enter Valid Address!',fg='red')
    elif con=="":
        labl.configure(text='Please Provide Valid Contact!',fg='red')
    elif dep=='--Select Department--'or dep=="":
        labl.configure(text='Please Select A Department!',fg='red')
    else:
        f_file=open('employee.txt','rb+')
        r.update(emp1)
        f_file.seek(0)
        pickle.dump(r,f_file)
        f_file.close()
        labl.configure(text='Employee Added To The Department!', fg='green')
def reset():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
def ex():
    screen3.destroy()
    main_screen()
def b():
    screen4.destroy()
    user_dashboard()
def exit():
    screen3.destroy()
def add_employee():
    screen3.destroy()
    global screen4
    screen4 = Tk()
    screen4.geometry('440x580+0+0')
    screen4.configure(bg='#3333ff')
    global e1
    global e2
    global e3
    global e4
    global e5
    global id
    global labl
    global name
    global age
    global address
    global contact
    global department
    id=StringVar()
    name=StringVar()
    age=StringVar()
    address=StringVar()
    contact=StringVar()
    department=StringVar()
    Label(screen4, text='Employee Management', font=(('samanata'), 20,'bold'), bg='white',fg='#3333ff', height=2, width=440).pack()
    Label(screen4, text='',bg='#3333ff').pack()
    Label(screen4, text='ID*:', font=(('samanata'), 10),bg='#3333ff',fg='white').pack()
    e1=Entry(screen4,textvariable=id)
    e1.pack()
    Label(screen4, text='Full Name*:', font=(('samanata'), 10),bg='#3333ff',fg='white').pack()
    e2=Entry(screen4, textvariable=name)
    e2.pack()
    Label(screen4, text='Age*:', font=(('samanata'), 10),bg='#3333ff',fg='white').pack()
    e3=Entry(screen4, textvariable=age)
    e3.pack()
    Label(screen4, text='Address*:', font=(('samanata'), 10),bg='#3333ff',fg='white').pack()
    e4=Entry(screen4, textvariable=address)
    e4.pack()
    Label(screen4, text='Contact*:', font=(('samanata'), 10),bg='#3333ff',fg='white').pack()
    e5=Entry(screen4, textvariable=contact)
    e5.pack()
    Label(screen4, text='Department*:', font=(('samanata'), 10),bg='#3333ff',fg='white').pack()
#####################################################Department Addition#######################################################################################
    lt=[]
    f=open('department.txt','rb')
    w=pickle.load(f)
    for i,j in w.items():
        lt.append(j)
    f.close()
    box=ttk.Combobox(screen4,textvariable=department)
    box.set('--Select Department--')
    box['values']=lt
    box.pack()
    Label(screen4, text='').pack()
    labl=Label(screen4, text='')
    labl.pack()
    Button(screen4, text='Back', font=(('samanata'),10),width=8,command=b).pack(side='left',padx=60)
    Button(screen4, text='Save', font=(('samanata'),10),width=8,command=save).pack(side='right',padx=60)
    Button(screen4, text='Reset', font=(('samanata'),10),width=8,command=reset).pack(side='bottom',pady=51)
    screen4.mainloop()
def user_dashboard():
    global screen3
    screen3= Tk()
    screen3.geometry('440x580+0+0')
    screen3.configure(bg='#3333ff')
    Label(screen3, text='Dashboard', fg='#3333ff', font=('samanata', 20, 'bold'), bg='white', height=2, width=440).pack()
    Label(screen3,text='',bg='#3333ff').pack()
    Label(screen3, text='++Welcome To Employee Management System++', font=('samanata', 10)).pack()
    Label(screen3, text='',bg='#3333ff').pack()
    Button(screen3, text='Add Department', font='samanata', height=1, width=20, command=add_department).pack()
    Label(screen3, text='',bg='#3333ff').pack()
    Button(screen3, text='Add Employee', font='samanata', height=1, width=20, command=add_employee).pack()
    Label(screen3, text='',bg='#3333ff').pack()
    Button(screen3, text='View Employee', font='samanata', height=1, width=20, command=view).pack()
    Label(screen3, text='',bg='#3333ff').pack()
    Button(screen3, text='View Department', font='samanata', height=1, width=20, command=view_dep).pack()
    Label(screen3, text='',bg='#3333ff').pack()
    Label(screen3, text='',bg='#3333ff').pack()
    Label(screen3, text='',bg='#3333ff').pack()
    Button(screen3, text='Home', font=('samanata', 10), width=8, command=ex).pack(side='left', padx=10)
    Button(screen3, text='Exit', font=('samanata', 10), width=8, command=exit).pack(side='right', padx=10)
    screen3.mainloop()
def logg():
    user= usr.get()
    passw=pas.get()
    f= open('userinfo.txt','rb')
    m=pickle.load(f)
    user_list=[]
    pass_list=[]
    for i,j in m.items():
        user_list.append(i)
        pass_list.append(j)
    if user in user_list:
        if passw in pass_list:
            l2.configure(text='Successfully Logged In!',bg='white')
            screen2.destroy()
            user_dashboard()
        else:
            l2.configure(text='Invalid Password!',fg='red',bg='white')
    else:
         l2.configure(text='User Not Found!',fg='red',bg='white')
def bac():
    screen2.destroy()
    main_screen()
def login():
    screen.destroy()
    global screen2
    global usr
    global pas
    global l2
    screen2= Tk()
    screen2.geometry('440x580+0+0')
    screen2.configure(bg='#3333ff')
    usr = StringVar()
    pas= StringVar()
    Label(screen2, text='Softwarica',fg='#3333ff', font=(('samanata'), 20,'bold'), bg='white', height=2, width=420).pack()
    Label(screen2, text='', bg='#3333ff').pack()
    Label(screen2, text='', bg='#3333ff').pack()
    Label(screen2, text='++Please Login To Access Employee Management System++',font=(('samanata'),10)).pack()
    Label(screen2, text='', bg='#3333ff').pack()
    Label(screen2, text='', bg='#3333ff').pack()
    Label(screen2, text='Username*:',fg='white',bg='#3333ff', font=(('samanata'), 10)).pack()
    Entry(screen2,textvariable=usr).pack()
    Label(screen2, text='Password*:',fg='white',bg='#3333ff', font=(('samanata'), 10)).pack()
    Entry(screen2,textvariable=pas,show='*').pack()
    Label(screen2, text='', bg='#3333ff').pack()
    Button(screen2, text='Login', font=(('samanata'),10),width=8,command=logg).pack()
    Label(screen2,text="",bg='#3333ff').pack(pady=20)
    l2=Label(screen2,text='',bg='#3333ff')
    l2.pack()
    Label(screen2, text='', bg='#3333ff').pack()
    Label(screen2, text='', bg='#3333ff').pack()
    Label(screen2, text='', bg='#3333ff').pack()
    Label(screen2, text='', bg='#3333ff').pack()
    Button(screen2, text='Back', font=(('samanata'),10),width=8, command=bac).pack(side='left', padx=10, pady=2)
    Button(screen2, text='Back', font=(('samanata'), 10), width=8, command=screen2.destroy).pack(side='right', padx=10, pady=2)
    screen2.mainloop()
def submit():
    user=username.get()
    passw=password.get()
    cpassw=con_password.get()
    d1= {user:passw}
    file= open('userinfo.txt','rb+')
    d=pickle.load(file)
    file.close()
    if user=="":
        l1.configure(text='Invalid Username!',fg='red',bg='white')
    elif passw!=cpassw or passw=="" or cpassw=="":
        l1.configure(text='Invalid Password!',fg='red',bg='white')
    elif user in d:
        l1.configure(text='User Already Exists!',fg='red',bg='white')
    else:
        f= open('userinfo.txt','rb+')
        d.update(d1)
        f.seek(0)
        pickle.dump(d,f)
        f.close()
        l1.configure(text='Registered Please Log In!',fg='green',bg='white')
        ent1.delete(0,END)
        ent2.delete(0, END)
        ent3.delete(0, END)
def back():
    screen2.destroy()
    main_screen()
def register():
    screen.destroy()
    global screen2
    screen2= Tk()
    screen2.geometry('440x580+0+0')
    screen2.configure(bg='#3333ff')
    global ent1
    global ent2
    global ent3
    global first_name
    global last_name
    global username
    global password
    global con_password
    global l1
    username=StringVar()
    password=StringVar()
    con_password=StringVar()
    Label(screen2, text='Softwarica', fg='#3333ff', font=(('samanata'), 20, 'bold'), bg='white', height=2, width=420).pack()
    Label(screen2, text='', bg='#3333ff').pack()
    Label(screen2, text='', bg='#3333ff').pack()
    Label(screen2, text='', bg='#3333ff').pack()
    Label(screen2, text='++Verify your information to log in++', font=(('samanata', 12))).pack()
    Label(screen2, text='', bg='#3333ff').pack()
    Label(screen2, text='Username*:', font=(('samanata'), 10), bg='#3333ff', fg='white').pack()
    ent1=Entry(screen2, textvariable=username)
    ent1.pack()
    Label(screen2, text='Password*:', font=(('samanata'), 10), bg='#3333ff', fg='#ffffff').pack()
    ent2=Entry(screen2, textvariable=password, show='*')
    ent2.pack()
    Label(screen2, text='Confirm Password*:', font=(('samanata'), 10), bg='#3333ff', fg='white').pack()
    ent3=Entry(screen2, textvariable=con_password, show='*')
    ent3.pack()
    Label(screen2, text='', bg='#3333ff').pack()
    Button(screen2, text='Submit', font=(('samanata'), 10), command=submit).pack()
    Label(screen2, text='', bg='#3333ff').pack()
    l1 =Label(text='',bg='#3333ff')
    l1.pack()
    Label(screen2, text='', bg='#3333ff').pack()
    Label(screen2, text='', bg='#3333ff').pack()
    Label(screen2, text='', bg='#3333ff').pack()
    Button(screen2, text='Back', font=(('samanata'), 10), command=back, width=8).pack(side='left', padx=10, pady=10)
    Button(screen2, text='Cancel', font=(('samanata'), 10), width=8, command=screen2.destroy).pack(side='right', padx=10, pady=10)
    screen2.mainloop()
def main_screen():
    global screen
    screen=Tk()
    screen.geometry('440x580+0+0')
    screen.configure(bg='#3333ff')
    Label(screen, text='Softwarica', font=(('samanata'), 20,'bold'),fg='#3333ff', bg='white', height=2, width=420).pack()
    Label(screen, text="",bg='#3333ff').pack()
    Label(screen, text="",bg='#3333ff').pack()
    Label(screen, text="",bg='#3333ff').pack()
    Label(screen, text="",bg='#3333ff').pack()
    Label(screen, text="",bg='#3333ff').pack()
    Label(screen, text="",bg='#3333ff').pack()
    Button(screen, text='Login', font=(('samanata')),bg='white', height=1, width=20, command=login).pack()
    Label(screen, text="",bg='#3333ff').pack()
    Button(screen,text='Register', font=(('samanata')),bg='white',height=1,width=20,command=register).pack()
    Label(screen, text="",bg='#3333ff').pack()
    Label(screen, text="",bg='#3333ff').pack()
    Label(screen, text="",bg='#3333ff').pack()
    Label(screen, text="",bg='#3333ff').pack()
    Label(screen, text="",bg='#3333ff').pack()
    Label(screen, text="",bg='#3333ff').pack()
    Label(screen, text="",bg='#3333ff').pack()
    Button(screen, text='Exit', font=(('samanata'),10),width=8,bg='white',fg='black', command=screen.destroy).pack(padx=10, pady=10)
    screen.mainloop()
create()
main_screen()