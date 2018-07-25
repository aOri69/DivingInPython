"""Запуск нескольких корутин"""
import asyncio


async def sleep_task(num):
    for i in range(5):
        print(f"process task:{num} iteration: {i}")
        await asyncio.sleep(1)


if __name__ == "__main__":
    # ensure_future or create_task
    loop = asyncio.get_event_loop()

    task_list = [loop.create_task(sleep_task(i)) for i in range(10)]
    loop.run_until_complete(asyncio.wait(task_list))

    loop.run_until_complete(loop.create_task(sleep_task(3)))
    loop.run_until_complete(asyncio.gather(sleep_task(10), sleep_task(2)))
