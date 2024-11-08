
f = open("scoreboard", "w")

from random import randint
from collections import Counter


special_chars = '@_!#$%^&*()<>?/\|}{~:;.[]'
special_chars2 = '@_!#$%^&*()<>?/\|}{~:;[]'

print("-" * 20 + " Welcome to Roulette! " + "-" * 20 + "\n")
print(
    "Rules" + "\n" + "\n" + "- You must enter all the information asked below to begin your game.You are given a starting balance of $100." + "\n" + "- You will guess a number from 0-36. If your guess matches the generated winning number, you will win money in that round." + "\n" + "- If you guess incorrectly, you lose money. However, this game lasts five total rounds, adding and subtracting from your total as the rounds progress." + "\n" + "- At the end of the game, you will be shown the leaderboard with the overall winner by points." + "\n" + "Good Luck!" + "\n" + "\n" + "-" * 40 + "\n")
# input num of players. If too many, error, else continue
players = input("Enter the number of players: ")
while players.isspace() or players == "" or not players.isnumeric() or int(players) > 20 or players in special_chars:
    if players.isalpha():
        print("Input a number.")
        players = input("Enter the number of players: ")
    elif players.isspace() or players == "":
        print("Input a number.")
        players = input("Enter the number of players: ")
    elif "-" in players:
        print("Input a positive number.")
        players = input("Enter the number of players: ")
    elif players in special_chars:
        print("Input a number.")
        players = input("Enter the number of players: ")
    elif int(players) > 20:
        print("Too many players")
        players = input("Enter the number of players: ")


else:
    my_list = []
    # Collects the names and ages of players and appends them to a list, creating a 2D list (my_list)
    for i in range(int(players)):
        player_name = input("Player " + str(i + 1) + " name: ")
        while any(player_name in x for x in my_list) or player_name.isspace() or "" == player_name:
            if any(player_name in x for x in my_list):
                print("Names cannot be the same.")
                player_name = input("Player " + str(i + 1) + " name: ")
            elif player_name.isspace() or player_name == "":
                print("Enter a name.")
                player_name = input("Player " + str(i + 1) + " name: ")

        player_age = input("Player " + str(i + 1) + " age: ")
        while not player_age.isnumeric():
            if player_age.isalpha():
                print("Please enter a valid age.")
                player_age = input("Player " + str(i + 1) + " age: ")
            elif "-" in player_age:
                print("Please enter a valid age.")
                player_age = input("Player " + str(i + 1) + " age: ")
            elif player_age.isspace() or player_age == "":
                print("Please enter a valid age.")
                player_age = input("Player " + str(i + 1) + " age: ")
            elif player_age in special_chars:
                print("Please enter a valid age.")
                player_age = input("Player " + str(i + 1) + " age: ")

        my_list.append([player_name, int(player_age), 100])

    print("\n" + "-" * 40)
    # Generates winning number
    winning_num = randint(0, 36)
    # print(winning_num)

    # looping so program can run for 5 rounds
    for j in range(5):
        # loops for each player to get their information for calculation
        print("\n" + "Round " + str(j + 1))
        for i in range(int(players)):
            print("\n" + my_list[i][0] + ", you have $" + str(my_list[i][-1]))
            bet_amt = input(my_list[i][0] + ", enter the amount of money you would like to bet: ")
            while not bet_amt.isdigit() or float(bet_amt) <= 0:
                if bet_amt.isalpha():
                    print("Enter a valid bet.")
                    bet_amt = input(my_list[i][0] + ", enter the amount of money you would like to bet: ")
                elif bet_amt in special_chars2:
                    print("Enter a valid bet.")
                    bet_amt = input(my_list[i][0] + ", enter the amount of money you would like to bet: ")
                elif float(bet_amt) <= 0:
                    print("Enter a bet greater than 0.")
                    bet_amt = input(my_list[i][0] + ", enter the amount of money you would like to bet: ")
                elif bet_amt.isspace() or bet_amt == "":
                    print("Enter a valid bet.")
                    bet_amt = input(my_list[i][0] + ", enter the amount of money you would like to bet: ")
                elif "." in bet_amt:
                    break

            bet_num_amt = input("Enter the amount of numbers you would like to guess: ")
            while not bet_num_amt.isnumeric() or int(bet_num_amt) <= 0:
                if bet_num_amt.isalpha():
                    print("Enter a valid number.")
                    bet_num_amt = input("Enter the amount of numbers you would like to guess: ")
                elif bet_num_amt.isspace() or bet_num_amt == "":
                    print("Enter a valid number.")
                    bet_num_amt = input("Enter the amount of numbers you would like to guess: ")
                elif bet_num_amt in special_chars:
                    print("Enter a valid number.")
                    bet_num_amt = input("Enter the amount of numbers you would like to guess: ")
                elif int(bet_num_amt) <= 0:
                    print("Enter a bet greater than 0.")
                    bet_num_amt = input("Enter the amount of numbers you would like to guess: ")

            guess_list = []
            # Makes list of all guessed numbers for that round
            for x in range(int(bet_num_amt)):
                choice_num = input("Enter your guess (0-36): ")
                while not choice_num.isnumeric() or int(choice_num) < 0 or int(
                        choice_num) > 36 or choice_num.isspace() or choice_num == "":
                    if choice_num.isalpha():
                        print("Enter a valid bet.")
                        choice_num = input("Enter your guess (0-36): ")
                    elif choice_num in special_chars:
                        print("Enter a valid bet.")
                        choice_num = input("Enter your guess (0-36): ")
                    elif int(choice_num) <= 0:
                        print("Enter a bet greater than 0.")
                        choice_num = input("Enter your guess (0-36): ")
                    elif int(choice_num) > 36:
                        print("Your guess must be equal to or below 36.")
                        choice_num = input("Enter your guess (0-36): ")
                    elif choice_num.isspace() or choice_num == "":
                        print("Enter a valid bet.")
                        choice_num = input("Enter your guess (0-36): ")

                guess_list.append(int(choice_num))

            # Gets if user wants off even or neither
            odd_even = input("Guess if the number is odd or even (Enter \"n\" to skip): ")
            while not odd_even.isalpha() or " " in odd_even or odd_even in special_chars:
                if odd_even.isnumeric():
                    print("Enter a valid guess.")
                    odd_even = input("Guess if the number is odd or even (Enter \"n\" to skip): ")
                elif odd_even.isspace() or odd_even == "":
                    print("Enter a valid guess.")
                    odd_even = input("Guess if the number is odd or even (Enter \"n\" to skip): ")
                elif "-" in odd_even:
                    print("Enter a valid guess.")
                    odd_even = input("Guess if the number is odd or even (Enter \"n\" to skip): ")
                elif " " in odd_even:
                    print("Please enter odd, even, or n.")
                    odd_even = input("Guess if the number is odd or even (Enter \"n\" to skip): ")
                elif odd_even in special_chars:
                    print("Please enter odd, even, or n.")
                    odd_even = input("Guess if the number is odd or even (Enter \"n\" to skip): ")
            odd_even_fin = odd_even

            # if they guess the number right
            if int(winning_num) in guess_list:
                win_dollars = 37 * float(bet_amt) / int(bet_num_amt)
                if odd_even_fin.lower() == "even":
                    # number and even right
                    if int(winning_num) % 2 == 0:
                        win_dollars = float(win_dollars) * 2
                    else:
                        win_dollars = float(win_dollars) / 2
                elif odd_even_fin.lower() == "odd":
                    # number and odd right
                    if int(winning_num) % 2 == 0:
                        win_dollars = float(win_dollars) / 2
                    else:
                        win_dollars = float(win_dollars) * 2
                else:
                    win_dollars = win_dollars
                my_list[i][-1] += float(win_dollars)

            else:
                # if they guess the number wrong
                if odd_even_fin.lower() == "even":
                    # number wrong but even right
                    if int(winning_num) % 2 == 0:
                        loss_dollars = float(bet_amt) / 2
                    else:
                        # number wrong and even wrong
                        loss_dollars = float(bet_amt) * 2
                elif odd_even_fin.lower() == "odd":
                    # number wrong and odd wrong
                    if int(winning_num) % 2 == 0:
                        loss_dollars = float(bet_amt) * 2
                    else:
                        # number wrong but odd right
                        loss_dollars = float(bet_amt) / 2
                else:
                    loss_dollars = float(bet_amt)
                my_list[i][-1] -= float(loss_dollars)

    print("\n" + "-" * 40 + "\n")
    my_dict = {}
    # Create a dictionary with name as key and score as value
    for i in range(len(my_list)):
        my_dict.update({my_list[i][0]: my_list[i][-1]})
    # Sorts dictionaryand prints highest score first
    x = dict(sorted(my_dict.items(), key=lambda item: item[1]))
    res = dict(reversed(list(x.items())))
    print("Final Scores")
    counter = 0
    winner = (next(iter(res)))
    # prints highest score in green
    winners = []
    for i in res:
        if counter == 0:
            print(str(i) + ': ' + str(res[i]))
            # writes first score in file
            f.write(str(i) + ': ' + str(res[i]))
            f.write("\n")
            high_score = res[i]
            winners.append(str(i))
            counter += 1
        else:
            if res[i] == high_score:
                print(str(i) + ': ' + str(res[i]))
                # writes first score in file
                f.write(str(i) + ': ' + str(res[i]))
                f.write("\n")
                winners.append(str(i))
            else:
                print(str(i) + ': ' + str(res[i]))
                # writes rest of scores in file
                f.write(str(i) + ': ' + str(res[i]))
                f.write("\n")
            counter += 1

    del res[next(iter(res))]

    f.close()

    print("\n" + "-" * 40 + "\n")

    # calculates average score by age
    print("Average Balance By Age")
    age_list = []
    for i in range(len(my_list)):
        age_list.append(int(my_list[i][1]))
        c = Counter(age_list)
    items = c.items()
    # print(items)

    age_val = []
    # appends age and occurances as list inside larger list
    for key, value in items:
        age_val.append([key, value])
    # print(age_val)

    # goes through list and finds if ages are the same. If they are, it adds them together in a loop. Outside loop, it divides by numbers that were added together
    for i in range(len(age_val)):
        total_balance = 0
        for player in my_list:
            if player[1] == age_val[i][0]:
                total_balance += player[2]
            # print(total_balance)
        total_avg = total_balance / age_val[i][1]
        age_val[i][-1] = total_avg

    for i in range(len(age_val)):
        print("Age: " + str(age_val[i][0]) + "\t" + "Average Score: " + str(age_val[i][-1]))
    print("\n" + "-" * 40 + "\n")
    print("*   *       *            *          *" + "\n" + "     *      *   *         *       *    ")
    print("\t" + "Congratulations " + " and ".join(winners) + "!")
    print("       *    *            *      *    " + "\n" + "*    *      *            *          *")
    print("\n" + "Thanks for playing!")
