from turtle import Turtle, Screen;
import random;
import os

def clear_console():
    os.system('cls')


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')  # Function to clear the console
def race():

    ship = "images/ship.gif";
    ship1 = "images/ship1.gif";
    ship2 = "images/ship2.gif";
    ship3 = "images/ship3.gif";


    is_race_on = False;


    screen = Screen();
    screen.setup(width=700, height=600)
    screen.bgcolor("black")
    screen.bgpic("images/bg.png") 


    ship_images = [ship, ship1, ship2, ship3];
    ship_list = [];
    x_cordinates = [-200, -100, 100, 200];

    for ship in ship_images:
        screen.addshape(ship);

    for i in range(len(x_cordinates)):
        pointer = Turtle();
        pointer.speed(10)
        pointer.shape(ship_images[i])
        pointer.seth(90);
        pointer.pu();
        pointer.goto(x=x_cordinates[i], y=-170);
        ship_list.append(pointer);

    user_bet = screen.textinput(title="Make a bet", prompt="Which ship will win the race from left to right (1/2/3/4)?: ").lower()
    print(f"User bet is: {user_bet}");

    if user_bet:
        is_race_on = True;

    winner = None;

    while is_race_on:
        
        for index, ship in enumerate(ship_list):
            if ship.ycor() > 230:
                winner = index + 1;
                is_race_on = False;
                print(f"Ship: {winner} Won");
                if winner == int(user_bet):
                    print(f"You won the bet, ship number: {winner} won.");
                else:
                    print(f"You lost ship number: {winner} won");
                
            
            random_distance = random.randint(0,10)
            ship.forward(random_distance);




screen = Screen() 
play_again = 'yes'


while play_again == 'yes':
    race()
    play_again = screen.textinput("Play Again?", "Do you want to play again? (yes/no)").lower();
    clear_console()