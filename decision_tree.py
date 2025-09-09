import time
from time import sleep
from variables import *

start()
decision1 = input(ques1)
sleep(1)

if decision1 == ("1"):
    snooze()
    decision2 = (input("Would you like to [1] Brush your teeth or [2] Take a shower: "))
    sleep(1)
    if decision2 == ("1"):
        brush_teeth()
        decision3 = input("Would you like to [1] Go to school or [2] Fake sick and stay home: ")
        if decision3 == ("1"):
            go_school()
            decision4 = input("Do you [1] Run home or [2] Stay in the field bored for an hour: ")
            if decision4 ==("1"):
                run_home()
            if decision4 == ("2"):
                stay_school()
        if decision3 == ("2"):
            fake_sick()
    if decision2 == ("2"):
        take_shower()
        decision3 = input("Would you like to get [1] Popcorn or [2] Nerds gummy clusters: ")
        if decision3 == ("1"):
            print("Good choice")

if decision1 == ("2"):
    decision2 = input("Congrats on actually waking up early, would you like to [1] Scroll ig reels for 10 minutes or [2] Get breakfast: ")
else:
    print("You typed something wrong, please try again")