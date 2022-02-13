import socket
from states import States
from time import sleep
from threading import Thread
from os import system, name


class Killswitch(Thread):
    def __init__(self):
        super().__init__()
        self.state = States.KILLING

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.connect(("8.8.8.8", 80))

    def run(self):
        while 1:

            if self.state == States.KILLING:
                self.sock.send(b"\x05" * killSize)

            elif self.state == States.PAUSED:
                sleep(0.1)


def main():
    switches = []
    for i in range(1):
        switches.append(Killswitch())

    for switch in switches:
        switch.start()

    while 1:
        for switch in switches:
            switch.state = States.PAUSED

        print("pause")
        system("cls" if name == "nt" else "clear")
        sleep(10)
        system("cls" if name == "nt" else "clear")
        print("kill")

        for switch in switches:
            switch.state = States.KILLING
        sleep(10)


if __name__ == "__main__":
    pauseDelay = float(input("Pause delay in FLOAT, e.g. 1.23 (seconds to wait after every kill): "))
    killDuration = float(input("Kill duration in FLOAT, e.g. 1.23 (seconds the kill will be performed): "))
    killSize = int(input("Kill size (bytes per packet, default 40000): "))
    main()