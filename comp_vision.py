import cv2
from numpy import size
import time

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


while True:
    ret,frame = cap.read()

    (class_ids,scores,bboxes)=model.detect(frame)

    # for class_id in class_ids:
    #     name = classes[class_id]
    #     print(name)

    #time.sleep(0.3)
    for class_id,score,bbox in zip(class_ids,scores,bboxes):
        (x,y,w,h) = bbox
        print(x,y,w,h)
        name = classes[class_id]
        cv2.putText(frame,name,(x,y-5),2,cv2.FONT_HERSHEY_PLAIN,(200,0,50),2)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(200,0,50),3 )


    cv2.imshow("Frame",frame)
    cv2.waitKey(1)