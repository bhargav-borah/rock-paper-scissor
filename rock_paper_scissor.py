import random

options = ["r", "p", "s"]

human_score = 0
comp_score = 0

def display(inp):
   
    if inp == "r":
        return "Rock"
    elif inp == "p":
        return "Paper"
    elif inp == "s":
        return "Scissor"
       
def eval_game(human_inp, comp_inp):
    global human_score, comp_score, game_num
    print(f"Human: {display(human_inp)} v/s Computer: {display(comp_inp)}")
    if human_inp == "r":
        if comp_inp == "s":
            print("You win this round")
            human_score += 1
          
        elif comp_inp == "p":
            print("Computer wins this round")
            comp_score += 1
           
        elif comp_inp == "r":
            print("This round has been drawn")
    elif human_inp == "p":
        if comp_inp == "r":
            print("You win this round")
            human_score += 1
          
        elif comp_inp == "s":
            print("Computer wins this round")
            comp_score += 1
           
        elif comp_inp == "p":
            print("This round has been drawn")
    elif human_inp == "s":
        if comp_inp == "p":
            print("You win this round")
            human_score += 1
          
        elif comp_inp == "r":
            print("Computer wins this round")
            comp_score += 1
          
        elif comp_inp == "s":
            print("This round has been drawn")
    display_score()
           
def display_score():
    print(f"Human: {human_score}  | Computer: {comp_score}")
    print()
   
def check_continuation(tries):
   
    if comp_score == tries:
        print("Game over! The computer won the game")
        return False
    elif human_score == tries:
        print("Yayy!! You won this game!")
        return False
    return True
   
def play(tries):
   
    while True:
            human_inp = input("Enter your choice(r/p/s): ").lower()
            if human_inp in options:
                break
            else:
                print("Invalid input. Enter a valid choice")
       
       
    comp_inp = random.choice(options)
   
    eval_game(human_inp, comp_inp)
   
   

print("Rock(R), Paper(P), Scissor(S)")
print()

while True:
    try:
        tries = int(input("Best of -> "))
        print()
        break;
    except:
        print("Invalid input. Enter a natural no.")

game_on = True
while game_on:
    play(tries)
    game_on = check_continuation(tries)

