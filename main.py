from jsonOperations import getObjectsFromJson
from languageChecker import checkLanguage

artists = getObjectsFromJson('artists2.jsonl')

def filterGenres(artists, func=checkLanguage):
    for artist in artists:
        filteredLanguages = []
        for genre in artist['genres']:
            language = func(genre)
            if language == 'EN':
                filteredLanguages.append(genre)
            else:
                pass
        artist['genres'] = filteredLanguages
    return artists

def genresToDict(artists):
    genresDictionary = {}
    for artist in artists:
        for genre in artist['genres']:
            if genre in genresDictionary:
                genresDictionary[genre] += 1
            else:
                genresDictionary[genre] = 1
    return genresDictionary

def filteringFunction(pair):
    key, value = pair
    return value < 10

def sortedFunction(pair1, pair2):
    _, value1 = pair1
    _, value2 = pair2
    return value1 - value2

dictionary = genresToDict(artists)
print(dictionary.items())
# print(dict(sorted(dictionary.items())))
# print(len(dictionary))
# print(dict(filter(filteringFunction, dictionary.items())))