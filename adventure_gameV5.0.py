import time


import random


import string


def typewriter_simulator(message):
    for char in message:
        print(char, end='')
        if char in string.punctuation:
            time.sleep(.5)
        time.sleep(.03)
    print('')


def print_pause(message, delay=1):
    typewriter_simulator(message)
    time.sleep(delay)


def intro(villain, colors):
    print_pause("""You find yourself standing in an open field,
    ... filled with grass and """ + colors + " wildflowers.")
    print_pause("Rumor has it that a " + villain + """ is somewhere around
    ... here, and has been terrifying the nearby village.""")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("""In your hand you hold your trusty
    ...(but not very effective) dagger.""")


def one_two(items, villain, colors):
    print_pause("Please select 1 or 2.")
    response = input()
    if response == '1':
        house(items, villain, colors)
    elif response == '2':
        bear_attack = ["live", "die"]
        bear = random.choice(bear_attack)
        cave(items, villain, bear, colors)
    else:
        print_pause("Sorry I don't understand.")
        one_two(items, villain, colors)


def field(items, villain, colors):
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    one_two(items, villain, colors)


def play_again():
    while True:
        p_a = input("Would you like to play again? (y/n)").lower()
        if p_a == "y":
            print_pause("Excellent! Restarting the game ...")
            play_adventure_game()
        elif p_a == "n":
            exit("Thanks for playing! See you next time.")
        else:
            print_pause("Please enter a choice of y (for yes) or n (for no).")


def house(items, villain, colors):
    print_pause("You approach the door of the house.")
    print_pause("""You are about to knock when the door opens and
     ...out steps a """ + villain + ".")
    print_pause("Eep! This is the " + villain + "'s house!")
    print_pause("The " + villain + " attacks you!")
    if "Sword of Ogoroth" not in items:
        print_pause("""You feel a bit under-prepared for this, what with only
        ...having a tiny dagger.""")
    while True:
        fight_or_flight = input("Would you like to (1) fight or (2) run away?")
        if fight_or_flight == "1":
            if "Sword of Ogoroth" in items:
                print_pause("As the " + villain + """ moves to attack,
                ...you unsheath your new sword.""")
                print_pause("""The Sword of Ogoroth shines brightly in your
                ...hand as you brace yourself for the attack.""")
                print_pause("But the " + villain + """ takes one look at your
                ...shiny new toy and runs away!""")
                print_pause("""You have rid the town
                ...of the """ + villain + ".")
                print_pause("You are victorious!")
                play_again()
            else:
                print_pause("You do your best...")
                print_pause("but your dagger is no match for the ")
                print_pause(villain + ".")
                print_pause("You have been defeated!")
                play_again()
        if fight_or_flight == "2":
            if "Sword of Ogoroth" in items:
                print_pause("You trip onto your Sword of Ogoroth")
                print_pause("Why did you run with such a big sword?")
                print_pause("You died.")
                play_again()
            else:
                print_pause("""You run back into the field.
                ...Luckily, you don't seem to have been followed.""")
                field(items, villain, colors)


def cave(items, villain, bear, colors):
    if "Sword of Ogoroth" in items:
        print_pause("You peer cautiously into the cave.")
        print_pause("You've been here before, and gotten all the good stuff.")
        print_pause("It's just an empty cave now.")
        print_pause("...")
        print_pause("...")
        print_pause("ROOOAAAAAR!!!")
        print_pause("It seems you have awakened a bear from hibernation!")
        print_pause("You reach for your Sword of Ogoroth...")
        print_pause("But it is TOO LATE!")
        print_pause("The bear has got you.")
        print_pause("You struggle to fight off the bear...")
        if "live" in bear:
            print_pause("You manage to poke the bear in the eyes.")
            print_pause("The bear scampers off.")
            print_pause("You run out into the field, to safety.")
            field(items, villain, colors)
        if "die" in bear:
            print_pause("But to no avail.")
            print_pause("You become the bear's dinner.")
            play_again()
    else:
        print_pause("You peer cautiously into the cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("""You discard your silly old dagger
        ...and take the sword with you.""")
        print_pause("You walk back out to the field.")
        print_pause("""You find yourself standing in an open field,
        ... filled with grass and """ + colors + " wildflowers.")
        items.append("Sword of Ogoroth")
    field(items, villain, colors)


def play_adventure_game():
    villain = random.choice(["wicked fairie", "gorgon", "pirate",
                            "dragon", "aggressive duck"])
    colors = random.choice(["red", "orange", "yellow", "blue", "violet"])
    intro(villain, colors)
    items = []
    field(items, villain, colors)


play_adventure_game()
