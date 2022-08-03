import re
import csv
import aiohttp
import asyncio
import datetime
from draw import Graph
import os

##edit below to change csv name
sampling = ['Match_addr', 'x', 'IN_City', 'score', 'IN_Address', 'IN_Postal', 'Subregion', 'y', 'Postal', 'PostalExt',
            'ResultID', 'City']

file = open('input.csv', encoding='utf8')
outside = []
current_line = ''
sample = csv.DictReader(file)
now = datetime.datetime.now()
current_directory = os.getcwd()
final_directory = os.path.join(current_directory, str(now))
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
    url = f'https://www.walkscore.com/score/{address}'
    async with session.get(url) as get:
        response = await get.text()
        try:
            walk = int(re.search(pattern=r'has a Walk Score of (\d*)', string=response).group(1))
            bike = int(re.search(pattern=r'png" alt="(\d*) Bike Score of', string=response).group(1))
            transit = int(re.search(pattern=r'png" alt="(\d*) Transit Score of', string=response).group(1))
            print(f'{address} walk: {walk} bike: {bike} transit: {transit}')
            g = Graph(walk, bike, transit, address)
            g.construct()
        except AttributeError:
            global outside
            outside.append(full)


asyncio.run(main_scrape())
os.chdir(current_directory)
with open('recheck.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, sampling)
    dict_writer.writeheader()
    dict_writer.writerows(outside)

# https://compiletoi.net/fast-scraping-in-python-with-asyncio/
