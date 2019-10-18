from time import sleep
from  serial import Serial
import string
import pynmea2
import webbrowser


port = "/dev/ttyS0"
ser = Serial(port, baudrate = 9600)
longitude_list=[]
latitude_list=[]
run=True
def longitude_average(longitudes):
    return sum(longitudes)/len(longitudes)

def latitude_average(latitudes):
    return sum(latitudes)/len(latitudes)

while run:
         try:
           data=ser.readline()
           if(data[0:6]=='$GPGGA'):
                    msg=pynmea2.parse(data)
                    lon=float(msg.lon)/100
                    longitude_list.append(lon)
                    lat=float(msg.lat)/100
                    latitude_list.append(lat)

                    strings="Lat: "+str(lat)+"  Lon: "+str(lon)
                    print(strings)
                  
         except:
            averagedLog=longitude_average(longitude_list)
            averagedLat=latitude_average(latitude_list)
            print("Averaged Logitude: "+str(averagedLog)+" ""Averaged Latitude: "+str(averagedLat))
            webbrowser.open("https://www.latlong.net/c/?lat="+str(averagedLat)+"&long="+str(averagedLog))
            run=False
             
     