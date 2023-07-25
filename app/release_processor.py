from bs4 import BeautifulSoup
from .classes.album import Album

likes = ['Doom', 'Atmospheric', 'Black', 'Melodic', 'Sludge', 'Stoner']
dislikes = ['Thrash', 'Grindcore', 'Technical', 'Raw', 'Brutal', 'Groove', 'Djent', 'Progressive', 'Folk', 'Power']

final_list = {
    'fo_sho': [],
    'maybe': [],
    'nah': []
}


def process_list(albums):
    for release in albums:
        obj = list_to_album(release)
        if release[2] == 'Demo' or release[2] == 'Single':
            continue
        elif in_list(obj.genre, dislikes):
            final_list['nah'].append(obj)
        elif in_list(obj.genre, likes):
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
    print(album.formatted_output())


def list_to_album(album_release):
    name_raw = BeautifulSoup(album_release[0], 'html.parser')
    album_raw = BeautifulSoup(album_release[1], 'html.parser')

    return Album(name_raw.text, name_raw.find("a").get("href"), album_raw.text, album_raw.find("a").get("href"),
                 album_release[3], album_release[4])


def in_list(genre, preferences):
    contains_genre = False
    for preference in preferences:
        if contains_genre:
            break
        contains_genre = preference in genre
    return contains_genre
