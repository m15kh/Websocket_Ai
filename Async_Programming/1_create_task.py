import asyncio
from  time import time

async def one(name):
    await asyncio.sleep(1)
    print(f"welcome to this channel {name}")


# t1 = time()
# asyncio.run(one("mohammad"))
# asyncio.run(one("liam"))
# print(f"execution is occured {time() - t1}") #NOTE #time that occured 2.0040266513824463



async def main():
    task_1 = asyncio.create_task(one("mohammad"))
    task_2 = asyncio.create_task(one("liam"))
    
    await task_1
    await task_2
    
    
t2 = time()
asyncio.run(main())
print(f"execution is occured {time() - t2}") #NOTE #execution is occured 1.001509428024292
