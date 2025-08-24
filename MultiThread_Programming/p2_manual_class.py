from threading import Thread
import time 
from time import perf_counter
from SmartAITool.core import *

s1 = perf_counter()

def show(name, delay):
    cprint(f"starting thread number:{name}", 'yellow')
    time.sleep(delay)
    cprint(f"finishing thread number:{name}", 'blue')
    
    
class ShowThread(Thread):
    def __init__(self, name, delay):        
        super().__init__()
        self.delay = delay
        self.name = name
    
    def run(self):
        show(self.name, self.delay)

t1 = ShowThread('one', 4)
 
t2 = ShowThread('two', 4)
t1.start()
t2.start()
t1.join()
t2.join()

print(f"time to execusion {(perf_counter() - s1):.2f}")