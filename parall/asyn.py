import asyncio
import aiohttp
import time

urls = ["https://httpbin.org/get"] * 10  

class asyn_c:
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
        pr = await asyncio.gather(asyn_c.async_requests(), asyn_c.interv())
        pr.async_requests()
        pr.interv()
        
    def __del__(self):
        print('удаление')
        
    if __name__ == "__main__":
        asyncio.run(main())    


