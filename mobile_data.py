"""
Este programa se asegura que exista la conexión con los datos móviles, 
(se asume que la configuración ya fue realizada con el APN). Este verifica
5 veces la conexión a internet (probar solo con chip). Si no se recibe respuesta esas 
5 veces, entonces se reinicial la interfaz enviando un comando AT. Si aún así esto no funciona,
y esto se repite por 3 veces, entonces el sistema se reinicia. Esto supone que el chip no funciona o
que ya no dispone de conexión a internet.


"""

import os 
import sys
import time
import urllib.request

ATTEMPTS = 5
GENERAL_ATTEMPS = 5
SETUP_DELAY = 60  # el mínimo es aprox 30 segundos luego de ejecutar el comando AT, asi que 1 minuto esta bien
ATTEMPT_DELAY = 5   # no es necesario que sea amplio (tener en cuenta que s emultiplicara xATTEMPTS para comprobar conexion)
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

    def mobile_attempt(self, attempts=ATTEMPTS, attempt_delay=ATTEMPT_DELAY, setup_delay=SETUP_DELAY):
        self.disconnects_counter = 0
        time.sleep(setup_delay)
        os.system("echo mydebug: Executing ppp -c") #print
        os.system("ppp -c")
        time.sleep(attempt_delay)
        os.system("route add default dev ppp0") # se asume que se crea la interfaz ppp0
        time.sleep(attempt_delay)
        while self.disconnects_counter <= attempts-1:
            if self.connect_link():
                os.system("echo mydebug: Connected") #print
                self.disconnects_counter = 0
                self.attempts_counter = 0
            
            else:
                self.disconnects_counter += 1
                os.system(f' echo mydebug: Disconnected, {self.disconnects_counter} attempt') #print

            time.sleep(attempt_delay)

        os.system("atcom --port /dev/ttyUSB2 --baudrate 115200 AT+CRESET") # Restart interface sending the AT command

    def go(self,attempts=GENERAL_ATTEMPS):
        self.attempts_counter = 0

        while self.attempts_counter <= attempts - 1:
            self.mobile_attempt()
            self.attempts_counter += 1
            os.system(f"echo mydebug: {self.attempts_counter} ATTEMPT FAIL")

        os.system("echo mydebug: not connecting, rebooting") #print
        os.system("reboot")
    

    
    
def main():
    mobile_data_connection = Connection()
    mobile_data_connection.go()

    
    
    


if __name__ == '__main__':
    try:
        main()

    except:
        sys.exit(1)


