import random
import ART
import time

print(ART.logo)
print(ART.message)

# game function choosing number between 1 and 100 randomly
def game():
    # generating a random number
    number=random.randint(1,100)
    
    # level the user want to play hand/easy
    level=input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    # assigning the lives/ number of attempts
    if level=='hard':
        attempts=5
    elif level=='easy':
        attempts=10

    # telling the user the number of attempts the user have
    print(f"You have {attempts} attempts remaining to guess the number.")
    
    # taking guess from the user till the time he has atleast 1 attempt left
    while attempts>=1:
        guess=int(input("Make a guess: "))

        # if guess is the correct number
        if guess==number:
            print(f"You got it! The answer was {number}.")
            break
        # if guess is not the correct number
        else:
            attempts-=1 # 1 attempt completed
            # incase the game is over
            if attempts==0:
                print("You've run out of guesses, you lose.")
            # if the game is not over, giving user some hint
            else:
                if guess<number:
                    print("Too low.")
                    print("Guess again.")
                else:
                    print("Too high.")
                    print("Guess again.")

                print(f"You have {attempts} attempts remaining to guess the number.")

play_game = 'yes'
# running the game till the time user want to play
while play_game=='yes':
    game()
    play_game = input("Wanna Play the game again(yes/no): ").lower()
else:
    print(ART.game_over)
    time.sleep(5)