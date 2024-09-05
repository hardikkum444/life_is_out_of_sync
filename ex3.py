# explaining the usage of the gather function

import asyncio

async def get_info(info_id, delay):
    print(f"coroutined {info_id} is running ...")
    await asyncio.sleep(delay)
    return {"id":info_id, "data":"This is some random data"}

async def main():
    
    # This is running coroutines concurrently instead of making individual tasks
    results = await asyncio.gather(get_info(1,2), get_info(2,2), get_info(3,2))

    for result in results:
        print(f"This is the recieved result -> {result}")

if __name__ == "__main__":
    asyncio.run(main())

