import asyncio
from  time import time

async def one(name):
    await asyncio.sleep(1)
    print(f"welcome to this channel {name}")



async def main():
    
    task1 = asyncio.create_task(one("sara"))
    task2 = asyncio.create_task(one("parya"))
    
    await task1
    await task2
    

# t1 = time()
# asyncio.run(main())
# print(f"time for runnign code{time() - t1}")
    

t2 = time()
loop = asyncio.new_event_loop()
try:
    loop.run_until_complete(main())
    
finally:
    loop.close()
print(f"time for runnign code{time() - t2}")
    
    