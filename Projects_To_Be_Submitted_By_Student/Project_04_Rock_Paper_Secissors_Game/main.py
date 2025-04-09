import random

def play():
    user: str = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    
    if user not in ['r', 'p', 's']:
        return "❌ Invalid input. Please choose 'r', 'p' or 's'."
    

    computer: str = random.choice(['r', 'p', 's'])
    print(f'Computer chose: {computer}')

    if user == computer:
        return "It's a tie 🤝"
    
    # r > s, s > p, p > r

    if is_win(user, computer):
        return 'You won! 🎉'
    
    
    return 'You lost! 💔'

def is_win(player, opponent):
    # return true if player wins
    # r > s, s > p, p > r
     return (player == 'r' and opponent == 's') or \
           (player == 's' and opponent == 'p') or \
           (player == 'p' and opponent == 'r')
    

if __name__ == '__main__':
    print(play())