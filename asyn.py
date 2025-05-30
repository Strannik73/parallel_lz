import asyncio
import aiohttp
import time
from threading import Timer

urls = ["https://httpbin.org/get"] * 10  # 10 одинаковых запросов для примера


# функция асинхронные задачи
async def async_requests():
    async with aiohttp.ClientSession() as session:
        tasks = []
        start = time.time()
        for url in urls:
            tasks.append(session.get(url))
        responses = await asyncio.gather(*tasks)
        return time.time() - start
    
def interv(interval, iterations):
    interval: 1
    iterations: 5
    for i in range(iterations):
        time.sleep(interval)
        break
# def repeater(interval, function):
#     Timer(interval, repeater, [interval, function]).start()
#     function()

# def my_task():
#     print("Задача выполнена")

# repeater(1, my_task)
# break
# Запуск
print(f"Асинхронные запросы: {asyncio.run(async_requests()):.2f} сек")
