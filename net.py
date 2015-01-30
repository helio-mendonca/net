#!/usr/bin/python

import time #sleep
import sys #exit
import signal #signal
import myServer

def signal_handler(signal, frame):
    app.exit()

class App():
    def main(self):
        print("net sample")
        signal.signal(signal.SIGINT, signal_handler)
            
        self.server = myServer.myServer()   
        self.server.onMsg = self.onMsg

        while True:
            time.sleep(.1)
    
    def onMsg(self, cmd):
        if cmd[0:3] == "log":
            self.server.log = True if cmd[3:4] == "1" else False       
        if cmd[0] == "v":
            version = "net v1.0"
            print(version)
            self.server.send(version)       
        
    def exit(self):
        print("\rYou pressed Ctrl+C!")
        self.server.exit()
        sys.exit(0)
        
if __name__ == '__main__':
    app = App()
    app.main()