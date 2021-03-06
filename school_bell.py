from playsound import playsound
import time

timetable = {(8,0):1,(9,0):1,(10,0):1,(11,0):1,(12,0):1,(13,0):1,(14,0):1,(15,0):1,(16,0):1,(17,0):1,(18,0):1,(19,0):1,(20,0):1,(21,0):1,(22,0):1}
#timetable = {(8,0):1,(9,0):1,(10,0):1,(11,0):1,(12,0):1,(13,0):1,(14,0):1,(15,0):1,(16,0):1,(17,0):1,(18,0):1,(19,0):1,
#            (20,0):1,(21,0):1,(22,0):1,(23,0):1, (23,50):1}
def ring():
    print("ring",time.localtime().tm_hour, time.localtime().tm_min, time.localtime().tm_sec)
    playsound('school_bell.mp3')
 
def itemcheck(_time):
    if _time[0] == time.localtime().tm_hour and _time[1] == time.localtime().tm_min:
        ring()
        timetable[_time] = 0
    #before
    elif _time[0] > time.localtime().tm_hour or ( _time[0] == time.localtime().tm_hour and _time[1] > time.localtime().tm_min ): #before ring
        gaptime = (_time[0]-time.localtime().tm_hour)*60+ (_time[1] - time.localtime().tm_min)
        while(gaptime > 1):
            gaptime=(_time[0]-time.localtime().tm_hour)*60+ (_time[1] - time.localtime().tm_min)
            sleeptime = min(6, gaptime)-1
            time.sleep(sleeptime*60) #if computer sleep
        time.sleep(60-time.localtime().tm_sec)
        ring()
        timetable[_time] = 0
    #after
    elif timetable[_time] :
        timetable[_time] = 0

print("start",time.localtime().tm_hour, time.localtime().tm_min)
for _time in sorted (timetable.keys()) :
        #print(_time[0], _time[1])
    itemcheck(_time)
print("end")
