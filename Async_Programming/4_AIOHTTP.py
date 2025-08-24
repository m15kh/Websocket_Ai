import asyncio
import aiohttp


async def show_status(session, url):
    async with  session.get(url) as result:
        return result.status



async def main():
    async with aiohttp.ClientSession() as session:
        url = 'https://chatgpt.com'
        status = await asyncio.create_task(show_status(session, url))
        
        print(status)
asyncio.run(main())