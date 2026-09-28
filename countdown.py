from time import sleep
def countDown(time):
    if time==0 or time < 0:
       print("Countdown over !")
       return 0
    print(f"Time remaining {time}")
    sleep(1)
    return countDown(time-1)

countDown(60)