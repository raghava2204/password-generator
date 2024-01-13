import tkinter
from tkinter import messagebox
import random
import string

#frame
root=tkinter.Tk()
root.title("Password Generator")
root.configure(background="white")
def password():
    enter=en_try.get()
    try:
        len=int(enter)
    except ValueError:
        messagebox.showwarning(title="Warning!",message="you must enter length")

    num_ericals=state_1.get()
    special_char=state_2.get()

    num=string.digits
    spec=string.punctuation

    char=string.ascii_letters
    if num_ericals:
        char+=num
    if special_char:
        char+=spec
    generate_password=''
    for i in range(len):
        generate_password+=random.choice(char)
    op_box.insert(0,generate_password)
    en_try.delete(0,tkinter.END)
    

    
   
#output box
op_box=tkinter.Listbox(root,height=10,width=40,font=("Times New Roman",20),background="black",foreground="white")
op_box.grid(row=0,column=0,rowspan=2,columnspan=5)

len_label=tkinter.Label(root,text="Enter the Length of password ",font=("Comic Sans MS",12,"roman"),background="white",foreground="black")
len_label.grid(row=2,column=0,sticky=tkinter.NSEW)
root.grid_rowconfigure(0,weight=1)
root.grid_columnconfigure(0,weight=1)


#input
en_try=tkinter.Entry(root,background="white")
en_try.grid(row=2,column=1)
label0=tkinter.Label(root,text="                               ",background="white")
label0.grid(row=3,column=0)

#checkbox
state_1=tkinter.BooleanVar()
state_2=tkinter.BooleanVar()
num_box=tkinter.Checkbutton(root,text="Numericals",background="snow3",fg="black",variable=state_1)
num_box.grid(row=4,column=1)
label1=tkinter.Label(root,text="                               ",background="white")
label1.grid(row=5,column=0)
special_box=tkinter.Checkbutton(root,text="Special Characters",bg="snow3",fg="black",variable=state_2)
special_box.grid(row=6,column=1)
label2=tkinter.Label(root,text="                               ",background="white")
label2.grid(row=7,column=0)
gen_button=tkinter.Button(root,text="Generate",height=2,width=10,background="black",fg="red",font=("Courier New",10,"bold"),command=password)
gen_button.grid(row=8,column=1,padx=50)
root.mainloop()