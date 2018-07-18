import serial
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session
import requests
import datetime

PORT = "COM4"
RATE = "115200"
class Serial:
    def __init__(self, port, rate):
        self.port = port
        self.rate = rate
        self.connection = serial.Serial(self.port, self.rate, timeout=1)
        self.close = self.connection.close()
        self.open = self.connection.open()

    #send command for status packet then read lines from serial port until it hits the phrase you specifiy
    def read(self, fraza):
        self.connection.write(b"status_get\r\n")
        read_line = self.connection.readline()
        while fraza.encode() not in read_line:
            read_line = self.connection.readline()
        return read_line.decode().split(":")[1].strip()



    #get hex decimal uuid number with cli command then transform it to normal uuid style
    def get_uuid(self):
        real_uuid = ""
        counter = 0
        self.connection.write(b"uuid_get\r\n")
        read_line = self.connection.readline()
        while b"UUID" not in read_line:
            read_line = self.connection.readline()
        for a in read_line.decode().split(":")[1].split():
            real_uuid = real_uuid + a[2:]
            counter += 1
            if counter in {4, 6, 8, 10}:
                real_uuid = real_uuid + "-"
        return real_uuid

    def get_gtin(self):
        return self.read("PV2_GTIN")

    def get_firmware(self):
        major = self.read("PV2_FIRMWARE_VERSION_MAJOR")
        minor = self.connection.readline().decode().split(":")[1].strip()
        revision = self.connection.readline().decode().split(":")[1].strip()

        return major + "." + minor + "." + revision

    def get_bootloader(self):
        major = self.read("PV2_BOOTLOADER_VERSION_MAJOR")
        minor = self.connection.readline().decode().split(":")[1].strip()
        revision = self.connection.readline().decode().split(":")[1].strip()

        return major + "." + minor + "." + revision

    def get_wifi_type(self):
        return self.read("PV2_WIFI_MODULE_ID")[2:]

class Rma_api:

    def get_access_token(self):
        client_id="C30ifzyuaWQ3HLycDk1eN5meqoUi7M6YIy3eKiW6"
        client = BackendApplicationClient(client_id=client_id)
        client_secret = "gf8zNeFDb275uxN9c7Vzsyh9hq3ATgVVL0lGbziVAqAS72DHZtMEPxNrkGRpMm6ZBrEGZasep8d51TzqxPzdHtQTVZF4AsYwB24U4WCfwQpDgE3heOV5KFKnSN63ulAm"
        oauth = OAuth2Session(client=client)
        token = oauth.fetch_token(token_url="https://dt.vnct.xyz/api/token/", client_id=client_id, client_secret=client_secret)
        return token["access_token"]

    def send_rma(self,data):
        r = requests.post("https://dt.vnct.xyz/api/v1/rma/rma_detail", json=data, headers={"Authorization": "Bearer " + str(self.get_access_token)})
        print(r.status_code, r.reason)

def main():
    rma_info = {}
    user_info = {}
    device_info = []
    command = Serial(PORT, RATE)
    rma_info["device_id"] = command.get_uuid()
    device_info.extend((command.get_wifi_type(), command.get_firmware(), command.get_bootloader(), command.get_gtin()))
    rma_info["date_recieved"] = datetime.datetime.now().isoformat()
    print("Rma info. Please press enter after each prompt.\n")
    print("Reasons for return:\n15: Integration\n14: Damage-wifi\n13: Damage-screen\n12: Upgrade\n9: CC signal\n8: Battery\n7: Satisfied\n5: Costs\n4: RS module\n3: CC module")
    rma_info["return_reason"] = input("Select return reason: ")
    print("State of the RMA at this moment:\n6: Open\n7: Closed\n8: In transit\n9: At customs\n10: Arrived\n11: Testing\n12: Repair")
    rma_info["return_state"] = input("Select the state of the RMA: ")
    rma_info["id"] = input("Please enter the RMA number: ")
    user_info["customer_name"] = input("Please enter the customers name: ")
    rma_info["customer"] = input("Please enter the customers email: ")
    user_info["company_name"] = input("Please enter the customers company name: ")

    send_data = Rma_api()
    send_data.send_rma(rma_info)


if __name__ == '__main__':
    main()

