import schedule
import time
import fetcher

schedule.every().day.at("07:00").do(fetcher.fetcher)

while True:
    schedule.run_pending()
    time.sleep(60) # wait one minute
