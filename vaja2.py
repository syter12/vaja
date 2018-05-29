import serial
import datetime
import time

class Beri():
    def read(port,rate):
        ser = serial.Serial(port, rate, timeout=1)  #initiate serial port
        ser.open()
        read_line = ser.readline()    #read line from serial
        print(read_line.decode())
        while("PV2_EPD_TEMP_SENSOR" not in read_line):  #read serial port until wanted line
            read_line = ser.readline()

<<<<<<< HEAD
        temp = read_line.split(":")[1]
        print("Temperature at {1} was {0} degrees celsius".format(temp.strip(), datetime.datetime.today().isoformat()))
        ser.close()
        return(temp.strip(),datetime.datetime.today().isoformat())  
    def write(port,rate):
        ser = serial.Serial(port, rate, timeout=1)
        ser.close()
        ser.open()
        ser.write("status_get\r\n")    #get status packet




def main():
    port = "/dev/ttyUSB0"
    rate="115200"
    zbirka = []
    a = 0
    Beri.write(port,rate)
    while True:
        temp, date = Beri.read(port,rate)
=======
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
>>>>>>> 62fac8f91f635aafb8677020c336c91a8a987aa4
        time.sleep(5)
        zbirka.append(temp +","+ date)
        a+=1
        if a > 10:
            break
<<<<<<< HEAD
    print(zbirka)
=======
    print zbirka
>>>>>>> 62fac8f91f635aafb8677020c336c91a8a987aa4

if __name__ == '__main__':
    main()
