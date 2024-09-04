# In this bit of code we are running the coroutines async-ly by creating tasks and then awaiting them resulting in the whole op taking only 2 sec in stead of 6. 

import asyncio 

async def fetching_data(no, delay):
    print(f"Coroutine fetching data {no} ...")
    await asyncio.sleep(delay)
    return {"id": id, "data": f"Sample data number {no} has been collected"}

async def main():

    # creating coroutines:

    task1 = asyncio.create_task(fetching_data(1,2))
    task2 = asyncio.create_task(fetching_data(2,2))
    task3 = asyncio.create_task(fetching_data(3,2))

    result1 = await task1
    result2 = await task2
    result3 = await task3

    print(result1, result2, result3)

if __name__ == "__main__":
    asyncio.run(main())
