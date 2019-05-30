import random
# REPL LOOP
wins = 0
losses = 0
ties = 0

cmds = ["r", "p", "s"]


def compare_answers(player_choice, computer_choice):
    if (player_choice == computer_choice):
        return 0
    elif (player_choice == "r" and computer_choice == "s") or \
         (player_choice == "p" and computer_choice == "r") or \
         (player_choice == "s" and computer_choice == "p"):
        return 1
    else:
        return -1


while True:
        cmd = input("Please Input r/p/s: ")
        print(f"{wins} - {losses} - {ties}")
        opponent_cmd = random.choice(cmds)
        print(f"Opponent chooses: {opponent_cmd}")
        if cmd == "q":
            break
        elif cmd in cmds:
            results = compare_answers(cmd, opponent_cmd)
        else:
            print("I did not understand that command")
            continue
        if results == 1:
            print("You win!")
            wins += 1
        elif results == 0:
            print("You tie")
            ties += 1
        else:
            print("You lose")
            losses += 1

print("Thank you for playing")

# while True:
#         cmd = input("Please Input r/p/s: ")
#         print(f"{wins} - {losses} - {ties}")
#         opponent_cmd = random.choice(cmds)
#         print(f"Opponent chooses: {opponent_cmd}")
#         if cmd == "r":
#             if opponent_cmd == "r":
#                 print("Tie")
#                 ties += 1
#             if opponent_cmd == "p":
#                 print("You Lose")
#                 losses += 1
#             if opponent_cmd== "s":
#                 print("You Win")
#                 wins += 1
#         elif cmd == "p":
#             if opponent_cmd== "p":
#                 print("Tie")
#                 ties+= 1
#             if opponent_cmd== "s":
#                 print("You Lose")
#                 losses += 1
#             if opponent_cmd== "r":
#                 print("You Win")
#                 wins += 1

#         elif cmd == "s":
#             if opponent_cmd == "s":
#                 print("Tie")
#                 ties += 1
#             if opponent_cmd== "r":
#                 print("You Lose")
#                 losses += 1
#             if opponent_cmd== "p":
#                 print("You Win")
#                 wins += 1
#         elif cmd== "q":
#             break
#         else:
#             print("I did not understand that command")

# print("Thank you for playing")
