import turtle
from tkinter import *
from tkinter.filedialog import *
import fileinput
from tkinter.messagebox import *
from tkinter import messagebox
import time
from  turtle import *

window = Tk()
bg=PhotoImage(file='img_1.png')
a=Label(window,image=bg)
a.pack()
window.title('library')
window.geometry('500x400')
idpp='1234567'

storedPassword=''
username=''

def name():
    if txt.get() == username:
        password1()
    else:
        lbl4 = Label(window, text='Wrong UserName', fg='red', bg='gray77')
        lbl4.place(x=237, y=197)


def password1():
    if txt1.get() == storedPassword:
        window.withdraw()
        b = 0
        color('white')
        turtle.title('Verification Accaunt')
        bgcolor('black')
        speed(11)
        hideturtle()
        while b < 70:
            left(b+1)
            forward(b*2)
            b = b + 1
        time.sleep(1)
        libr()
    else:
        lbl3 = Label(window, text='Wrong Password', bg='gray77', fg='red')
        lbl3.place(x=237, y=270)


def pswshw():
    if txt1.cget('show') == '':
        txt1.config(show='*')
        rbt.config(text='Show Password')
    else:
        txt1.config(show='')
        rbt.config(text='Hide Psasword')


def libr():
    lib = Toplevel()
    lib.geometry('1200x700')
    lib.title('Library')
    bg=PhotoImage(file='img_3.png')
    a=Label(lib,image=bg)
    a.pack()
    books = [
        {
            'id': 1234,
            'title': 'Sharp Objects',
            'photo': PhotoImage(file='img.png'),
            'texr':('sharp11.txt'),
            'author':'Gillian Flynn',
            'Published':': 2007',
            'janre':'Crime',
            'number of books':20
        },
        {
            'id': 1687,
            'title': 'he Lightning Thief',
            'photo': PhotoImage(file='img_4.png'),
            'texr':('The light.txt'),
            'author': 'Rick Riordan',
            'Published': ':  2005',
            'janre': 'Fantasy',
            'number of books': 30
        },
        {
            'id': 1987,
            'title': 'Peter Pen',
            'photo': PhotoImage(file='img_2.png',),
            'texr':('peterpan.txt'),
            'author': 'J. M. Barrie ',
            'Published': ': 1981',
            'janre': 'Fantasy',
            'number of books': 10
        }
    ]

    lbl3 = Label(lib, text='Home Page', font='bold')
    lbl3.place(x=400,y=10,relwidth=0.2, relheigh=0.07)

    lbl4=Label(lib,text='Author:',font='bold',bg='#BABFBF')
    lbl4.place(x=600,y=200,relwidth=0.07, relheigh=0.03)
    lbl5=Label(lib,text='No Information',font='bold',bg='#BABFBF')
    lbl5.place(x=690,y=200,relwidth=0.09, relheigh=0.03)
    lbl6=Label(lib,text='Published',font='bold',bg='#BABFBF')
    lbl6.place(x=600,y=250,relwidth=0.07, relheigh=0.03)
    lbl7=Label(lib,text='No Information',font='bold',bg='#BABFBF')
    lbl7.place(x=690, y=250, relwidth=0.09, relheigh=0.03)
    lbl8=Label(lib,text='Janre',font='bold',bg='#BABFBF')
    lbl8.place(x=600,y=300,relwidth=0.07, relheigh=0.03)
    lbl9=Label(lib,text='No Information',font='bold',bg='#BABFBF')
    lbl9.place(x=690, y=300, relwidth=0.09, relheigh=0.03)
    lbl10=Label(lib,text='Number of books',font='bold',bg='#BABFBF')
    lbl10.place(x=610,y=350,relwidth=0.1, relheigh=0.03)
    lbl11=Label(lib,text='No Info',font='bold',bg='#BABFBF')
    lbl11.place(x=725,y=350,relwidth=0.06, relheigh=0.03)




    elements = []
    for i in books:
        elements.append(i['title'])
    elements_list = Listbox(lib, bg='gray75',height=22, width=35)
    scroll = Scrollbar(lib)
    scroll.config(command=elements_list.yview)
    elements_list.config(yscrollcommand=scroll.set)
    scroll.place(x=280, y=200)
    elements_list.place(x=50, y=200)
    for i in elements:
        elements_list.insert(END, i)


    def inf():
        sel = elements_list.get('active')
        for i in books:
            if i['title'] == sel:
                imgPath = i['photo']
                photoLabel.config(image=imgPath)
                txtPath=i['texr']
                autPath=i['author']
                lbl5.config(text=autPath)
                pubPath=i['Published']
                lbl7.config(text=pubPath)
                janPath=i['janre']
                lbl9.config(text=janPath)
                numPath=i['number of books']
                lbl11.config(text=numPath)
                with open(txtPath,'r') as fl:
                    text=fl.read()
                    tex1.delete(1.0,END)
                    tex1.insert(1.0,text)
                break

    def pasred():
        for i in books:
            sel = elements_list.get('active')
            if i['title'] == sel:
                numPath = i['number of books'] - 1
                lbl11.config(text=numPath)

    def addPhoto():
        global img
        from tkinter import filedialog
        fileName = filedialog.askopenfilename(initialdir='/',
                                              title='Open',
                                              filetypes=(('Photo', '*.png'),
                                                         ('All files', '.')))
        img = PhotoImage(file=fileName)
        photoLabel.config(image=img)
        book = {}
        book['photo'] = img
        books.append(book)


    def ad():
        tex2=Entry(lib,bg='gray75')
        tex2.place(x=50,y=150)
        # btn12=Button(lib,text='adini elave et',command=lambda :done())
        # btn12.place(x=200,y=150)
        btn13=Button(lib,text='sekili elave et', command=addPhoto)
        btn13.place(x=290,y=150)
        btn14=Button(lib,text='yadda saxla',command=lambda :add())
        btn14.place(x=380,y=150)

        tex4 = Entry(lib, bg='gray75')
        tex4.place(x=480, y=200)

        tex5 = Entry(lib, bg='gray75')
        tex5.place(x=480, y=250)

        tex6 = Entry(lib, bg='gray75')
        tex6.place(x=480, y=300)

        tex7 = Entry(lib, bg='gray75')
        tex7.place(x=480, y=350)

        def add():
            if len(tex2.get())>0:
                if len(tex4.get())>0:
                    if len(tex5.get())>0:
                        if len(tex6.get())>0:
                            if len(tex7.get()) > 0:
                                books[0][len(books[0])+1]={'title':tex2.get(),
                                                           'author':tex4.get(),
                                                           'Published':tex5.get(),
                                                           'janre':tex6.get(),
                                                           'number of book':tex7.get()}
                                elements_list.insert(END,tex2.get())
                            else:
                                messagebox.showinfo("Error",'Not Name')
                        else:
                            messagebox.showinfo("Error", 'Not Name')
                    else:
                        messagebox.showinfo("Error", 'Not Name')
                else:
                    messagebox.showinfo("Error", 'Not Name')
            else:
                messagebox.showinfo("Error", 'Not Name')

            tex2.destroy()
            tex4.destroy()
            tex5.destroy()
            tex6.destroy()
            tex7.destroy()
            btn13.destroy()
            btn14.destroy()

    def delet_el():
        sel = elements_list.curselection()
        for i in reversed(sel):
            elements_list.delete(i)

    def sortaz():
        newl = sorted(elements)
        elements_list.delete(0, END)
        for i in newl:
            elements_list.insert(END, i)

    def shortza():
        newl = sorted(elements)
        elements_list.delete(0, END)
        newl.reverse()
        for i in newl:
            elements_list.insert(END, i)

    def pp():
        lib.withdraw()
        profwind=Toplevel()
        profwind.geometry('980x756')
        bg=PhotoImage(file='img_5.png')
        lbl55=Label(profwind,image=bg)
        lbl55.pack()

        lbl56 = Label(profwind, text=username,bg='#000000',fg='white')
        lbl56.place(x=720,y=220,relwidth=0.1, relheigh=0.03)
        btn33=Button(profwind,text='go back',bg='grey17',fg='white',command=lambda:bck())
        btn33.place(x=845,y=65,relwidth=0.09, relheigh=0.06)
        lbl57 = Label(profwind, text='Username:', bg='#000000', fg='white')
        lbl57.place(x=620, y=220,relwidth=0.1, relheigh=0.03)

        lbl56 = Label(profwind, text=storedPassword, bg='#000000', fg='white')
        lbl56.place(x=720, y=370, relwidth=0.1, relheigh=0.03)
        lbl57 = Label(profwind, text='Password:', bg='#000000', fg='white')
        lbl57.place(x=620, y=370, relwidth=0.1, relheigh=0.03)

        tex111 = Label(profwind,text=idpp, bg='black',fg='white')
        tex111.place(x=690, y=510)
        lbl58 = Label(profwind, text='Personal Id:', fg='black')
        lbl58.place(x=670, y=470)





        def bck():
            profwind.withdraw()
            lib.deiconify()


        profwind.mainloop()
    def lgot():
        lib.destroy()
        window.deiconify()
    def ntf():
        messagebox.showinfo("Notification",'Sizin bildirisiniz yoxdur!')


    Button(lib, text='add',command=ad).place(x=300, y=200, relwidth=0.09, relheigh=0.02)
    Button(lib, text='Delete', command=delet_el).place(x=300, y=250, relwidth=0.09, relheigh=0.02)
    Button(lib, text='edit').place(x=300, y=300, relwidth=0.09, relheigh=0.02)
    Button(lib, text='Sort Z-A',command=shortza).place(x=300, y=500, relwidth=0.09, relheigh=0.02)
    Button(lib, text='pass to reader',command=pasred).place(x=300, y=350, relwidth=0.09, relheigh=0.02)
    Button(lib, text='return').place(x=300, y=400, relwidth=0.09, relheigh=0.02)
    Button(lib, text='Sort A-Z', command=sortaz).place(x=300, y=450, relwidth=0.09, relheigh=0.02)
    Button(lib, text='get info',command=inf).place(x=300, y=550, relwidth=0.09, relheigh=0.02)
    Button(lib, text='Notification',bg='grey17',fg='white',command=ntf).place(x=1100, y=50, relwidth=0.09, relheigh=0.08)
    Button(lib, text='Profile',bg='grey17',fg='white',command=pp).place(x=1100, y=100, relwidth=0.09, relheigh=0.08)
    Button(lib, text='Log out',bg='grey17',fg='white',command=lgot).place(x=1100, y=150, relwidth=0.09, relheigh=0.08)




    tex1 = Text(lib,bg='gray75')
    tex1.place(x=650, y=400,relwidth=0.4, relheigh=0.4)

    frame1 = Frame(lib, highlightbackground='black', highlightthicknes=3)
    frame1.place(x=800, y=40, relwidth=0.2, relheigh=0.5)
    photoLabel = Label(frame1,text='No Photo',font='bold')
    photoLabel.pack(fill=BOTH)


    scroll = Scrollbar(lib)
    scroll.config(command=tex1.yview)
    tex1.config(yscrollcommand=scroll.set)
    scroll.place(x=1150, y=400)

    lib.mainloop()


frame = Frame(window, width=300, highlightbackground='black', highlightthicknes=3)
frame.place(x=180, y=30, relwidth=0.3, relheigh=0.1)
lbl = Label(frame, text='Welcome', font='SemiBold')
lbl.pack()

frame1 = Frame(window, width=300, highlightbackground='black', highlightthicknes=3)
frame1.place(x=180, y=100, relwidth=0.3, relheigh=0.09)
lbl1 = Label(frame1, text='Login', font='SemiBold')
lbl1.pack()

txt = Entry(bg='gray85')
txt.place(x=110, y=200)
lbl2 = Label(window, text='UserName:', bg='gray77', fg='black')
lbl2.place(x=110, y=180)

txt1 = Entry(window, show='*',bg='gray85')
txt1.place(x=110, y=270)
lbl2 = Label(window, text='Password:', bg='gray77', fg='black')
lbl2.place(x=110, y=250)

btn = Button(window, text='Log In', bg='gray77',fg='black', command=name)
btn.place(x=320, y=340, relwidth=0.3, relheigh=0.1)
rbt = Radiobutton(window, text='Show password', bg='gray77',fg='black', command=pswshw)
rbt.place(x=80, y=290)

window.mainloop()