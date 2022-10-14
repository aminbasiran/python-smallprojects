# import schedule
import time

milisecond = 0
second = 0
minute = 0
placesecond = "0"
# placeholder = "0" + str(minute) + ":" + "0" +str(second) + ":" + "0" + placemili



# placeholder = "00:00:00"
# placeholder = str(minute)+ ":" + str(second) + ":" + str(milisecond)


def startwatch():
    
    global milisecond, second, minute,placesecond
    milisecond = milisecond + 1
    if (milisecond <= 9):
        placemili = str(milisecond)
        print("00:0"+placesecond+":0"+placemili)
    if (milisecond > 9):
        placemili = str(milisecond)
        print("00:0"+placesecond+":"+placemili)
    if (milisecond > 99):
        milisecond  = 0
        second = second + 1
        placesecond = str(second)
        placemili = str(milisecond)
        print("00:0"+placesecond+":0"+placemili)
    

    
starttime = time.time()
while True:
    startwatch()
    time.sleep(0.01 - ((time.time() - starttime) % 0.01))