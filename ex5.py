# using locks and global shared resources in python asyncio

import asyncio

shared_resource = 0

lock = asyncio.Lock()

async def modify_shared_resource():
    global shared_resource
    async with lock:
        # This is here is the critial section

        print(f"Global resource before modification -> {shared_resource}")
        shared_resource +=1
        await asyncio.sleep(1)
        print(f"Resource after modification: {shared_resource}")
        
        # This is the end of critical section

async def main():
    for _ in range(5):
        await asyncio.gather(modify_shared_resource())

asyncio.run(main())

# It is important to note here that even after making this function async, it will execute one by one due to the presence of a lock which gaurds and allows the processign of only one function until the lock gets released
