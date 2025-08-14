from tkinter import* 
from tkinter import messagebox
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"
try:
    data=pd.read_csv("data/words_to_learn.csv")
except:
    original_data=pd.read_csv("data/french_words.csv")
    to_learn=original_data.to_dict(orient="records")
else:
    to_learn=data.to_dict(orient="records")
current_card = {}

def next_card():
    global current_card,flip_timer
    tk.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canva.itemconfig(card_title,text="French",fill="black")
    canva.itemconfig(card_word,text=current_card["French"],fill="black")
    canva.itemconfig(card_face,image=card_frontimg)
    flip_timer=tk.after(3000,func=flip_card)

def flip_card():
    global current_card
    canva.itemconfig(card_title,text="English",fill="white")
    canva.itemconfig(card_word,text=current_card["English"],fill="white")
    canva.itemconfig(card_face,image=card_back)

def is_known():
    to_learn.remove(current_card)
    next_card()
    data=pd.DataFrame(to_learn)
    data.to_csv("data/Words_to_learn.csv",index=False)






tk=Tk()
tk.title("Flash Card")
tk.config(padx=50,pady=50,bg=BACKGROUND_COLOR)


flip_timer=tk.after(3000,func=flip_card)


card_frontimg = PhotoImage(file="images/card_front.png")
card_back=PhotoImage(file="images/card_back.png")

canva = Canvas(width=800, height=526,)
card_face=canva.create_image(400, 263, image=card_frontimg)


card_title=canva.create_text(400, 150, text="", font=("ariel", 40, "italic"))
card_word = canva.create_text(400, 263, text="", font=("ariel", 60, "bold"))
canva.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canva.grid(row=0,column=0,columnspan=2,)





wrong_img = PhotoImage(file="images/wrong.png")
right_img = PhotoImage(file="images/right.png")

button1 = Button(image=wrong_img, borderwidth=0, highlightthickness=0,command=next_card)
button1.grid(row=1, column=0)

button2 = Button(image=right_img, borderwidth=0, highlightthickness=0,command=is_known)
button2.grid(row=1, column=1)


next_card()



tk.mainloop()

