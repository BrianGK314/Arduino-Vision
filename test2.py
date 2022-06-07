from socket import timeout
import serial
import time

ser = serial.Serial("COM5",9600,timeout=1)

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
    data = str(rd())
    # if data != "b''":
    #     cleaned_data = ret_num(data)
    #     print(cleaned_data)
    print(data)
#        time.sleep(0.4)



# ls = ["b'1182\\r\\n'", "b'118\\r\\n'", "b'11\\r\\n'", "b'1\\r\\n'"]

# for i in ls:
#     if len(i) ==8:
#         print(i[2:3])

#     elif len(i) ==9:
#         print(i[2:4])

#     elif len(i) ==10:
#         print(i[2:5])

#     elif len(i) ==11:
#         print(i[2:6])
