from  gpiozero import LED
from time import sleep
led1=LED(21)
led2=LED(16)
led3=LED(20)
led4=LED(26)
print("Program is running .... CTRL+C to quit")

def pattern1():
	print("Pattern 1 running...")
	led1.on()
	sleep(0.5)
	led1.off()
	sleep(0.5)
	
	led2.on()
	sleep(0.5)
	led2.off()
	sleep(0.5)
	
	led3.on()
	sleep(0.5)
	led3.off()
	sleep(0.5)
	
	led4.on()
	sleep(0.5)
	led4.off()
	sleep(0.5)
	
def pattern2():
	print("Pattern 2 running ....")

	led1.on()
	led2.on()
	led3.on()
	led4.on()
	sleep(1)
	led1.off()
	led2.off()
	led3.off()
	led4.off()
	sleep(1)
	

def pattern3():
	print("Pattern 3 running ....")
	for i in range(4):
		if i==1:
			for i in range(3):
			    led1.on()
			    sleep(0.1)
			    led1.off()
			    sleep(0.1)
		elif i==2:
			 for i in range(3):
			     led2.on()
			     sleep(0.1)
			     led2.off()
			     sleep(0.1)
		elif i==3:
			 for i in range(3):
			     led3.on()
			     sleep(0.1)
			     led3.off()
			     sleep(0.1)
		else:
			for i in range(3):
			    led4.on()
			    sleep(0.1)
			    led4.off()
			    sleep(0.1)							
	

def pattern4():
	print("Pattern 4 running ....")
	led1.on()
	sleep(1)
	led1.off()
	sleep(1)
	led2.on()
	sleep(1)
	led2.off()
	sleep(1)
	led3.on()
	sleep(1)
	led3.off()
	sleep(1)
	led4.on()
	sleep(1)
	led4.off()
	sleep(1)
	
while True:
	pattern1()
	for i in range(2):
		pattern2()
	pattern3()
	pattern4()

led1.off()
led2.off()
led3.off()
led4.off() 
