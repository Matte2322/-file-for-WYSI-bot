import pytz
import tweepy 
import datetime, time
import schedule
import random

now = datetime.datetime.now()
utc_now = now.astimezone(pytz.UTC)
print(utc_now)
# current = utc_now.strftime("%H:%M:%S")

auth = tweepy.OAuthHandler("CONSUMER_KEY", "CONSUMER_SECRET")
auth.set_access_token("KEY", "SECRET_KEY")


api = tweepy.API(auth)

# randomize responses for bot to tweet
response = [
    "HOLY SHIT, WHEN YOU SEE IT. Print out at 7:27 AM/PM",
    "WYSI, THE FUNNY NUMBER HOLY SHIT!!!",
    "727, haha funny number. So funny that I fuck...",
    "I love cookiezi and aireu so much that I love it.",
    "Futa cock."
]


# testing if my tokens work
try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")


def task():
    api.update_status(random.choice(response))
        

# converted local time to universal time 
schedule.every().day.at("23:27").do(task)
schedule.every().day.at("11:27").do(task)


while True:
    schedule.run_pending()
    time.sleep(1)  
