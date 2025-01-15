import random

import player_class as pc

def playerTurn(attacker,target):
    x = input("What do you do, [" + str(getattr(target, 'name')) + "]?\n")
    if x in "attack":
        if attacker.can_hit(target.speed):
            x = target.attack(attacker)
            attacker.health = x
            print(str(attacker.name) + " has [" + str(attacker.health) + "] health left.")
    elif x in "disengage":
        target.disengage()

def main():
    p1In = input("What is your name, player_1?\n")
    p2In = input("What is your name, player_2?\n")

    player1 = pc.player(250,10,21,.22,p1In) ## Represents the strongest possible player/class
    #player2 = pc.player(75,1,7,.05,p2In) ## Represents the weakest player/class
    player2 = pc.player(75, 7, 7, .05, p2In)

    p1Initiative = round(random.random()*20,0)
    p2Initiative = round(random.random()*20,0)

    ## Stole the initiative straight from D&D, I've been playing a lot of BG3
    if p1Initiative > p2Initiative:
        first = player1
        second = player2
    else:
        first = player2
        second = player1

    while first.is_alive() and second.is_alive():
        playerTurn(first,second)
        playerTurn(second,first)
main()