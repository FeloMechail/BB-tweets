import tweepy
import webbrowser
import time
import datetime as dt
from time import sleep

t = dt.datetime.now()
minute_count = 0 

print("pick a number to choose your console to follow")
print("1. Ps5")
print("2. xbox")
print("3. Both")

choose = input("Console: ")
if choose == "1":
    key = ['#playstation5','ps5','playstation5','playstation','playstation 5']
    key2 = ['stock','available','back'] 
elif choose == '3': 
    key = ['#XboxSeriesX','xboxseriesx','xbox','#playstation5','ps5','playstation5','playstation','playstation 5']
    key2 = ['stock','available','back']
else: 
    key = ['#XboxSeriesX','xboxseriesx','xbox']
    key2 = ['stock','available','back']

auth = tweepy.OAuthHandler("HANDLER HERE", "HANDLER HERE")
auth.set_access_token("ACCESS HERE", "ACCESS HERE")

api = tweepy.API(auth) 

loop = True
print("started")
while loop == True:
    time.sleep(1)
    tweets = api.user_timeline("BBYC_Gamers", count = 1, include_rts = False, tweet_mode = 'extended')
    for info in tweets:
        delta = dt.datetime.now()-t
        if delta.seconds >= 180:
            print(info.full_text)
            # Update 't' variable to new time
            t = dt.datetime.now()
        tweet = info.full_text.split(" ")
        for words in tweet:
            for x in key:
                if words.lower() == x:
                    for words in tweet:
                        for y in key2:
                            if words.lower() == y:
                                print(f"Tweet:{info.full_text}\n")
                                loop = False
                    
                                    
                     
webbrowser.open("https://www.bestbuy.ca/en-ca/basket")
#TO ADD A WEBPAGE
#webbrowser.open("add your webpage here")
 