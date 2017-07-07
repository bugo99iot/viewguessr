#this is the basic algorithm for the online game viewguessr
#here below we import a dictionaty/list of 5 youtube urls + number of views from youtube_urls

from random import randint, choice
import math
import time, threading
import csv
import itertools

class style:
    BOLD = '\033[1m'
    END = '\033[0m'
    RED = '\033[91m'


def tot_points(guess, views):
    points = 0
    percent = 0.0
    base = 0.0
    #"base" accounts for the fact that guessing small numbers is harder than guessing large numbers
    #IMPRO: find a polynomial fit (ax^2+bx+c/dx^2+ex+f) with horizontal asynstote b = 10 for large v + right features close to v = 100
    base = 10 + 7*math.log10(1000000000000000/views)
    argument = 0.0
    if base > 60.0:
        base = 60.0
    elif base < 20.0:
        base = 20.0
    argument = guess/views
    percent = (1.0 - abs(math.log(argument,base)))
    if percent < 0:
        percent = 0
    points = int(round(1000*(percent)))
    return points


def main():
        
    #IMPRO: import ONLY 5 lines at random
    data_urls = []
    data_views = []
    with open('urls.txt') as textfile:
        urlsTXT = csv.reader(textfile, delimiter=',')
        for row in urlsTXT:
            data_urls.append(row[0])
            data_views.append(row[1])

    urls = dict(zip(data_urls,data_views))
        
    print
    print "Welcome to ViewGuessr!"
    #time.sleep(2)
    print "In what follows, we are going to show you a few random videos from the Youtube."
    #time.sleep(2)
    print "Your job is to guess how many views each video has made."
    #time.sleep(2)
    print "ENJOY!"
    print
    print
    #time.sleep(2)


    #start for loop here (5 videos)
    #check that videos are not repeated when randomly chosen
    score = 0
    total_score = 0
    i = 0
    while i < 5:
        current_video = choice(urls.keys())
        #IMPRO: play video for 30 seconds, if user clicks video interrupts
        print "Here is a video:", current_video, ", copy-paste it onto your browser and watch it!"
        #time.sleep(1)
        print "How many views you think it has made? This is a beta version, don't cheat!"
        #time.sleep(1)
        #guess = float(input("Your guess: "))
        guess = 0
        while True:
            try:
                guess = float(input("Your guess: "))   
                while guess < 0:
                    print "Sorry, you must enter a", style.BOLD + "positive" + style.END, "whole number."    
                    guess = float(input("Your guess: "))
            except NameError:
                print "Sorry, you must enter a whole number between zero and infinity." 
                continue
            except SyntaxError:
                print "Sorry, you must enter a whole number between 0 and infinity."
                continue
            else:
                break 
        #while type(guess) != int: 
        #    print "Sorry, you must enter a whole number between 0 and infinity."
        #    guess = input("Your guess: ")
        views = float(urls[str(current_video)])
        score = tot_points(guess, views)
        print "POINTS: ", style.BOLD + str(score) + style.END
        if tot_points(guess, views) == 1000:
            print "Hey, this is the perfect score in ViewGuessr, well done!"
        #IMPRO: print numbers in comma format (100000000 -> 100,000,000)
        print "The actual number of views was: ", int(views)
        #check total score
        total_score += score
        time.sleep(2)
        i += 1
        print

    print "Your total score is: ", style.BOLD + style.RED + str(total_score) + style.END
    #IMPRO: state how the user classifies
    print
    print "Well done!"
    print

    #save results to a ranking
    #IMPRO: add click buttons
    print "Would you like to store your results?"
    yes_no = raw_input("Yes or no? ")
    yes_no = yes_no.lower()
    if yes_no == "y" or yes_no == "yes":
        username = raw_input("What's your name? ")
        #IMPRO: add click buttons
        saveFile = open("ranking.txt", "a")
        saveFile.write(str(total_score) + "," + username + "\n")
        saveFile.close()
    #IMPRO: show ranking
    #IMPRO: WANNA PLAY AGAIN?
    print
    #IMPRO:make email address
    print "Would like to share your own videos with ViewGuessr? Write to us!"
    
if __name__ == "__main__":
    main()
