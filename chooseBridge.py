import random
from tkinter import *
from tkinter import ttk

# 1. Make the screen
# 2. Make title label, then make it bigger
# 3. Change the window size and make it fit the title label
# 4. How do I make a function change its print statement based on what button I press?
# 5. How do I change the font size and button size of the buttons
# 6. How do I use random to assign the correct bridge?
def main():

    bridgeChoices = ['first', 'second', 'third']

    root = Tk()
    root.title("Choose a Bridge")
    root.geometry("700x450")
    root.resizable(False, False)

    titleLabel = Label(root,
                       text="Choose a Bridge!",
                       font=("Courier New", 50))
    titleLabel.pack()

    firstButton = Button(root,
                         text="First",
                         width=12,
                         font=("Courier New", 23),
                         command=lambda: print(bridgeChoices[0]))

    firstButton.place(x=225,y=100)

    secondButton = Button(root,
                          text="Second",
                          width = 12,
                          font=("Courier New", 23),
                          command=lambda: print(bridgeChoices[1]))

    secondButton.place(x=225, y=200)

    thirdButton = Button(root,
                         text="Third",
                         width = 12,
                         font=("Courier New", 23),
                         command= lambda: print(bridgeChoices[2]))
    

    thirdButton.place(x=225, y = 300)
    root.mainloop()


main()