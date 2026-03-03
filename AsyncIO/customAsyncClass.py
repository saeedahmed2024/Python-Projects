import asyncio
import time
import requests

class CustomAwaitable:
    def __await__(self):
        yield from asyncio.sleep(2).__await__()  # Delegate to asyncio
        return "Custom Awaitable Done"

#
async def function1():
    URL = "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.freepik.com%2Ffree-photos\
    -vectors%2F4k&psig=AOvVaw2fZH2VgolgIsteSyntjc3N&ust=1751274692597000&source=\
    images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCMii7-Oklo4DFQAAAAAdAAAAABAE"
    response = requests.get(URL)
    open("image1.jpeg", "wb").write(response.content)
    print("function 1")

    return "Saeed"

async def function2():
    URL = "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.freepik.com%2Ffree-photos\
    -vectors%2F4k&psig=AOvVaw2fZH2VgolgIsteSyntjc3N&ust=1751274692597000&source=\
    images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCMii7-Oklo4DFQAAAAAdAAAAABAE"
    response = requests.get(URL)
    open("image2.jpeg", "wb").write(response.content)
    print("function 2")

    return 1

async def function3():
    URL = "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.freepik.com%2Ffree-photos\
    -vectors%2F4k&psig=AOvVaw2fZH2VgolgIsteSyntjc3N&ust=1751274692597000&source=\
    images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCMii7-Oklo4DFQAAAAAdAAAAABAE"
    response = requests.get(URL)
    open("image3.jpeg", "wb").write(response.content)
    print("function 3")

    return 2


async def main():
    start_time = time.time()
    # result = await CustomAwaitable()
    # print(result)
    result = await asyncio.gather(
        function1(),
        function2(),
        function3()
    )
    print(result)
    elapsed_time = time.time() - start_time
    print(f"Time elapsed: {elapsed_time}")

asyncio.run(main())