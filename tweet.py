import pytz
import tweepy 
import datetime
import schedule 
import time

now = datetime.datetime.now()

utc_now = now.astimezone(pytz.UTC)
print(utc_now)
# current_time = now.strftime("%H:%M:%S")

auth = tweepy.OAuthHandler("CONSUMER_KEY", "CONSUMER_SECRET")
auth.set_access_token("KEY", "SECRET_KEY")


api = tweepy.API(auth)

# testing if my tokens work
try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

time1 = '7:27 AM/PM'
def task():
    api.update_status(f"HOLY SHIT, WHEN YOU SEE IT. Printed out at {time1} UTC.")
        

# converted local time to universal time 
schedule.every().day.at("23:27").do(task)
schedule.every().day.at("11:27").do(task)


while True:
    schedule.run_pending()
    time.sleep(1)   





