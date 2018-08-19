# #_*_ coding:utf-8 _*_


from sys import exit

def dead(why):
    print why, "Good job!"
    exit(0)

def gold_room():
    print "This room is full of gold. How much do you take?"

    next = raw_input("> ")

    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("Man, learn to type a number")

    if how_much < 50 :
        print "Nice, you're not greedy, you win"
        exit(0)
    else:
        dead("You greedy bastard!")


def bear_room():

    bear_moved = False

    while True:
        next = raw_input("> ")

        if next == "take honey":
            dead("The bear looks at you")
        elif next == "taunt bear" and not bear_moved:
            print "The bear was moved...."
            bear_moved = True
        elif next == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif next == "open door" and bear_moved:
            gold_room()
        else:
            print "I got no idea what that means."




def if_func():

    print("88888")



if __name__ == "__main__":
    if_func()

