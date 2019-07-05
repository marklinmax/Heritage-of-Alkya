import os
import datetime
from lib import console
from threading import Thread
from multiprocessing import Queue

class Logger:

    def __init__(self, log_abs_path, con=None, cons_enabled=True):


        if con == None and cons_enabled == True:
            self.cons = console.Console()
        else:
            self.cons = console

        self.cons_enabled = cons_enabled

        self.running = True

        self.abs_path = log_abs_path

        self.to_log = Queue()
        self.to_write = Queue()

        self.file = None
        self.openFile()

        self.threads = []

        self.threads.append(Thread(target=self.writer, args=(self.to_write,), daemon=True).start())

        if self.cons_enabled == True:
            self.threads.append(Thread(target=self.printer, args=(self.to_log,), daemon=True).start())
        


    def getDate(self):
        return str(datetime.datetime.today()).split(".")[0]

    def writer(self, q):
        while self.file != None and self.running:
            while not q.empty():
                try:
                    self.file.write(q.get() + "\n")
                except(Exception):
                    pass

    def printer(self, q):
        while self.cons_enabled:
            while not q.empty():
                msg = q.get()
                if len(msg) == 2:
                    self.cons.cprint(msg[0], msg[1])
                else:
                    self.cons.cprint(msg[0])
        self.cons.stop()
        
    def openFile(self):
        try:
            date = self.getDate().replace(":","-").replace(" ", "_")
            os.chdir(self.abs_path)
            
            ok = True
            x = 1
            name = "{}.txt".format(date)
            while ok == True:
                if name in os.listdir():
                    x += 1
                    name = "{}-{}.txt".format(date, x)
                else:
                    ok = False
            
            self.file = open(name, "w")
        except(Exception) as error:
            print("Logger failed to open the log file.")
            print(error)

    def closeFile(self):
        try:
            self.file.close()
            self.file = None
        except(Exception) as error:
            print("Logger failed to close the log file.")
            print(error)

    def garbageCollect(self):
        for t in self.threads:
            if not t.isAlive():
                del t

    def openConsole(self, console=None):
        if self.cons == None and self.cons_enabled == False:
            if console == None:
                self.cons = console.Console()
            else:
                self.cons = console
            self.garbageCollect()
            self.threads.append(Thread(target=self.printer, args=(self.to_log,), daemon=True).start())
            self.cons_enabled = True
        else:
            self.log("A console is already runnig.")

    def closeConsole(self):
        if self.cons != None and self.cons_enabled == True:
            self.cons_enabled = False
        else:
            self.log("There is no console to close.")
            
            

    def log(self, text, msgtype="default"):
        if not self.running:
            print("The logger is stopped and can't log anymore.")
        else:
            try:
                format_text = "[{}] {}".format(self.getDate(), text)
                if msgtype == "error":
                    if self.cons_enabled:
                        self.to_log.put(("<ERROR> " + format_text, "red"))
                    self.to_write.put("<ERROR> " + format_text)
                elif msgtype == "info":
                    if self.cons_enabled:
                        self.to_log.put(("<INFO> " + format_text, "cyan"))
                    self.to_write.put("<INFO> " + format_text)
                elif msgtype == "warning":
                    if self.cons_enabled:
                        self.to_log.put(("<WARNING> " + format_text, "yellow"))
                    self.to_write.put("<WARNING> " + format_text)
                else:
                    if self.cons_enabled:
                        self.to_log.put((format_text,)) ##It is a TUPLE !
                    self.to_write.put(format_text)
            except(Exception) as error:
                print("Logger failed to log the message.")
                print(error)

    def stop(self):
        while not self.to_write.empty():
            pass
        
        while not self.to_log.empty():
            pass

        self.running = False
        self.closeConsole()
        self.closeFile()

    def __del__(self):
        try:
            while not self.to_write.empty():
                pass
            
            while not self.to_log.empty():
                pass

            self.running = False
            self.closeConsole()
            self.closeFile()
            
        except(Exception):
            pass
