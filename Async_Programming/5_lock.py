import asyncio


counter = 0



async def increment_counter(lock):
    global counter
    async with lock: #BUG if we dont use lock each task overlap together becasue of sleep muthod !
        temp_counter = counter
        temp_counter += 1
        await asyncio.sleep(0.01)
        counter = temp_counter

async def main():
    global counter
    lock = asyncio.Lock()
    tasks =  [asyncio.create_task(increment_counter(lock)) for _ in range(100)]
    
    await asyncio.gather(*tasks)
    print(f"counter is =={counter}")
    
    
asyncio.run(main())