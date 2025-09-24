import random
def play_for_100(target=100, p_win=0.6):
    balance=0
    rounds=0

    while balance<target:
        rounds += 1
        if random.random() < p_win:
            balance +=1
        else:
            balance -=1
    return rounds


rounds_played= play_for_100(target=100, p_win=0.6)
print(f"Number of rounds played to win $100: {rounds_played}")