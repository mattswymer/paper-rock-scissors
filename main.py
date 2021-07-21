if __name__ == '__main__':

    import random

    # Beginning scores
    computer_score = 0
    computer_paper = 0
    computer_rock = 0
    computer_scissors = 0
    user_score = 0
    user_paper = 0
    user_rock = 0
    user_scissors = 0
    user_paper_win = 0
    user_rock_win = 0
    user_scissors_win = 0
    user_paper_tie = 0
    user_rock_tie = 0
    user_scissors_tie = 0
    tie = 0
    number_of_games = 0

    # This is the loop for the game
    while True:

        # This is the loop for the menu
        while True:
            try:
                print("1: paper")
                print("2: rock")
                print("3: scissors")
                print("4: random")
                print("5: stats")
                user_input = int(input("Enter a number: "))

                print("\n")
                # This section tells what option was chosen
                if user_input == 1:
                    print("You chose paper!")
                    user_paper += 1
                    break
                elif user_input == 2:
                    print("You chose rock!")
                    user_rock += 1
                    break
                elif user_input == 3:
                    print("You chose scissors!")
                    user_scissors += 1
                    break
                elif user_input == 4:
                    print("You chose random!")
                    break
                elif user_input == 5:
                    print("You chose stats!")
                    stats()
                else:
                    print("Invalid input!")
                    print("Try again.")
                    print("\n")
            except:
                continue


        # These are the random inputs
        computer_choice = random.randint(1, 3)
        random_choice = random.randint(1, 3)

        # These are the options if a random choice is chosen
        if user_input == 4:
            user_input = random_choice
            if random_choice == 1:
                user_paper += 1
                print("The computer chose paper for you!")
            elif random_choice == 2:
                user_rock += 1
                print("The computer chose rock for you!")
            elif random_choice == 3:
                user_scissors += 1
                print("The computer chose scissors for you!")

        print("\n")

        # These are the computer options
        if computer_choice == 1:
            computer_paper += 1
            print("The computer chose paper!")
        elif computer_choice == 2:
            computer_rock += 1
            print("The computer chose rock!")
        elif computer_choice == 3:
            computer_scissors += 1
            print("The computer chose scissors!")

        print("\n")

        # These are the win-lose-tie conditions and score movements
        # These are the tie conditions
        if user_input == 1 and computer_choice == 1:
            out_put = random.choice(["Ugh...it's a tie. Awesome, bro.", "Seriously? A tie?", "Cool. No one wins."])
            tie += 1
            user_paper_tie += 1
            print(out_put)
        elif user_input == 2 and computer_choice == 2:
            out_put = random.choice(["Ugh...it's a tie. Awesome, bro.", "Seriously? A tie?", "Cool. No one wins."])
            tie += 1
            user_rock_tie += 1
            print(out_put)
        elif user_input == 3 and computer_choice == 3:
            out_put = random.choice(["Ugh...it's a tie. Awesome, bro.", "Seriously? A tie?", "Cool. No one wins."])
            tie += 1
            user_scissors_tie += 1
            print(out_put)

        # These are the user win conditions
        elif user_input == 1 and computer_choice == 2:
            out_put = random.choice(["You win? That's impossible!", "Cool. You beat a machine.", "You win. What? "
                                                                                                 "You "
                                                                                                 "think you're "
                                                                                                 "special "
                                                                                                 "now?"])
            user_score += 1
            user_paper_win += 1
            print(out_put)
        elif user_input == 2 and computer_choice == 3:
            out_put = random.choice(
                ["You win? That's impossible!", "Cool. You beat a machine.", "You win. What? You "
                                                                             "think you're special "
                                                                             "now?"])
            user_score += 1
            user_rock_win += 1
            print(out_put)
        elif user_input == 3 and computer_choice == 1:
            out_put = random.choice(
                ["You win? That's impossible!", "Cool. You beat a machine.", "You win. What? You "
                                                                             "think you're special "
                                                                             "now?"])
            user_scissors_win += 1
            user_score += 1
            print(out_put)

        # These are the computer win conditions
        elif user_input == 1 and computer_choice == 3:
            out_put = random.choice(
                ["I win!! You aren't very good at this!", "You lose. I'm so good. That's the best "
                                                          "you've got?", "Wasn't even close. I won "
                                                                         "without even trying."])
            computer_score += 1
            print(out_put)
        elif user_input == 2 and computer_choice == 1:
            out_put = random.choice(
                ["I win!! You aren't very good at this!", "You lose. I'm so good. That's the best "
                                                          "you've got?", "Wasn't even close. I won "
                                                                         "without even trying."])
            computer_score += 1
            print(out_put)
        elif user_input == 3 and computer_choice == 2:
            out_put = random.choice(
                ["I win!! You aren't very good at this!", "You lose. I'm so good. That's the best "
                                                          "you've got?", "Wasn't even close. I won "
                                                                         "without even trying."])
            computer_score += 1
            print(out_put)

        number_of_games += 1

        # This is the stats function
        def stats():
            computer_percentage = round((computer_score / number_of_games) * 100, 2)
            user_percentage = round((user_score / number_of_games) * 100, 2)
            tie_percentage = round((tie / number_of_games) * 100, 2)
            user_paper_win_percentage = round((user_paper_win / user_paper) * 100, 2)
            user_rock_win_percentage = round((user_rock_win / user_rock) * 100, 2)
            user_scissors_win_percentage = round((user_scissors_win / user_scissors) * 100, 2)
            print("Number of games: {}".format(number_of_games))
            print("\n")
            print("Your wins: {}".format(user_score))
            print("Your win percentage: {}".format(user_percentage))
            print("\n")
            print("Computer's wins: {}".format(computer_score))
            print("Computer's win percentage: {}".format(computer_percentage))
            print("\n")
            print("Ties: {}".format(tie))
            print("Tie percentage: {}".format(tie_percentage))
            print("\n")
            print("Computer chose paper {} times.".format(computer_paper))
            print("Computer chose rock {} times.".format(computer_rock))
            print("Computer chose scissors {} times.".format(computer_scissors))
            print("\n")
            print("You chose paper {} times.".format(user_paper))
            print("You won {} times and tied {} times when you chose paper.".format(user_paper_win, user_paper_tie))
            print("You win {} percent of the time when you choose paper.".format(user_paper_win_percentage))
            print("\n")
            print("You chose rock {} times.".format(user_rock))
            print("You won {} times and tied {} times when you chose rock.".format(user_rock_win, user_rock_tie))
            print("You win {} percent of the time when you choose rock.".format(user_rock_win_percentage))
            print("\n")
            print("You chose scissors {} times.".format(user_scissors))
            print(
                "You won {} times and tied {} times when you chose scissors.".format(user_scissors_win, user_scissors_tie))
            print("You win {} percent of the time when you choose scissors.".format(user_scissors_win_percentage))
            print("\n")


        print("\n")

        # This breaks the loop to stop playing
        if input('Do you want to play again? (y/n)') == 'n':
            break

        print("\n")
