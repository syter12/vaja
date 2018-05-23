import serial
import datetime
import time

def read(port,rate):
    print datetime.datetime.today().isoformat()
    ser = serial.Serial(port, rate, timeout=1)
    ser.close()
    ser.open()
    ser.write("status_get\r\n")

    read_line = ser.readline()
    print(read_line.decode())
    while("PV2_EPD_TEMP_SENSOR" not in read_line):
        read_line = ser.readline()
        if "PV2_EPD_TEMP_SENSOR" in read_line:
            temp = read_line.split(":")[1]
            print("Temperature at {1} was {0} degrees celsius".format(temp.strip(), datetime.datetime.today().isoformat()))
            return(temp.strip(),datetime.datetime.today().isoformat())
    ser.close()




def main():
    #port = input("Select port")
    zbirka = []
    a = 0

    while True:
        temp, date = read("/dev/ttyUSB0","115200")
        time.sleep(5)
        zbirka.append(temp +","+ date)
        a+=1
        if a > 10:
            break
    print zbirka

if __name__ == '__main__':
    main()
