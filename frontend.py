from tkinter import *
import backend

def get_selected_row(event):
    try:
        global selected_tuple
        index=list1.curselection()[0]
        selected_tuple=list1.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])
    except IndexError:
        pass

def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in backend.search(Username_text.get(),TSS_text.get(),Date_text.get(),Received_text.get()):
        list1.insert(END,row)

def add_command():
    backend.insert(Username_text.get(),TSS_text.get(),Date_text.get(),Received_text.get())
    list1.delete(0,END)
    list1.insert(END,(Username_text.get(),TSS_text.get(),Date_text.get(),Received_text.get()))

def delete_command():
    backend.delete(selected_tuple[0])

def update_command():
    backend.update(selected_tuple[0],Username_text.get(),TSS_text.get(),Date_text.get(),Received_text.get())

def ResetButton():
    e1.delete('0',END)
    e2.delete('0',END)
    e3.delete('0',END)
    e4.delete('0',END)
    


window=Tk()

var = StringVar()
label = Message( window, textvariable=var, relief=RAISED )

var.set("PLEASE SCAN YOUR CARD AND LAPTOP ASSETNUMBER !!!")
label.grid(row=0,column=0, )

window.wm_title("LOANLAPTOPS")



l1=Label(window,text="Username")
l1.grid(row=0,column=1)

l2=Label(window,text="TSS")
l2.grid(row=0,column=3)

l3=Label(window,text="Date")
l3.grid(row=0,column=5)

l4=Label(window,text="Received")
l4.grid(row=0,column=7)

Username_text=StringVar()
e1=Entry(window,textvariable=Username_text)
e1.grid(row=0,column=2)

TSS_text=StringVar()
e2=Entry(window,textvariable=TSS_text)
e2.grid(row=0,column=4)

Date_text=StringVar()
e3=Entry(window,textvariable=Date_text)
e3.grid(row=0,column=6)

Received_text=StringVar()
e4=Entry(window,textvariable=Received_text)
e4.grid(row=0,column=8)

list1=Listbox(window, height=10,width=100)
list1.grid(row=4,column=1,rowspan=4,columnspan=7)

sb1=Scrollbar(window)
sb1.grid(row=4,column=6,rowspan=6,columnspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)

b1=Button(window,text="View all", width=12,fg = 'red' ,command=view_command)
b1.grid(row=4,column=10)

b2=Button(window,text="Search entry", width=12,command=search_command)
b2.grid(row=5,column=10)

b3=Button(window,text="Add entry", width=12,command=add_command)
b3.grid(row=6,column=10)

b4=Button(window,text="Update selected", width=12,command=update_command)
b4.grid(row=7,column=10, sticky=W, pady=4 )

b5=Button(window,text="Delete selected", width=12,command=delete_command)
b5.grid(row=8,column=10)

b6=Button(window,text="Close", width=12,command=window.destroy)
b6.grid(row=9,column=10)

b7=Button(window,text="CLEAR/RESET",fg = 'blue',bg = 'white', width=14,command=ResetButton)
b7.grid(row=1,column=1 ,sticky=W, pady=4)

window.mainloop()
