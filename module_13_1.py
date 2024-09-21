import asyncio


async def start_strongman(name, power):
    balls = 5
    print(f'Силач {name} начал соревнования.')
    for i in range(1, 6):
        await asyncio.sleep(1 / power)
        print(f'Силач {name} поднял {i}')

    print(f'Силач {name} закончил соревнования.')


async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Иван', 2))
    task2 = asyncio.create_task(start_strongman('Алексей', 1.5))
    task3 = asyncio.create_task(start_strongman('Михаил', 3))

    await task1
    await task2
    await task3

asyncio.run(start_tournament())