from struct import pack
import pyttsx3
import serial
import time


ser  =serial.Serial()
ser.baudrate =9600
ser.port = "COM5"
ser.open()

pre_dist=""

while True:
    if ser.in_waiting:
        packet = ser.readline()
        packet_data = packet.decode("utf")
        if (pre_dist != packet_data) and (packet_data):
            pre_dist = packet_data
            print(packet_data)


            words = "The object is "+packet_data+" meters away"
            proper_word = words.replace('\r\n', "")
        
            time.sleep(0.4)
