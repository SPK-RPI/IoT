import sys
from mfrc522 import SimpleMFRC522
from time import sleep
from gpiozero import Buzzer
import RPi.GPIO as GPIO
reader = SimpleMFRC522()



autorizedGreenLed=Buzzer(21)
unautorizedRedLed=Buzzer(20)
buzzer=Buzzer(16)   
def authenticationCheck(id,person):
    if (id ==735818122071 and person=='shiva'):
        print("Wellcome",person)
        buzzer.beep(0.1,0.1,4)
        
        autorizedGreenLed.beep(0.5,0.5,10)  

    
        
    else:
        print("Un-Authoried personal")
        buzzer.beep(0.5,0.5,4)
        unautorizedRedLed.beep(0.3,0.3,10)  
            
    
try:
    while True:
        print("Hold your tag near the reader")
        id, person = reader.read()
        authenticationCheck(id,person.strip())
        sleep(5)
except KeyboardInterrupt:
    autorizedGreenLed.off()
    buzzer.off()
    unautorizedRedLed.off()
    GPIO.cleanup()
    raise
