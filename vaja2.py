import serial
import datetime
import time

class Beri():
    def __init__(self, port, rate):
        self.port = port
        self.rate = rate

    def read(self, fraza):
        ser = serial.Serial(self.port, self.rate, timeout=1)  #initiate serial port
        ser.open()
        read_line = ser.readline()    #read line from serial
        print(read_line.decode())
        while(fraza not in read_line):  #read serial port until wanted line
            read_line = ser.readline()
        data = read_line.split(":")[1]
        print("Temperature at {1} was {0} degrees celsius".format(data.strip(), datetime.datetime.today().isoformat()))
        ser.close()
        return(data.strip(),datetime.datetime.today().isoformat())

    def write(self):
        ser = serial.Serial(self.port, self.rate, timeout=1)
        ser.close()     #close serial port first
        ser.open()
        ser.write("status_get\r\n")    #get status packet


def main():
    port = "/dev/ttyUSB0"
    rate = "115200"
    zbirka = []
    a = 0
    command = Beri(port, rate)
    data = Beri(port, rate)
    command.write()
    while True:
        #temp, date = data.read(line)
        temp, date = data.read("PV2_EPD_TEMP_SENSOR")

        time.sleep(5)
        zbirka.append(temp + "," + date)
        a += 1
        if a > 10:
            break
    print(zbirka)


if __name__ == '__main__':
    #main(input("Please type the command line you want: "))
    main()

