import asyncio


async def fetch_data(id: int, sleep_time: int) -> dict:
    print(f"Coroutine starting to fetch data....")

    await asyncio.sleep(sleep_time)
    return {"id": id, "data": f"Sample data from {id}"}

async def main() -> None:
    tasks: list = []
    async with asyncio.TaskGroup() as tg:
        for i, sleep_time in enumerate([2, 1, 3], start = 1):
            task: asyncio.Task = tg.create_task(fetch_data(i, sleep_time))
            tasks.append(task)

    results: list = [task.result() for task in tasks]

    for result in results:
        print(f"Received result: {result}")

asyncio.run(main())