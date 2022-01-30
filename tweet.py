import tweepy 
import datetime
import schedule 
import time

# utc_now = datetime.datetime.utcnow()
now = datetime.datetime.now()
current_time = now.strftime("%H:%M:%S")

auth = tweepy.OAuthHandler("tkYxTnmNaTTTM1yM2lDsJusPd", "z3wqYmJDvt0mFLF1jz3O2yMpuGDmlRjNXe3JktXShRWuftP5Vk")
auth.set_access_token("1487688914420723712-y4rUPzLPTv38bRvKQgygrt14gVga1K", "hm2COJnZ6zazz7Wv4l5jGlB8ly51I3rMaK8upxBKyXzKn")


api = tweepy.API(auth)

# testing if my tokens work
try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")


def task():
    api.update_status(f"HOLY SHIT, WHEN YOU SEE IT. Printed out at {current_time} UTC.")

schedule.every().day.at("07:27").do(task)
schedule.every().day.at("19:27").do(task)

while True:
    schedule.run_pending()
    time.sleep(1)







