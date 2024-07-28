import random

Rock='''🪨'''
Paper='''🔖'''
Scissors='''✂️'''
game_images=[Rock,Paper,Scissors]

def play_game():
    while True:
        userchoice=int(input("\nEnter your choice:\nType 0 for Rock\nType 1 for paper\nType 2 for Scissors\n"))
        if userchoice >= 3 or userchoice < 0:
            print("Invalid choice. You lose.")
        else:
            print(game_images[userchoice])
            compchoice=random.randint(0,2)

            print("Computer chose:")
            print(game_images[compchoice])

            if compchoice == userchoice:
                print("It's a tie.")
            elif compchoice==0 and userchoice==2:
                print("You lose.")
            elif compchoice==2 and userchoice==0:
                print("You win.")
            elif compchoice>userchoice:
                print("You lose.")
            elif compchoice<userchoice:
                print("You win.")

            play_again=input("Do you want to play again? (y/n): ")
            if play_again!='y':
                print("Thanks for playing!")
                break

play_game()
                

