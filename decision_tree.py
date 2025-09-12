import time
from time import sleep
from variables import *

start()
decision1 = input(ques1)
sleep(1)

if decision1 == ("1"):
    snooze()
    decision2 = input(ques2)
    if decision2 == ("1"):
        brush_teeth()
        decision3 = input(ques3)
        if decision3 == ("1"):
            go_school()
            decision4 = input(ques4)
            if decision4 ==("1"):
                run_home()
            if decision4 == ("2"):
                stay_school()
        if decision3 == ("2"):
            fake_sick()
    if decision2 == ("2"):
        take_shower()
        decision3 = input(ques5)
        if decision3 == ("1") or decision3 == ("2"):
            candy_choice()
            decision4 = input(ques6)
            if decision4 == ("1"):
                better_seats()
            if decision4 == ("2"):
                keep_seats()


if decision1 == ("2"):
    decision2 = input(ques7)
    if decision2 == ("1"):
        ig_reels()
        decision3 = input(ques8)
        if decision3 == ("1"):
            no_pouch()
            decision4 = input(ques9)
            if decision4 == ("1"):
                finish_homework()
            if decision4 == ("2"):
               procrastinate()
        if decision3 == ("2"):
            comply_phone()
    if decision2 == ("2"):
        get_brecky()
        decision3 = input(ques10)
        if decision3 == ("1"):
            sub_mess_around()
        if decision3 == ("2"):
            focus_school()
else:
    print("You typed something wrong, please try again")

ending_message()