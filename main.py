
from tkinter import *

import random

import pandas

BACKGROUND_COLOR = "#B1DDC6"
try:
   new_panda=pandas.read_csv("data/stores.csv")

except FileNotFoundError:
 origional=pandas.read_csv("data/french_words.csv")
 to_learn=origional.to_dict(orient="record")
 print(to_learn)


else:
 to_learn=new_panda.to_dict(orient="record")


current_card={}

def something():
    global current_card,call
    window.after_cancel(call)
    current_card=random.choice(to_learn)
    flashcard.itemconfig(random1,text="french")
    flashcard.itemconfig(random2,text=current_card["French"])
    call=window.after(3000,something2)


def something2():
   flashcard.itemconfig(random1,text="English")
   flashcard.itemconfig(random2,text=current_card["English"])
   flashcard.itemconfig(back_images,image=flashfile1)

def to_known():
   to_learn.remove(current_card)
   print(len(to_learn))
   data=pandas.DataFrame(to_learn)
   data.to_csv("data/stores.csv",index=False)
   

window=Tk()
window.title("flash card")
window.config(padx=100,pady=100,background="#B1DDC6")
call=window.after(3000,something2)

# def something():

#  with open ("data/french_words.csv","r") as file:
#     allText = file.read()
#     words = list(map(str, allText.split()))
#     now=random.choice(words)
#     flashcard.itemconfig(random1, text = now)

# 
flashcard=Canvas(width=800,height=526)
flashfile=PhotoImage(file="images/card_back.png")
flashfile1=PhotoImage(file="images/card_front.png")
back_images=flashcard.create_image(400,263, image=flashfile)
# front_images=flashcard.create_image(400,263, image=flashfile1)
flashcard.config(background="#B1DDC6",highlightthickness=0)
random1=flashcard.create_text(400,158,text="",font=("ariel",40,"italic"))
random2=flashcard.create_text(400,256,text="",font=("ariel",40,"bold"))
flashcard.grid(column=0,row=0,columnspan=2)

buttonimg=PhotoImage(file="images/right.png")
flashbutton=Button(image=buttonimg,command=something)
flashbutton.grid(column=0,row=1)


buttonimg1=PhotoImage(file="images/wrong.png")
flashbutton=Button(image=buttonimg1,command=to_known)
flashbutton.grid(column=1,row=1)

something()

window.mainloop()

