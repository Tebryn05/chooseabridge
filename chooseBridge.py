import random
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# 1. Make the screen
# 2. Make title label, then make it bigger
# 3. Change the window size and make it fit the title label
# 4. How do I make a function change its print statement based on what button I press?
# 5. How do I change the font size and button size of the buttons
# 6. How do I use random to assign the correct bridge?


def checkChoice(choiceList, choice, correctBridgeChoice):
    if choiceList.index(choice) == correctBridgeChoice:
        print(choice + " correct")
        messagebox.showinfo(title="Choice", message="Correct Choice!")
    else:
        print(choice + " wrong")
        messagebox.showinfo(title="Choice", message="Wrong Choice.")

def restartGame(root):
    root.destroy()
    main()
    
def helpGame(root):
    print("Blah Blah Blah")
    messagebox.showinfo(title="Instructions",
                        message="You have three bridges. Two will break and one is sturdy enough to cross. Choose the correct bridge.")

def main():

    correctBridgeChoice = random.randint(0,2)

    bridgeChoices = ['first', 'second', 'third']


    root = Tk()
    root.title("Choose a Bridge")
    root.geometry("700x450")
    root.resizable(False, False)

    gameMenu = Menu(root)

    game = Menu(gameMenu, tearoff=0)
    gameMenu.add_cascade(label="Game", menu = game)
    game.add_command(label="Restart Game", command = lambda: restartGame(root))
    game.add_separator()
    game.add_command(label = "Exit", command = root.destroy)

    help = Menu(gameMenu, tearoff = 0)
    gameMenu.add_cascade(label="Help", menu = help)
    help.add_command(label="How To Play", command = lambda: helpGame(root))

    
    titleLabel = Label(root,
                       text="Choose a Bridge!",
                       font=("Courier New", 50))
    titleLabel.pack()

    firstButton = Button(root,
                         text="First",
                         width=12,
                         font=("Courier New", 23),
                         command=lambda: checkChoice(bridgeChoices,bridgeChoices[0], correctBridgeChoice))

    firstButton.place(x=225,y=100)

    secondButton = Button(root,
                          text="Second",
                          width = 12,
                          font=("Courier New", 23),
                          command=lambda: checkChoice(bridgeChoices,bridgeChoices[1], correctBridgeChoice))

    secondButton.place(x=225, y=200)

    thirdButton = Button(root,
                         text="Third",
                         width = 12,
                         font=("Courier New", 23),
                         command=lambda: checkChoice(bridgeChoices,bridgeChoices[2], correctBridgeChoice))
    

    thirdButton.place(x=225, y = 300)

    root.config(menu = gameMenu)
    root.mainloop()

main()