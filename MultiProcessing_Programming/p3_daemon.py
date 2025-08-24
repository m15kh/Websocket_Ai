from multiprocessing import Process
import time 
from time import perf_counter
from SmartAITool.core import *
import sys
s1 = perf_counter()

def show(name):
    cprint(f"starting thread number:{name}", 'yellow')
    time.sleep(1)
    cprint(f"finishing thread number:{name}", 'blue')
    
    

t1 = Process(target=show, args=("one",), daemon= True)
t2 = Process(target=show, args=("two",), daemon= True)

t1.start()
t2.start()


print(f"time to execusion {(perf_counter() - s1):.2f}")
sys.exit()