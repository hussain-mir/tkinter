from tkinter import *
root=Tk()

root.title('Hussain')
root.geometry('400x500+400+120')
root.resizable(False, False)
root.config(bg='#262626')

# label
labl_title=Label(root, text='its hussain',font=('times new roman','16','bold'), fg='red', bg='white',pady=5,bd=5,relief=GROOVE).place(x=0,y=0, height=60,relwidth=1)



# ---------------------BuTTON
# hand1
# hand2
def show():
    # print(entry1.get())
    # labe2_result.config(text=entry1.get())
    labe2_result.config(text=var_1.get())
btn=Button(root,text='SHOW', font=('times new roman',15,'bold'), fg='black', bg='red',bd=5,relief=GROOVE, activebackground='black', activeforeground='red', cursor='hand1',command=show)
btn.place(x=300,y=120, width=100, height=40)



# entry
var_1=StringVar()

entry1=Entry(root, font=('times new roman',15,'bold'), fg='black', textvariable=var_1, bg='lightyellow',bd=7,relief=GROOVE)
entry1.place(x=0,y=70, relwidth=1)


# result
labe2_result=Label(root,font=('times new roman','20','bold'), fg='red', bg='#262626',pady=10)
labe2_result.place(x=0,y=160, height=70,relwidth=1)


root.mainloop()