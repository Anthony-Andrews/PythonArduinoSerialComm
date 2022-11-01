from pynput.keyboard import Key, Listener
from serial import Serial
import serial  
import time
arduino = serial.Serial('COM8', 115200) # Arduino on COM8 baud rate 115200

pos = 100

def on_press(key):

    global pos
    
    if key == Key.up:       # if key up is being pressed, pos + 10, convert to str, then write to serial port
        pos += 10
        pos_str = str(pos)
        arduino.write(str.encode(pos_str))
        readpos = str(arduino.readline())       # read received value from arduino and print
        print (readpos)
    if key == Key.down:
        pos -= 10
        pos_str = str(pos)
        arduino.write(str.encode(pos_str))
        readpos = str(arduino.readline())
        print (readpos)

# Collect events until released
with Listener(on_press=on_press) as listener:
    listener.join()