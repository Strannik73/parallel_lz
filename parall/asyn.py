import asyncio
import aiohttp
import time

urls = ["https://httpbin.org/get"] * 10  # 10 одинаковых запросов для примера


# асинхронные задачи
async def async_requests():
    async with aiohttp.ClientSession() as session:
        tasks = [session.get(url) for url in urls]
        start = time.time()
        responses = await asyncio.gather(*tasks)
        return (f'выполнено{time.time() - start} сек')
    
async def interv():
    start = time.time()
    for i in range(5):
        print(f'вывод №{time.time() - start} сек')  
        await asyncio.sleep(1)
        
async def main():
    await asyncio.gather(async_requests(), interv())

asyncio.run(main())
