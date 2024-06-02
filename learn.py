import time



def timer(hours,minutes,seconds):
    totalTime = hours*3600 + minutes*60 +seconds

    while totalTime:
        hours, remainder = divmod(totalTime, 3600)
        minutes, seconds = divmod(remainder, 60)

        timer = '{:02d}:{:02d}:{:02d}'.format(hours, minutes,seconds)

        print (timer, end='\r')
        time.sleep(1)

        totalTime -=1
    print('Timer Completed')



timer(0,1,15)