#เกมสุ่มตัวเลข
import random
import time

target = 72
minnumber = 0
maxnumber = 100
count = 1

for num in range(maxnumber+1):
    print("Choose number between 0-100:")
    randomnumber = int(input(""))
    if randomnumber > maxnumber or randomnumber < minnumber:
        print("Sorry, your guess is out of range. Try the number between 0-100")
    elif randomnumber < target:
        print("Sorry, your guess is too low. Try the higher number")
    elif randomnumber > target:
        print("Sorry, your guess is too high. Try the lower number.")
    else:
        print("Congratulations, your guess is correct. Total number of guesses is " + str(count) + "!\n")
        break
    count += 1


time.sleep(1)
#เกมโบวลิ่ง
maxround = 10
maxscore = 10
totalscore = 0
maxbowling = 2

for x in range(1, maxround+1):
    score = 0
    round = 0
    leftscore = 10
    print("Round " + str(x) + ":")
    for z in range(1, maxbowling+1):
        rand = random.randint(0, leftscore)
        round += 1
        score += rand
        print("Bowling " + str(z) + " Score: " + str(rand))
        if score >= maxscore and round == 1:
            print("Strike, Nice Shoot!")
            score = 10
            break
        elif score >= maxscore and round == 2:
            print("Spare, Nice Shoot!")
            score = 10
        elif score < 10 and round == 2:
            print("Open Frame, Nice Shoot!")
        totalscore += rand
        leftscore -= rand
    print("Round " + str(x) + " Total Score: " + str(score) + "!\n")

print("Your total score is " + str(totalscore) + "!, VERY GOOD")

        
            

