import requests
from app import url, release_processor

headers = {'Accept': 'application/json, text/javascript',
           'Connection': 'keep-alive',
           'Accept-Language': 'en-US,en;q=0.5',
           'Accept-Encoding': 'gzip, deflate, br',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0'}


def find_metal():
    r = requests.get(url=url.today(), headers=headers)
    data = r.json()

    if data['aaData'] is not None:
        release_processor.process_list(data['aaData'])
    else:
        raise Exception("Data not found")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    find_metal()
