#Chirag Narula
from tkinter import *
from tkinter import messagebox

master = Tk()

master.geometry("400x275")

master.title("Chirag's Quiz")

master["bg"]="#45b8ac"

QueList=["Who developed C?","Who developed Python?","When Python is released?",
"Which of the following is not a keyword?","What is the answer to this expression, 22 % 3 is?"]

OptList=[["Denish Ritchie" ,"Bjarne Stroustrup" ,"James Gosling" ,"Tim Berners Lee"],
["Denish Ritchie" ,"Bjarne Stroustrup" ,"James Gosling" ,"Guido van Rossum"],["1992","1991","1990","1994"],["assert","nonlocal","pass","eval"],["5","7","1","0"]]

OutList=["1","4","2","4","3"]

i=result=0

v = StringVar(master, "1")
que=StringVar()
op1=StringVar()
op2=StringVar()
op3=StringVar()
op4=StringVar()

Label(master, width="300", text="Python Quiz Application", bg="orange", fg="#000000",font='Helvetica 12 bold').pack()

Label(master,text='',textvariable=que,bg="#45b8ac",fg="#ffffff",font='Helvetica 13 bold').place(x=90,y=35)

Radiobutton(master,text='',variable=v,value="1",bg="#45b8ac").place(x=140,y=60)

Label(master,text="",textvariable=op1,bg="#45b8ac",fg="#ffffff",font='Helvetica 12').place(x=160,y=60)

Radiobutton(master,text='',variable=v,value="2",bg="#45b8ac").place(x=140,y=80)

Label(master,text="",textvariable=op2,bg="#45b8ac",fg="#ffffff",font='Helvetica 12').place(x=160,y=80)

Radiobutton(master,text='',variable=v,value="3",bg="#45b8ac").place(x=140,y=100)

Label(master,text="",textvariable=op3,bg="#45b8ac",fg="#ffffff",font='Helvetica 12').place(x=160,y=100)

Radiobutton(master,text='',variable=v,value="4",bg="#45b8ac").place(x=140,y=120)

Label(master,text="",textvariable=op4,bg="#45b8ac",fg="#ffffff",font='Helvetica 12').place(x=160,y=120)

que.set("Q.1 "+QueList[0])

option=OptList[0]

op1.set(option[0])
op2.set(option[1])
op3.set(option[2])
op4.set(option[3])

i+=1

def myFun():
    
    global i
    global result
    
    if i<=len(QueList):
    
     if v.get() == OutList[i-1]:
        
         result += 1
     
     if(i!=len(QueList)):
      
      que.set("Q."+str(i+1)+" "+(QueList[i]))
      option=OptList[i]
    
      op1.set(option[0])
      op2.set(option[1])
      op3.set(option[2])
      op4.set(option[3])
     else:
        
      messagebox.showinfo("Result","Total Question:"+str(len(QueList))+"\nCorrect:"+str(result)+"\nIncorrect:"
      +str(len(QueList)-result)+"\nResult:"+str((result/(len(QueList))*100))+"%")
    
    i += 1

Label(master,text="Click here for next question",font='Helvetica 11',bg="#45b8ac",fg="yellow").place(x=120,y=180)

Button(master,text="Next",command=myFun,bg="green",fg="white",width="10",font='Helvetica 12').place(x=160,y=200)

mainloop()
