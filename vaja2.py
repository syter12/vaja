import serial
import time

def read(port,rate):
    ser = serial.Serial(port, rate, timeout=1)
    ser.close()
    ser.open()
    ser.write("status_get\r\n")

    read_line = ser.readline()
    print(read_line.decode())
    while("PV2_EPD_TEMP_SENSOR" not in read_line):
        read_line = ser.readline()
        if "PV2_EPD_TEMP_SENSOR" in read_line:
            print(read_line.split(":")[1])
    ser.close()



def main():
    #port = input("Select port")

    read("com3","115200")

if __name__ == '__main__':
    main()
