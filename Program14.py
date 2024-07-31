import time
if (int(time.strftime('%H'))>=0 and int(time.strftime('%H'))<6):
    print("Good Night Sir, time is", time.strftime('%H:%M:%S'))
elif(int(time.strftime('%H'))>=6 and int(time.strftime('%H'))<12):
    print("Good Morning Sir, time is", time.strftime('%H:%M:%S'))
elif(int(time.strftime('%H'))>=12 and int(time.strftime('%H'))<18):
    print("Good Afternoon Sir, time is", time.strftime('%H:%M:%S'))
else:
    print("Good Evening Sir,time is", time.strftime('%H:%M:%S'))