from time import sleep
import ast
import thingspeak
from gpiozero import LED
import json
channel_id = 792696
write_key = "6ANVTQF7AUFEMMH2"

lightsPin = LED(21)
fanPins = LED(20)


def doit(channel):
    try:
        lights = ast.literal_eval(channel.get_field_last(field="field1"))
        l = lights["field1"]
        print("Lights=>>", l)
        fans = ast.literal_eval(channel.get_field_last(field="field2"))
        f = fans['field2']
        print("Fans =>>", f)
        if l == "on":
            lightsPin.on()
        else:
            lightsPin.off()
        if f == "on":
            fanPins.on()
        else:
            fanPins.off()

    except:
        print("Failed to get")


if __name__ == "__main__":
    channel = thingspeak.Channel(channel_id, write_key)

    while True:

        doit(channel)
        
        
        
        sleep(1)
        
