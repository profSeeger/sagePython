import random

air_force_vision = [
    "The United States Air Force will be a trusted and reliable joint partner with our sister services known for integrity in all of our activities, including supporting the joint mission first and foremost. We will provide compelling air, space, and cyber capabilities for use by the combatant commanders. We will excel as stewards of all Air Force resources in service to the American people, while providing precise and reliable Global Vigilance, Reach and Power for the nation."]
af_mission = "The mission of the United States Air Force is to fly, fight, and win- air power anytime anywhere"
sec_af = "The Honorable Frank Kendall III"
sec_def = "The Honorable Lloyd J. Austin III"
af_cos = "General Charles Q. Brown Jr."
coso = "General John W. Raymond"
mylist = list((0, 1, 2, 3, 4))
score = 0
question_pack_one = [sec_af, sec_def, af_cos, coso, af_mission]
for x in range(0, 4):
    a = random.choice(mylist)
    if a == 0:
        anws = str(input("Who is the Secretary of the Air Force?"))
        if anws == sec_af:
            print("Correct")
            score = score + 1
        else:
            print("incorrect")
            print(anws)
            print("The correct anwser is", sec_af)
        x = x + 1
        mylist.remove(0)
    if a == 1:
        anws = str(input("Who is the Secretary of Defence?"))
        if anws == sec_def:
            print("Correct")
            score = score + 1
        else:
            print("incorrect")
            print(anws)
            print("The correct anwser is", sec_af)
        x = x + 1
        mylist.remove(1)
    if a == 2:
        anws = str(input("Who is the Air Force Cheif of Staff?"))
        if anws == af_cos:
            print("Correct")
            score = score + 1
        else:
            print("incorrect")
            print(anws)
            print("The correct anwser is", af_cos)
        x = x + 1
        mylist.remove(2)
    if a == 3:
        anws = str(input("Who is the Chief of Space Opperations?"))
        if anws == coso:
            print("Correct")
            score = score + 1
        else:
            print("incorrect")
            print(anws)
            print("The correct anwser is", coso)
        x = x + 1
        mylist.remove(3)
    if a == 4:
        anws = str(input("What is the Air Force Mission?"))
        if anws == af_mission:
            print("Correct")
            score = score + 1
        else:
            print("incorrect")
            print(anws)
            print("The correct anwser is", af_mission, "check grammar/spelling")
        x = x + 1
        mylist.remove(4)
print("You scored", score, "/ 5")