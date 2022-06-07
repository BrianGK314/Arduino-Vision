import serial
import time
from collections import Counter
import numpy as np

#ser = serial.Serial("COM5",9600,timeout=5)

def rdl():
    data= ser.readline(10)
    return data

# while True:
#     print(rdl())
#     time.sleep(0.3)

dist = []
for i in range(100):
    dist.append(i)
    if len(dist) > 4:
        dist = dist[1:]
    time.sleep(0.2)
    print(dist)
    print(np.mean(dist))