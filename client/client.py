import aiohttp
import asyncio
import datetime


async def uri_getter(queue, session):
    while True:
        uri = await queue.get()

        async with session.get(uri) as response:
            fuu = await response.text()

        queue.task_done()


async def main(*, worker_count, times, url):
    queue = asyncio.Queue()

    async with aiohttp.ClientSession() as session:

        workers = []
        for i in range(worker_count):
            workers.append(
                asyncio.create_task(
                    uri_getter(queue, session)
                )
            )

        for i in range(times):
            queue.put_nowait(url)

        await queue.join()

        for worker in workers:
            worker.cancel()

        await asyncio.gather(*workers, return_exceptions=True)


def client(*, worker_count, times, url):
    now = datetime.datetime.now()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(
        worker_count=worker_count,
        times=times,
        url=url
    ))
    end = datetime.datetime.now()
    total_time = end - now
    print(f'Total time: {total_time}')
