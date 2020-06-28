import random
import tkinter as tk

#NOTE: A function that determines whether the user wins or not
#      Passes the user's choice (based on what button they click)to the parameter
def get_winner(call):

    # Access variables declared after the function so that the variables can be changed inside of the function
    global wins, win, output, losses, youLabel, comLabel

    # 1. Create random integer 1-3 to use as computer's play
    play = random.randint(1,3)

    # 2. Using if-statements, assign the computer to a choice (rock, paper, scissors) using the random integer generated
    choice = ""
    if play == 1:
        choice = "rock"
    elif play == 2:
        choice = "paper"
    else:
        choice = "scissors"
    # 3. Determine the winner based on what the user chose and what the computer chose
    #   Rock beats Scissors


    #   Paper beats Rock
    #   Scissors beats Paper
    #   It's a tie if the computer and user chose the same object
    # If the user wins, increase win by 1
    # Use the output label to write what the computer did and what the result was (win, loss, tie)
    win = True
    print(f"you: {call}")
    print(f"comp: {choice}")
    tie = False
    if call == choice:
        tie = True
        win = True
    elif call == "rock":
        if choice == scissors:
            win = True
        else:
            win = False
    elif call == "paper":
        if choice == "rock":
            win = True
        else:
            win = False
    else:
        if choice == "paper":
            win = True
        else:
            win = False
    if tie:
        wins = wins + 1
        losses = losses+1
    elif win:
        wins = wins + 1
    else:
        losses = losses + 1
    youLabel.config(text=f"Wins for You: {wins}")
    comLabel.config(text=f"Wins for Computer: {losses}")
    totalLabel.config(text=f"{wins} - {losses}")


# Use these functions as "command" for each button
def pass_s():
    get_winner("scissors")
def pass_r():
    get_winner("rock")
def pass_p():
    get_winner("paper")

window = tk.Tk()

#Variable to count the number of wins the user gets


#START CODING HERE

# 1. Create 3 buttons for each option (rock, paper, scissors)
rock = tk.Button(
    text="rock",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
    command=pass_r
)

#rock.pack()

paper = tk.Button(
    text="paper",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
    command=pass_p
)

#paper.pack()

scissors = tk.Button(
    text="scissors",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
    command=pass_s
)

#scissors.pack()

# 2. Create 2 labels for the result and the number of wins
wins = 0
losses = 0
youLabel = tk.Label(
    text=f"Wins for You: {wins}",
    fg="white",
    bg="black",
    width=25,
    height=5
)

#youLabel.pack()

comLabel = tk.Label(
    text=f"Wins for Computer: {losses}",
    fg="white",
    bg="black",
    width=25,
    height=5,
)

totalLabel = tk.Label(
    text=f"{wins} - {losses}",
    fg="white",
    bg="black",
    width=25,
    height=5,
)
#comLabel.pack()

rock.grid(row=0,column=0)
paper.grid(row=0,column=1)
scissors.grid(row=0,column=2)
youLabel.grid(row=1,column=0)
comLabel.grid(row=1,column=1)
totalLabel.grid(row=1,column=2)

window.mainloop()
