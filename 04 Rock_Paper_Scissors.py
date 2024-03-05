import random
seznam = {"r":"rock","p":"paper","s":"scissors"}
winning_combinations = {"r": "s", "s": "p","p": "r"}

def play():
    user = input("'r' for rock, 'p' for paper, 's' for scissors: ")
    computer = random.choice(["r", "p", "s"])
    print(f"Computer chose {seznam[computer]}!")

    if user == computer:
        return "It's a tie"
    
    if is_win(user, computer):
        return "You won!"
    
    return "You lost!"

def is_win(player, opponent):

    # return true if player wins
    # r > s, s > p, p > r
    if player in winning_combinations and winning_combinations[player] == opponent:
        return True
        
print(play())