import asyncio
import inspect
import time

async def my_function():
  #time.sleep(2)
  #time.sleep(2)
  await asyncio.sleep(4)
  print("Hello! from my_function()")

async def fetch(delay: int, id: int):
    print(f"Coroutine id {id} started fetching data...")
    await asyncio.sleep(delay)
    print("Data fetched, id:", id)
    return {"data": "some data", "id":id}

async def main():
    task2= asyncio.create_task(fetch(2, 1))
    task1 = asyncio.create_task(fetch(1, 3))
    task3 = asyncio.create_task(fetch(3, 2))

    #start_time = time.time()
    # result1 = await task1
    # result2 = await task2
    # result3 = await task3
    # results = (result1, result2, result3)

    results = await asyncio.gather(task1, task2, task3)
    for result in results:
        print(f"Result: {result}")
    # print(results)
    # print(f"Time elapsed: {time.time() - start_time}")

asyncio.run(main())
# is_awaitable = inspect.isawaitable(my_function())
# print(f"Is awaitable: {is_awaitable}")

