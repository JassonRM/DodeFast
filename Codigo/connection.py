import serial

class Connection:
    def __init__(self, port):
        self.port = port
        self.arduino = serial.Serial(port, 9600, timeout=None)

    def ping(self, led):
        data = "LED" + str(led)
        self.arduino.write(str.encode(data))

    def listen(self):
        led = 1
        while True:
            entrada = str(self.arduino.readline())
            print(entrada)
            self.ping(led)
            if(led == 1):
                led = 2
                print("2")
            else:
                led = 1
                print("1")