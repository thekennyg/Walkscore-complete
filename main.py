import re
import csv
import aiohttp
import asyncio
import datetime
from datetime import datetime
from draw import Graph
import os
import platform


# edit below to change csv name
file = open('input.csv', encoding='utf8')
outside = []
completed = []
current_line = ''
sample = csv.DictReader(file)
sampling = sample.fieldnames
hard_sampling = list(sampling)
hard_sampling.append('walk')
hard_sampling.append('bike')
hard_sampling.append('transit')
now = datetime.now()
modified = now.strftime('%B %d %Hh%Mm%Ss%p')
current_directory = os.getcwd()
final_directory = os.path.join(os.sep, current_directory + os.sep, str(modified))
os.mkdir(final_directory)
os.chdir(final_directory)

async def main_scrape():
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
        tasks = []
        for line in sample:
            # edit below to change csv column name
            addy = line['Match_addr']
            future = asyncio.ensure_future(get_scores(session, addy, line))
            tasks.append(future)
        await asyncio.gather(*tasks)


async def get_scores(session, address, full):
    global outside
    global completed
    bully = full
    url = f'https://www.walkscore.com/score/{address}'
    try:
        async with session.get(url) as get:
            response = await get.text()
            try:
                walk = int(re.search(pattern=r'has a Walk Score of (\d*)', string=response).group(1))
            except:
                walk = 0
            try:
                bike = int(re.search(pattern=r'png" alt="(\d*) Bike Score of', string=response).group(1))
            except:
                bike = 0
            try:
                transit = int(re.search(pattern=r'png" alt="(\d*) Transit Score of', string=response).group(1))
            except:
                transit = 0
            print(f'{address} walk: {walk} bike: {bike} transit: {transit}')
            g = Graph(walk, bike, transit, address)
            g.construct()
            if walk == 0 and bike == 0 and transit == 0:
                outside.append(full)
            else:
                bully['walk'] = walk
                bully['bike'] = bike
                bully['transit'] = transit
                completed.append(bully)
    except aiohttp.ServerDisconnectedError:
        outside.append(full)


try:
    asyncio.run(main_scrape())
except asyncio.exceptions.TimeoutError:
    pass
with open(f'{now}.csv', 'w', newline='') as completed_scores:
    dict_writer = csv.DictWriter(completed_scores, hard_sampling)
    dict_writer.writeheader()
    dict_writer.writerows(completed)
os.chdir(current_directory)
with open('recheck.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, sampling)
    dict_writer.writeheader()
    dict_writer.writerows(outside)

# https://compiletoi.net/fast-scraping-in-python-with-asyncio/
