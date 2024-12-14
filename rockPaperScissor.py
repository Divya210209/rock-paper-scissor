from tkinter import *
from random import randint

from PIL import Image,Image,ImageTk
root=Tk()
root.title("ROCK PAPER SCISSOR")
root.configure(background="#9b59b6")

rock_user_img=ImageTk.PhotoImage(Image.open("rock-comp.jpeg"))
paper_user_img=ImageTk.PhotoImage(Image.open("paper-comp.jpeg"))
scissor_user_img=ImageTk.PhotoImage(Image.open("scissor-comp.jpeg"))
rock_comp_img=ImageTk.PhotoImage(Image.open("rock-comp.jpeg"))
paper_comp_img=ImageTk.PhotoImage(Image.open("paper-comp.jpeg"))
scissor_comp_img=ImageTk.PhotoImage(Image.open("scissor-comp.jpeg"))

user_label=Label(root,image=scissor_user_img,bg="#9b59b6")
comp_label=Label(root,image=scissor_comp_img,bg="#9b59b6")
comp_label.grid(row=1,column=0)
user_label.grid(row=1,column=4)

playerScore = Label(root,text=0,font=100,bg="#9b59b6",fg="white")
computerScore = Label(root,text=0,font=100,bg="#9b59b6",fg="white")
computerScore.grid(row=1,column=1)
playerScore.grid(row=1,column=3)

user_indicator=Label(root,font=50,text="USER",bg="#9b59b6",fg="white")
comp_indicator=Label(root,font=50,text="COMPUTER",bg="#9b59b6",fg="white")
user_indicator.grid(row=0,column=4)
comp_indicator.grid(row=0,column=0)

msg=Label(root,font=50,bg="#9b59b6",fg="white")
msg.grid(row=3,column=2)

def updateMessage(x):
    msg['text']=x

def updateUserScore():
    score=int(playerScore["text"])
    score += 1
    playerScore["text"] = str(score)

def updateCompScore():
    score=int(computerScore["text"])
    score += 1
    computerScore["text"] = str(score)

def checkWinn(player,computer):
    if player == computer:
        updateMessage("Its a Tie!!")
    elif player == "rock":
        if computer == "paper":
            updateMessage("You loose")
            updateCompScore()
        else:
            updateMessage("You Win")
            updateUserScore()
    elif player == "paper":
        if computer=="scissor":
            updateMessage("You loose")
            updateCompScore()
        else:
            updateMessage("You Win")
            updateUserScore()
    elif player == "scissor":
        if computer=="rock":
            updateMessage("You loose")
            updateCompScore()
        else:
            updateMessage("You Win")
            updateUserScore()
    else:
        pass

choices=["rock","paper","scissor"]
def updateChoice(x):

    compChoice = choices[randint(0,2)]
    if compChoice == "rock":
        comp_label.configure(image=rock_comp_img)
    elif compChoice=="paper":
        comp_label.configure(image=paper_comp_img)
    else:
        comp_label.configure(image=scissor_comp_img)


    if x=="rock":
        user_label.configure(image=rock_user_img)
    elif x=="paper":
        user_label.configure(image=paper_user_img)
    else:
        user_label.configure(image=scissor_user_img)
    checkWinn(x,compChoice)
    
rock=Button(root,width=20,height=2,text="ROCK",bg="#FF3E4D",fg="White",command=lambda:updateChoice("rock")).grid(row=2,column=1)
paper=Button(root,width=20,height=2,text="PAPER",bg="#FAD02E",fg="White",command=lambda:updateChoice("paper")).grid(row=2,column=2)
scissor=Button(root,width=20,height=2,text="SCISSOR",bg="#0ABDE3",fg="White",command=lambda:updateChoice("scissor")).grid(row=2,column=3)

root.mainloop()











































