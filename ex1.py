# In this bit of code we are using async functions and await keyword however we arent able to get the advantage of asynchronity

# This just ensures completion of one task before the execution of the next

import asyncio

async def fetching_data(delay, some_id):
    print(f'Fetching data {id}')
    await asyncio.sleep(delay)
    print(f'Data has been fetched with ID -> {id}')


async def main():
    task1 = fetching_data(2,1)
    task2 = fetching_data(2,2)

    await task1
    print("Done task-1")
    await task2
    print("Done task-2")

if __name__ == "__main__":
    asyncio.run(main())


