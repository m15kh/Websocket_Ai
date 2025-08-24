import asyncio


async def show(smp):
    # await smp.acquire()
    async with smp:
        print(" ---- showing results ----")
        await asyncio.sleep(1)
    # smp.release()
        
    
async def main():
    smp = asyncio.Semaphore(2)
    await asyncio.gather(*[show(smp)for _ in range (10)])
    
asyncio.run(main())


