# In this piece of code we will be using semaphores to allow process to to run async-ly in groups rather than all at once

import asyncio

async def access_resource(semaphore, resource_id):
    async with semaphore:
        print(f"accessing resource {resource_id}")
        await asyncio.sleep(1)
        print(f"releasing resource id -> {resource_id}")


async def main():
    semaphore = asyncio.Semaphore(2) # Allowing concurrent processes in groups of 2
    await asyncio.gather(*(access_resource(semaphore, i)for i in range(5)))

asyncio.run(main())
