from datetime import datetime
from aiohttp import ClientSession
import asyncio
async def trans_and_time(session: ClientSession,address):

    params = {
        'to': f'{address}',
        'ps': '100',
        'p': '1',
        'type': 'json',
    }
    try:
        async with session.get(f'https://voyager.online/api/txns',params=params) as response_time:
            response_time_json = await response_time.json()
            time = response_time_json['items']
            data = time[0]['timestamp']
            trans = len(time)
            return datetime.fromtimestamp(data).strftime('%Y-%m-%d'), trans
    except Exception as e:
        print('Фейл')
        return 0,0
async def balance(session: ClientSession, address):

    try:
        async with session.get(f'https://voyager.online/api/contract/{address}/balances') as response_balance:
            response_balance_json =await response_balance.json()
            balance = 0
            for i in response_balance_json:
                balance += float(i['usdFormattedBalance'][1:])

            return balance
    except Exception as e:
        print('Фейл')
        return 0
async def cheker(session: ClientSession, address):

    balances, time = await asyncio.gather(balance(session, address=address),trans_and_time(session, address=address))
    return f'{time[1]}:{balances}:{time[0]}'
async def main():

    addresses = []
    with open('wallet.txt', 'r') as file:
        for line in file:
            addresses.append(line.strip())
    async with ClientSession() as session:
        tasks = [cheker(session, address) for address in addresses]
        results = await asyncio.gather(*tasks)
        with open('output.txt', 'w') as file:
            file.write('')
        for i in range(len(addresses)):
            with open('output.txt', 'a') as file:
                data = f'{addresses[i]}:{results[i]}'
                file.write(data + '\n')
        return results

asyncio.run(main())
