from tkinter import *
import random
import pandas as pd
card_num = 0
BACKGROUND_COLOR = "#B1DDC6"


def reveal_meaning():
    global card_num

    next_button.grid_forget()
    right_button.grid(row=1, column=1)
    wrong_button.grid(row=1, column=0)
    del_button.grid(row=1, column=0, columnspan=2)
    card.itemconfig(card_img, image=card_back_img)
    card.itemconfig(language, text="English")
    card.itemconfig(word, text=words_dict[card_num % len(words_dict)]['English'])

    card_num += 1


def next_card():
    card.itemconfig(card_img, image=card_front_img)
    card.itemconfig(word, text=words_dict[card_num % len(words_dict)]['French'])
    card.itemconfig(language, text="French")
    next_button.grid(row=1, column=0, columnspan=2)
    right_button.grid_forget()
    wrong_button.grid_forget()
    del_button.grid_forget()


def delete_card():
    global card_num

    words_dict.remove(words_dict[card_num - 1])
    print(words_dict)
    pd.DataFrame(words_dict).to_csv("./data/unlearned_words.csv", index=False)
    card_num -= 1
    next_card()


window = Tk()

window.title("Language Flash Cards")
window.config(padx=50, pady=50)

words = pd.read_csv("./data/unlearned_words.csv")
words_dict = words.to_dict(orient="records")

random.shuffle(words_dict)

print(words_dict)

card = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
card_img = card.create_image(415,250, image=card_front_img)
language = card.create_text(400, 150, text="French", font=("Arial", 40, "italic"))
word = card.create_text(400, 283, text=words_dict[0]['French'], font=("Arial", 60, "bold"))
card.grid(row=0, column=0, columnspan=2)

correct_img = PhotoImage(file="./images/right.png")
right_button = Button(image=correct_img, command=next_card)

wrong_img = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_img, command=next_card)

next_img = PhotoImage(file="./images/next.png")
next_button = Button(image=next_img, command=reveal_meaning)

del_img = PhotoImage(file="./images/delete.png")
del_button = Button(image=del_img, command=delete_card)

next_card()

window.mainloop()
