from time import sleep
from gpiozero import LED 
from pyfingerprint.pyfingerprint import PyFingerprint


## Search for a finger
##
authorizedLed=LED(21)
unAuthorisedLed=LED(20)
index=0x01
## Tries to initialize the sensor
try:
    f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)

    if ( f.verifyPassword() == False ):
        raise ValueError('The given fingerprint sensor password is wrong!')

except Exception as e:
    print('The fingerprint sensor could not be initialized!')
    print('Exception message: ' + str(e))
    exit(1)

## Gets some sensor information
print('Currently used templates: ' + str(f.getTemplateCount()) +'/'+ str(f.getStorageCapacity()))
def readFingurePrint(ind):
    print('Waiting for finger...')

    ## Wait that finger is read
    while ( f.readImage() == False ):
        pass

    ## Converts read image to characteristics and stores it in charbuffer 1
    f.convertImage(ind)

    ## Searchs template
    result = f.searchTemplate()
    
    positionNumber = result[0]
    return positionNumber

## Tries to search the finger and calculate hash
try:
    positionNumber=readFingurePrint(index)
    
    if ( positionNumber == -1 ):
        print('No match found!')
        unAuthorisedLed.blink(on_time=0.2,off_time=0.2)
        sleep(10)
        unAuthorisedLed.off()
        
       
        
        
        
        
    else:
        authorizedLed.blink(on_time=0.6,off_time=0.6)
        print('Found template at position #' + str(positionNumber))
        
        sleep(10)

except Exception as e:
    print('Operation failed!')
    print('Exception message: ' + str(e))
    exit(1)