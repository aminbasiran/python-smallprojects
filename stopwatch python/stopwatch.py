# import schedule
import time

milisecond = 0
second = 0
minute = 0
placesecond = ""
intrval = 0.1



def startwatch():
    
    global milisecond, second, minute, placesecond
    # interface = f"{minute}:{second}:{milisecond}"
    milisecond = milisecond + 1
    if (milisecond <= 9):
        print(f"0{minute}:0{second}:0{milisecond}")
    if (milisecond > 9):
        print(f"0{minute}:0{second}:{milisecond}")
    if (milisecond > 15):
        milisecond  = 0
        second = second + 1
        print(f"0{minute}:0{second}:00")
        if (second > 9):
            print(f"0{minute}:{second}:0{milisecond}")
            # if( second > 9):
            #     print(f"0{minute}:{second}:0{milisecond}")


starttime = time.time()
while True:
    startwatch()
    time.sleep(intrval - ((time.time() - starttime) % intrval))