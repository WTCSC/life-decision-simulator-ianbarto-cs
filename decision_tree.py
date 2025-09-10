import time
from time import sleep
from variables import *

start()
decision1 = input(ques1)
sleep(1)

if decision1 == ("1"):
    snooze()
    decision2 = (input("Would you like to [1] Brush your teeth or [2] Take a shower: "))
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
        if decision3 == ("1") or decision3 == ("2"):
            candy_choice()
            decision4 = input("You are in your movie and you and your mother are the only people there... Do you [1] get in better seats [2] Keep the seats you payed for: ")
            if decision4 == ("1"):
                better_seats()
            if decision4 == ("2"):
                keep_seats()


if decision1 == ("2"):
    decision2 = input("Congrats on actually waking up early, would you like to [1] Scroll ig reels for 10 minutes or [2] Get breakfast: ")
    if decision2 == ("1"):
        ig_reels()
        decision3 = input("Do you [1] Tell the school that you are not putting your phone in pouch prison, or [2] Comply with the school and do it their way: ")
        if decision3 == ("1"):
            no_pouch()
            decision4 = input("Your time to relax is over, you have 20 minutes till dinner... Do you [1] finish your homeword or [2] Procrastinate till you need to go to bed, and miss out on sleep to do your homework: ")
            if decision4 == ("1"):
                finish_homework()
            if decision4 == ("2"):
               procrastinate()
        if decision3 == ("2"):
            comply_phone()
    if decision2 == ("2"):
        get_brecky()
        decision3 = input("So you finish breakfast and go to school, do you [1] screw around in the middle of class with a substitue, or [2] Focus on your work so you have more freetime later: ")
        if decision3 == ("1"):
            sub_mess_around()
        if decision3 == ("2"):
            focus_school()
else:
    print("You typed something wrong, please try again")

print("Thanks for playing the life simulation")
sleep(0.8)
print("I hope you made it far")