from instapy import InstaPy
from instapy import smart_run
import schedule
import time

my_username = 'dheirya._.mehta'
my_password = 'dheirya123456'

session = InstaPy(username = my_username,
                  password = my_password,
                  headless_browser = False)

with smart_run(session):
    session.set_relationship_bounds(enabled=True,
                                    delimit_by_numbers=True,
                                    max_followers=500,
                                    min_followers=90,
                                    min_following=200)

session.set_do_follow(True, percentage=100)

schedule.every().day.at("6:00").do(schedule.Job)
schedule.every().day.at("18:00").do(schedule.Job)

while True:
    schedule.run_pending()
    time.sleep(10)