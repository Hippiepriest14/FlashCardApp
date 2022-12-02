from tkinter import *
import pandas
import random
data = pandas.read_csv("data/english_words.csv")
data = data.to_dict(orient="records")
current_word = {}


def next_card():
    global current_word,flip_timer
    window.after_cancel(flip_timer)
    current_word = random.choice(data)
    canvas.itemconfig(card_title,text="English",fill="black")
    canvas.itemconfig(card_word,text=current_word["English"],fill="black")
    canvas.itemconfig(card_back,image=image)
    flip_timer = window.after(5000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="Russian",fill="white")
    canvas.itemconfig(card_word, text=current_word["Russian"],fill="white")
    canvas.itemconfig(card_back,image=image_back)

def wrong_answer():
    data.remove(current_word)
    next_card()

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("FlashCard")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

flip_timer = window.after(5000,func=flip_card)

canvas = Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
image = PhotoImage(file="images/card_front.png")
image_back = PhotoImage(file="images/card_back.png")
card_back = canvas.create_image(400,263,image=image)
card_title = canvas.create_text(400,100,text="Title",font=("courier", 40, "italic"))
card_word = canvas.create_text(400,250,text="Word",font=("Ariel", 30,"bold"))
canvas.grid(column=0,row=0,columnspan=2)

accept_image = PhotoImage(file="images/right.png")
accept = Button(image=accept_image,bg=BACKGROUND_COLOR,width=70,height=70,command=wrong_answer)
accept.grid(column=0,row=1)

wrong_image = PhotoImage(file="images/wrong.png")
wrong = Button(image=wrong_image,bg=BACKGROUND_COLOR,width=70,height=70,command=next_card)
wrong.grid(column=1,row=1)


next_card()






window.mainloop()