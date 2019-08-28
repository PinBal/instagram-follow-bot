# imports

import json
import instabot
import os
import time

# define account list

accounts = []

with open('accounts.txt', 'r') as filehandle:
    accounts = [account.rstrip() for account in filehandle.readlines()]

# clear function to delete followed file

def clear():
    anya = os.path.isfile('./followed.txt')
    if(anya == False):
        print("")
    else:
        os.remove("followed.txt")
        os.remove("unfollowed.txt") 
        
# follow function        

def follow(username):
    for x in accounts:
        bot = instabot.Bot()
        uname = x.split(":")[0]
        upass = x.split(":")[1]
        bot.login(username=uname, password=upass)
        bot.follow(username)
        clear()
        bot.logout()

# unfollow function

def unfollow(username):
    for x in accounts:
        bot = instabot.Bot()
        uname = x.split(":")[0]
        upass = x.split(":")[1]
        bot.login(username=uname, password=upass)
        bot.unfollow(username)
        clear()
        bot.logout

# user "interface"

print("Accounts loaded:", len(accounts))

i69 = input("Follow / Unfollow ( 1 / 2 ) : ")

if(i69 == "1"):
    i0 = input("Instagram username : ")

    print("We send", len(accounts), "followers to", i0, "account. Correct? y/n : ")
    i2 = input("")
    if(i2 == "y"):
        follow(i0);
    else:
        quit()
else:
    i420 = input("Username to unfollow : ")
    unfollow(i420)
    
    
    


