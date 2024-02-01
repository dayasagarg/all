from datetime import datetime,timedelta
global timing

def timing(currTimeStr,prevTimeStr):
    # global currTimeStr, prevTimeStr
    currTime = datetime.now()
    currTimeStr = datetime.strftime(currTime, "%Y-%m-%d")

    prevTime = currTime - timedelta(days=4)
    prevTimeStr = datetime.strftime(prevTime, "%Y-%m-%d")
    return currTimeStr, prevTimeStr