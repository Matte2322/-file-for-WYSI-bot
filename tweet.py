import pytz
import tweepy 
import datetime, time
import schedule
import random

now = datetime.datetime.now()
utc_now = now.astimezone(pytz.UTC)
print(utc_now)

def myToken():
    auth = tweepy.OAuthHandler('CONSUMER_KEY', 'CONSUMER_SECRET')
    auth.set_access_token('KEY', 'SECRET_KEY')
    return auth


api = tweepy.API(myToken())

# randomize responses for bot to tweet
response = [
    "HOLY SHIT, WHEN YOU SEE IT. Print out at 7:27 AM/PM",
    "WYSI, THE FUNNY NUMBER HOLY SHIT!!!",
    "727, haha funny number. So funny that I fuck...",
    "I love cookiezi and aireu so much that I love it.",
    "Futa cock.",
    "WYSI",
    "Haha, when you see the unfunny number."
]


# testing if my tokens work
try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")


def task():
    api.update_status(random.choice(response))
        
def testTask():
    api.update_status("It's femboy Friday yall!")

# converted local time to universal time 
schedule.every().day.at("23:27").do(task)
schedule.every().day.at("11:27").do(task)
schedule.every().friday.at("00:00").do(testTask)


while True:
    schedule.run_pending()
    time.sleep(1)  
