import csv
import datetime 

now = datetime.datetime.now()
nowtime=now.strftime("%A:%H:%M")
print (nowtime)




with open('timings.csv','r') as f:
    csv_reader=csv.reader(f)
    for line in csv_reader:
        
        if(nowtime==line[0]):
            meetingid=line[1]
            password=line[2]
            print(line[0])
            print("meeting ID ="+str(meetingid))
            print("password = "+str(password))
