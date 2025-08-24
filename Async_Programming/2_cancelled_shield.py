import asyncio
from asyncio.exceptions import CancelledError, TimeoutError


async def one():
    await asyncio.sleep(6)
    print("Hello to all Guys")
    
    
#NOTE manual timeout
# async def main():
#     task_1 = asyncio.create_task(one())
    
    
#     sec = 0 
#     while not task_1.done():
#         print("task not finished yet ..;")
#         await asyncio.sleep(1)
#         sec += 1
#         if sec == 5:
     
#             task_1.cancel()
    
#     try :
#         await task_1
        
#     except CancelledError as e:
        
#         print(f"task doesnt works due \n{e}")
        

#NOTE cancel task     
# async def main():
    
#     task1 = asyncio.create_task(one())
    
#     try:
#         await asyncio.wait_for(task1, timeout=5)
        
#     except TimeoutError:
#         print("timeout error ")
        
#     print(f"was that task cancelled?:{task1.cancelled()}")
            
            
#NOTE sheild task

async def main():
    
    task1 = asyncio.create_task(one())
    
    try:
        await asyncio.wait_for(asyncio.shield(task1), timeout=5)
        
    except TimeoutError:
        print("task takes time as usual")
        await task1
        
        
        
        
            
asyncio.run(main())
            


