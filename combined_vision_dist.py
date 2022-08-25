import cv2
from numpy import size
import time
from struct import pack
import pyttsx3
import serial

### COMPUTER VISION
# #neural net
net =cv2.dnn.readNet("dnn_model\dnn_model\yolov4-tiny.weights","dnn_model\dnn_model\yolov4-tiny.cfg")
model = cv2.dnn_DetectionModel(net)
model.setInputParams(size=(320,320),scale=1/255)

#Initialize and get input from cam
cap =cv2.VideoCapture(0)

classes=[]
with open("dnn_model\dnn_model\classes.txt","r") as labels:
    for label in labels.readlines():
        classes.append(label.strip())
print(classes)


### Arduino -Python Interface
eng = pyttsx3.init()


# ser  =serial.Serial()
# ser.baudrate =9600
# ser.port = "COM5"
# ser.open()

ser = serial.Serial("COM5",9600,timeout=1)


pre_dist=""
current_name=""

def rd():

    data = ser.readline()
    return data

def ret_num(i):
    if len(i) ==8:
        return i[2:3]

    elif len(i) ==9:
        return i[2:4]

    elif len(i) ==10:
        return i[2:5]

    elif len(i) ==11:
        return i[2:6]


while True:
    ### COMPUTER VISION II

    ret,frame = cap.read()

    (class_ids,scores,bboxes)=model.detect(frame)

    for class_id in class_ids:

        name = classes[class_id]
        if current_name != name:
            current_name =name
        print(current_name)

    time.sleep(0.3)

###########
# Synchronisation issue:
###########
# Current model: at least 12 seconds can pass before accurate readings
# of distance are transmitted to the computer:

    data = str(rd())
    if data != "b''":
        cleaned_data = ret_num(data)
        print(cleaned_data)


        words = "The "+ current_name+ " is "+cleaned_data+" centimeters away"
        #proper_word = words.replace('\r\n', "")

        
        eng.say(words)

        eng.runAndWait()  

        cv2.waitKey(1)

#Solutions:
#increase delay time
#Match delay time on py code to match that of arduino BT transmission
