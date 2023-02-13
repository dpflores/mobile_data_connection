import os 
import sys
import time
import urllib.request

ATTEMPTS = 5
GENERAL_ATTEMPS = 3
ATTEMPT_DELAY = 3
CONNECTION_LINK = 'http://google.com'

class Connection:
    def __init__(self, host=CONNECTION_LINK):
        self.host = host
        self.disconnects_counter = 0
        self.attempts_counter = 0
    
    def connect_link(self):
        try:
            urllib.request.urlopen(self.host)
            return True
        except:
            return False

    def mobile_attempt(self, attempts=ATTEMPTS, attempt_delay=ATTEMPT_DELAY):
        self.disconnects_counter = 0
        print("Executing ppp -c")
        os.system("ppp -c")
        time.sleep(attempt_delay)
        while self.disconnects_counter <= attempts-1:
            if self.connect_link():
                print("Connected")
                self.disconnects_counter = 0
                self.attempts_counter = 0
            
            else:
                self.disconnects_counter += 1
                print(f'Disconnected, {self.disconnects_counter} attempt')
            time.sleep(attempt_delay)

    def go(self,attempts=GENERAL_ATTEMPS):
        self.attempts_counter = 0

        while self.attempts_counter <= attempts-1:
            self.mobile_attempt()
            self.attempts_counter += 1
            print(f"{self.attempts_counter} FAIL")

        print("not connecting, rebooting")
        os.system("reboot")
    

    
    
def main():
    mobile_data_connection = Connection()
    mobile_data_connection.go()

    
    
    


if __name__ == '__main__':
    try:
        main()

    except:
        sys.exit(1)


