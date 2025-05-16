import random
import tkinter as tk
import time
from difflib import SequenceMatcher

TEXTS = ["Hace calor y el cielo está despejado. Los pájaros cantan en los árboles. Es un buen día para salir a caminar.\n"
         " Recuerda llevar agua y protector solar. Disfruta del aire libre y la naturaleza.",
         "Huele delicioso y sabe aún mejor. La mantequilla se derrite al contacto. Es perfecto para el desayuno.\n"
         " Un café caliente lo acompaña bien. Simple, pero muy satisfactorio.",
         "Corre tras una pelota roja. Salta y ladra de felicidad. Después se acuesta a descansar bajo un árbol.\n "
         "Los animales dan mucha alegría a la vida.",
         "Las gotas golpean el techo. El olor a tierra mojada es agradable. Es un buen momento para leer o dormir.\n "
         "El clima tranquilo relaja la mente.",
         "El cielo oscuro las hace destacar. A veces se ven constelaciones. Es bonito mirarlas en silencio.\n "
         "La naturaleza siempre sorprende.",]


window= tk.Tk()
window.title("TypeSpeed Test")
window.geometry('600x400')
window.config(padx=100,pady=100)

photos = []
image_label = tk.Label(text="Let´s Test your Typing Speed!", font=("Arial", 20), pady=15)
image_label.grid(row= 0, column = 0, columnspan=2)


def game_start():
    global start_time, sample_text_widget, user_txt_widget, finish_button

    start_time = time.time()
    random_text = random.choice(TEXTS)

    # hide Start button when the game starts
    start_button.grid_remove()

    # create and show user the selected text
    sample_text_widget = tk.Label(text=random_text, font=("Arial", 10), pady=15)
    sample_text_widget.grid(row=1, column=0, columnspan=2)

    # create user text box
    user_txt_widget = tk.Text(window, height=4, width=50)
    user_txt_widget.grid(row=2, column=0, columnspan=2)

    finish_button = tk.Button(
        text="Finish Game",
        padx=10,
        pady=5,
        command=lambda: finish_game(user_txt_widget, random_text, sample_text_widget, finish_button)
    )
    finish_button.grid(row=3, column=0, columnspan=2)


def finish_game(txt, rnd_txt, sample_widget, finish_btn):
    # calculate WPM
    elapsed_time = time.time() - start_time

    text_content = txt.get("1.0", "end-1c")
    words_user = text_content.split()
    words_txt = rnd_txt.split()

    total_words = len(words_user)
    wpm = round((total_words / elapsed_time) * 60, 2)

    # destroy stored widgets
    txt.destroy()
    sample_widget.destroy()
    finish_btn.destroy()

    # calculate Accuracy
    user_accuracy = round((SequenceMatcher(None, words_user, words_txt).ratio()) * 100,2)

    lbl.config(text=f"Text saved! Your WPM is: {wpm}\n with {user_accuracy}% accuracy")

    # show Start button again
    start_button.grid()


start_button = tk.Button(text="Start Game",padx=10, pady=5,command=game_start)
start_button.grid(row= 3, column = 0, columnspan=2)

lbl = tk.Label(window, text="")
lbl.grid(row= 4, column = 0, columnspan=2)

window.mainloop()