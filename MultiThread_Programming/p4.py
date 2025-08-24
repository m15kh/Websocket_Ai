from threading import Thread, current_thread , enumerate
import time 
from time import perf_counter
from SmartAITool.core import *

s1 = perf_counter()

def show(name):
    cprint(f"starting thread number:{name}", 'yellow')
    cprint(current_thread())
    cprint(enumerate(), 'white')
    time.sleep(1)
    cprint(f"finishing thread number:{name}", 'blue')
    
    

t1 = Thread(target=show, args=("one",))
t2 = Thread(target=show, args=("two",))

t1.start()
t2.start()

t1.join()
t2.join()
print(f"time to execusion {(perf_counter() - s1):.2f}")