import serial
import datetime
import time


class Serial:
    def __init__(self, port, rate):
        self.port = port
        self.rate = rate
        self.connection = serial.Serial(self.port, self.rate, timeout=1)
        self.close = self.connection.close()
        self.open = self.connection.open()


    def read(self, fraza):
        read_line = self.connection.readline()    #read line from serial
        while fraza not in read_line:  #read serial port until wanted line
            read_line = self.connection.readline()
        return read_line, datetime.datetime.today().isoformat()

    def status_get(self):
        self.connection.write("status_get\r\n")    #get status packet

    def temp_get(self):
        temp, date = self.read("PV2_EPD_TEMP_SENSOR")
        return temp.split(":").


def main():
    port = "/dev/ttyUSB0"
    rate = "115200"
    command = Serial(port, rate)
    while True:
        #temp, date = data.read(line)
        command.status_get()
        temp, date = command.temp_get()



if __name__ == '__main__':
    #main(input("Please type the command line you want: "))
    main()

