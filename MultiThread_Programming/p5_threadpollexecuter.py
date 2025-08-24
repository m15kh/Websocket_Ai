from threading import Thread
import time 
from time import perf_counter
from SmartAITool.core import *
from concurrent.futures import ThreadPoolExecutor

s1 = perf_counter()

def show(name):
    cprint(f"starting thread number:{name}", 'yellow')
    time.sleep(1)
    cprint(f"finishing thread number:{name}", 'blue')
    
    
with ThreadPoolExecutor(max_workers=2) as executer:
    name = ["one", "two","three","four","five","six"]
    executer.map(show, name)

print(f"time to execusion {(perf_counter() - s1):.2f}")