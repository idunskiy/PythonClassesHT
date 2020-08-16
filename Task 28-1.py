import random
import string
import os
from multiprocessing.pool import ThreadPool

import requests

from timer import timer

def fetch_pic(num_pic):
    url = 'https://picsum.photos/400/600'
    path = '/Users/ivan/PythonProjects/PythonClassesHT/pics'
    for _ in range(num_pic):
        random_name = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
        response = requests.get(url)
        if response.status_code == 200:
            with open(f'{path}/{random_name}.jpg', 'wb') as f:
                f.write(response.content)
                print(f"Fetched pic [{os.getpid()}]:{f.name}")

DATA_SIZE = 100
workers = 50

with timer('Elapsed: {}s'):
    with ThreadPool(workers) as pool:
        input_data = [DATA_SIZE // workers for _ in range(workers)]
        pool.map(fetch_pic, input_data)



