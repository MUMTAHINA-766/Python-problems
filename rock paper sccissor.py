#write a small function to depict a rock-paper-scissors game.your function should take two inputs and should give us the winner based on a certain condition.

print("Enter rock , paper , scissors: ")
p1 = input()
print("Enter rock , paper , scissors: ")
p2 = input()

def rpc_game(a, b):
    if a == b:
        return "It's a tie!"
    elif a == "rock":
        if b == "scissors":
            return "Rock beats sciessors!"
        else:
            return "Paper beats rock!"
    elif a == "scissors":
        if b == "paper":
            return "scissors beat paper!"
        else:
            return "Rock beats scissors!"
    elif a == "paper":
        if b == "rock":
            return "Paper beats rock!"
        else:
            return "Scissors beat paper!"
    else:
        return "You have not entered rock, paper or scissors."

print(rpc_game(p1, p2))
