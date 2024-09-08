# using an asyn task-group which makes sure that if one of the tasks fails, then the entire program stops 

import asyncio

async def fetch_data(info_id, delay):
    print(f"fetching data for info number {info_id}")
    await asyncio.sleep(delay)
    return {"data_fetched":f"id number {info_id}"}

async def main():
    tasks=[]
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(fetch_data(1,2))
        task2 = tg.create_task(fetch_data(2,2))
        tasks.append(task1)
        tasks.append(task2)
    
    # task group already awaits the function so we can directly print the result

    for task in tasks:
        print(task.result())

asyncio.run(main())
