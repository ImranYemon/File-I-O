# import for the game 
import random
# function define
def game ():
    print("Let's play ...")
# Score genarate 
    score = random.randint(1,100)
    print(f"Your score is {score}")
# file opening for reading , if the file is empty then hiscore is 0 or it's in int form .
    with open("hiscore.txt" , "r") as f :
        hiscore = f.read()
        if (hiscore !=""):
            hiscore = int(hiscore)
        else:
            hiscore = 0 
# if new score is higest then write the score into the hiscore . 
    if score>hiscore :
        with open("hiscore.txt" , "w") as f :
                f.write (str(score))
        return score

game()

        

        
