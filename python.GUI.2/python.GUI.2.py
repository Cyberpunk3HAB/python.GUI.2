from tkinter import *

def Button_click():
    output_text.delete(1.0, END)
    manipulated_text = "1. Dogs can see in the dark because of the tapetum lucidum 2.a mirror-like membrane in dogs’ eyes 3.There are light-and-motion sensitive cells in the retina that are referred to as rods"
    output_text.insert(END, manipulated_text)

def Button_click1():
    output_text.delete(1.0, END)
    manipulated_text = "1. A house cat’s genome is 95.6 percent tiger, and they share many behaviors with their jungle ancestors"
    output_text.insert(END, manipulated_text)

def Button_click2():
    output_text.delete(1.0, END)
    manipulated_text = "1. Rats are medium-sized rodents with a long tail. A group of rats is called a ‘mischief’! Rats are mainly nocturnal and live underground"
    output_text.insert(END, manipulated_text)

def Button_click3():
    output_text.delete(1.0, END)
    manipulated_text = "1. There are over 30,000 species of fish, There are lots of fish in the sea and some haven't even been discovered yet, Fish breathe through their gills"
    output_text.insert(END, manipulated_text)

def Button_click4():
    output_text.delete(1.0, END)
    manipulated_text = "1. There are 10,000 species of bird, There are around 10,000 different species of bird, All birds lay eggs. All female birds lay eggs"
    output_text.insert(END, manipulated_text)

window = Tk()
window.title("Animal Flashcards")

button1 = Button(window, text="DOG", width=5, pady = 150, background="white", command= Button_click)
button1.grid(row=2, column=0, sticky=W)

button2 = Button(window, text="CAT", width=5, pady = 150, background="cornsilk", command= Button_click1)
button2.grid(row=2, column=1, sticky=W)

button3 = Button(window, text="RAT", width=5, pady = 150, background="lemonchiffon", command= Button_click2)
button3.grid(row=2, column=2, sticky=W)

button4 = Button(window, text="FISH", width=5, pady = 150, background="khaki", command= Button_click3)
button4.grid(row=2, column=3, stick=W)

button5 = Button(window, text="BIRD", width=5, pady = 150, background="gold", command= Button_click4)
button5.grid(row=2, column=4, sticky=W)

output_text = Text(window, width=30, height=20, wrap=WORD, background="yellow")
output_text.grid(row=2, column=5, columnspan=4, sticky=W)

window.mainloop()
