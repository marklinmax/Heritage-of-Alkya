import sys
import time
from tkinter import *
from threading import Thread
from multiprocessing import Queue

DEFAULT_FG = "white"
DEFAULT_BG = "black"


class Console(Thread, Tk):
    
    def __init__(self):
        self.running = True
        
        self.to_disp = Queue()
        self.to_execute = Queue()

        self.line_count = 0

        self.main = None
        self.text = None

        self.q = Queue()

        self.t = Thread(target=self.window, daemon=True)
        self.t.start()

        ##time.sleep(1)
        ##self.main.quit()
        

    def window(self):
        self.main = Tk()
        self.main.title("Console - Heritage of Alkya")

        self.text = Text(self.main, bg="black", fg="white", insertbackground="white", state=DISABLED)
        self.text.pack(side=LEFT, fill=BOTH, expand=YES)

        self.main.after(100, self.update)
            
        self.main.mainloop()
        

    def update(self, event=None):
        while self.running:
            while not self.q.empty():
                msg = self.q.get()
                if msg == "0":
                    self.main.destroy()
                    self.running = False
                elif msg.split(":")[-1:][0] == "text":
                    fg = msg.split(":")[-3:-2][0]
                    bg = msg.split(":")[-2:-1][0]
                    string = ":".join(msg.split(":")[:-3])
                    
                    start = self.text.index("end")
                    self.text.config(state=NORMAL)
                    if self.line_count != 0:
                        self.text.insert("end", "\n" + string)
                        self.line_count += 1
                    else:
                        self.text.insert("end", string)
                        self.line_count += 1

                    end = self.text.index("insert lineend")
                    
                    self.text.tag_add(string, start, end)
                    self.text.tag_config(string, background=bg, foreground=fg)

                    self.text.config(state=DISABLED)
                    self.text.update()
            try:
                self.main.update()
            except(Exception):
                self.running = False
                    

    def cprint(self, text, fg=DEFAULT_FG, bg=DEFAULT_BG):
        formated = ":".join((text, fg, bg, "text"))
        self.q.put(formated)

    def stop(self):
        self.q.put("0")
