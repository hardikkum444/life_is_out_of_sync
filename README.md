# life_is_out_of_sync
## asyncio

An async function defined using the async keyword (ofcourse), is a function in programming which helps to perform asynchronous programming (ofcourse). It is defined using the async keyword before the function definition. (ofcourse). Async functions in general return a promise which ensures the completion (which could be success or faliure) of the operation.

### pip install asyncio
### pip install aiohttp

```python 

import aiohttp
import asyncio

async def fetch_data():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://www.somerandomwebsite.com/data') as response:
            # waiting for the response
            data = await response.json()
            return data

# Running the async function
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    data = loop.run_until_complete(fetch_data())
    print(data)
```

### Taking advantage of the async function functionality

```python 

import aiohttp
import asyncio

async def fetch_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            return data

async def main():
    urls = [
        'https://api.example.com/data1',
        'https://api.example.com/data2',
        'https://api.example.com/data3'
    ]
    
    # Create a list of tasks for concurrent execution
    tasks = [fetch_data(url) for url in urls]
    
    # Await the completion of all tasks
    results = await asyncio.gather(*tasks)
    return results

# Running the async function
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    data = loop.run_until_complete(main())
    print(data)

```


# Differences Between Async Programming and Multithreading

| Feature                | Async Programming                          | Multithreading                          |
|------------------------|-------------------------------------------|-----------------------------------------|
| **Execution Model**    | Single-threaded event loop                | Multiple threads running concurrently   |
| **Overhead**           | Lower overhead, lightweight                | Higher overhead due to context switching |
| **Use Cases**          | Best for I/O-bound tasks (e.g., network requests) | Best for CPU-bound tasks (e.g., heavy computations) |
| **Complexity**         | Simpler to reason about, avoids callback hell | More complex due to synchronization issues |
| **Control Flow**       | Uses `async` and `await` for non-blocking execution | Threads run independently, can lead to race conditions |
| **Resource Management**| Efficient resource usage, can handle many tasks with fewer resources | Requires careful management of shared resources |
| **Error Handling**     | Errors can be caught using try/catch in async functions | Requires careful handling to avoid crashes due to thread issues |


