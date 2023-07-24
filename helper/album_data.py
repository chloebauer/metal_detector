# 0	'<a href="https://www.metal-archives.com/bands/Formless_Oedon/3540464417">Formless Oedon</a>'
# 1	'<a href="https://www.metal-archives.com/albums/Formless_Oedon/Streams_of_Rot/1122782">Streams of Rot</a>'
# 2	"Full-length"
# 3	"Death Metal"
# 4	"July 24th, 2023"
# 5	"2023-03-13 21:43:44"
import json
from bs4 import BeautifulSoup

likes = ['Doom', 'Atmospheric', 'Black', 'Melodic', 'Sludge', 'Stoner']
dislikes = ['Thrash', 'Grindcore', 'Technical', 'Raw', 'Brutal', 'Groove', 'Djent', 'Progressive', 'Folk', 'Power']

final_list = {
    'fo_sho': [],
    'maybe': [],
    'nah': []
}


def process_list(albums):
    for album in albums:
        obj = list_to_obj(album)
        if album[2] == 'Demo' or album[2] == 'Single':
            continue
        elif in_list(obj['genre'], dislikes):
            final_list['nah'].append(obj)
        elif in_list(obj['genre'], likes):
            final_list['fo_sho'].append(obj)
        else:
            final_list['maybe'].append(obj)
    readable_list()


def readable_list():
    print("-----Will Most Likely Like-----")
    for album in final_list['fo_sho']:
        format_album(album)
        print("----------")
    print("-----Might Be Something Good-----")
    for album in final_list['maybe']:
        format_album(album)


def format_album(album):
    print('{} by {}\nGenre: {}\nRelease Date: {}'.format(album['album_name'], album['band_name'],
                                                         album['genre'], album['release_date']))


def list_to_obj(album_release):
    name_raw = BeautifulSoup(album_release[0], 'html.parser')
    album_raw = BeautifulSoup(album_release[1], 'html.parser')

    return {
        'band_name': name_raw.text,
        'band_url': name_raw.find("a").get("href"),
        'album_name': album_raw.text,
        'album_url': album_raw.find("a").get("href"),
        'genre': album_release[3],
        'release_date': album_release[4]
    }


def in_list(genre, list):
    contains_genre = False
    for item in list:
        if contains_genre:
            break
        contains_genre = item in genre
    return contains_genre