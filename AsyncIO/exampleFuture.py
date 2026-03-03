import asyncio

async def example_future():
    future = asyncio.Future()  # Create a Future object
    print(f"Initial state: {future.done()}")  # False (Pending)

    # Simulate computation
    await asyncio.sleep(2)

    future.set_result("Task Completed")  # Mark future as done
    print(f"Final state: {future.done()}")  # True (Done)
    print(f"Result: {future.result()}")  # "Task Completed"

asyncio.run(example_future()) # Error, will see it indepth in next topic

#await example_future() # Directly await the coroutine instead of calling asyncio.run