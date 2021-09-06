import random

comp_wins = 0
player_wins = 0

def Choose_option():
    user_choice = input("Choose Rock , Paper , Scissor")
    if user_choice in ["Rock", "rock", "r", "R"] :
        user_choice = "r"
    elif user_choice in ["paper", "paper", "p", "P"] :
        user_choice = "p"
    elif user_choice in ["Scissor", "scissor", "s", "S"] :
        user_choice = "s"
    else:
        print("I Dont Understand, try again.")
        Choose_option()
    return user_choice
def Computer_Option():
    comp_choice = random.randint(1,3)
    if comp_choice == 1:
        comp_choice = "r"
    elif comp_choice == 1:
        comp_choice = "p"
    else:
         comp_choice = "s"
    return comp_choice

while True:
    print("")
    user_choice = Choose_option()
    comp_choice = Computer_Option()
    print("")

    if user_choice == "r":
        if comp_choice == "r":
            print("you choose rock. The computer choose rock. You win.")
            player_wins += 1

        elif comp_choice == "p":
            print("you choose paper. The computer choose apper. You tied.")
            player_wins += 1

        elif comp_choice == "s":
            print("you choose paper. The computer choose scissor. You lose.")
            player_wins += 1

    elif user_choice == "s":
        if comp_choice == "r":
            print("You choose scissors. The computer choose rock. You lose.")
            comp_wins += 1

            print("")
            print("Player_wins: " +str(player_wins))
            print("Computer_wins" + str(comp_wins))
            print("")

            user_choice = input("Do you want to play again? (y/n)")
            if user_choice in ["Y", "y", "yes", "Yes"]:
                pass
            elif user_choice in ["N", "n", "no", "No"]:
                break
            else:
                break