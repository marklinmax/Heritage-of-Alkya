import os
import datetime
from termcolor import colored, cprint
from threading import Thread
from multiprocessing import Queue

if os.name == "nt":
    import colorama

class Logger:

    def __init__(self, log_abs_path):

        if os.name == "nt":
            colorama.init()

        self.running = True

        self.abs_path = log_abs_path

        self.to_log = Queue()
        self.to_write = Queue()

        self.file = None
        self.openFile()

        self.threads = []

        self.threads.append(Thread(target=self.writer, args=(self.to_write,), daemon=True).start())
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
        while self.running:
            while not q.empty():
                print(q.get())
        
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

    def log(self, text, msgtype="default"):
        if not self.running:
            print("The logger is stopped and can't log anymore.")
        else:
            try:
                format_text = "[{}] {}".format(self.getDate(), text)
                if msgtype == "error":
                    self.to_log.put(colored("<ERROR> " + format_text, "red"))
                    self.to_write.put("<ERROR> " + format_text)
                elif msgtype == "info":
                    self.to_log.put(colored("<INFO> " + format_text, "cyan"))
                    self.to_write.put("<INFO> " + format_text)
                elif msgtype == "warning":
                    self.to_log.put(colored("<WARNING> " + format_text, "yellow"))
                    self.to_write.put("<WARNING> " + format_text)
                else:
                    self.to_log.put(format_text)
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
        self.closeFile()
        if os.name == "nt":
            colorama.deinit()

    def __del__(self):
        try:
            while not self.to_write.empty():
                pass
            
            while not self.to_log.empty():
                pass

            self.running = False
            self.closeFile()
            if os.name == "nt":
                colorama.deinit()
        except(Exception):
            pass
