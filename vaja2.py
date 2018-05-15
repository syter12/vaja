import serial
import time

def read(port,rate):
    ser = serial.Serial(port, rate, timeout=1)
    ser.close()
    ser.open()
    ser.write("wifi_conf_get".encode("ascii"))

    time.sleep(2)
    read_line = ser.readline()
    print(read_line.decode())
    ser.close()



def main():
    #port = input("Select port")
    #rate = input("select baud rate")
    read("com3","9600")

if __name__ == '__main__':
    main()
