import asyncio
import random

async def producer(condition, queue):
    for i in range(5):
        await asyncio.sleep(random.uniform(1, 3))
        item = f"item-{i}"
        async with condition:     
            queue.append(item)    
            print(f"Produced {item}")
            condition.notify()    

async def consumer(name, condition, queue):
    while True:
        async with condition:               
            while not queue:                
                await condition.wait()
            item = queue.pop(0)             
        print(f"{name} consumed {item}")
        await asyncio.sleep(2)              

async def main():
    condition = asyncio.Condition()
    queue = []

    consumers = [asyncio.create_task(consumer(f"Consumer-{i}", condition, queue)) for i in range(2)]
    producers = [asyncio.create_task(producer(condition, queue))]

    await asyncio.gather(*producers)
    await asyncio.sleep(5)  
    for c in consumers:
        c.cancel()

asyncio.run(main())
