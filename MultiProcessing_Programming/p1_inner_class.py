import time 
from time import perf_counter
from SmartAITool.core import *
from multiprocessing import Process

s1 = perf_counter()

def show(name):
    cprint(f"starting thread number:{name}", 'yellow')
    time.sleep(1)
    cprint(f"finishing thread number:{name}", 'blue')
    
    

t1 = Process(target=show, args=("one",))
t2 = Process(target=show, args=("two",))

t1.start()
t2.start()

t1.join()
t2.join()
print(f"time to execusion {(perf_counter() - s1):.2f}")