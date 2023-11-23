from jsonOperations import getObjectsFromJson
from languageChecker import checkLanguage

artists = getObjectsFromJson('/Users/pawko/IUM_23Z/ium_23z/artists2.jsonl')

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
    return value <= 1

dictionary = genresToDict(artists)

# Sorts values from least to most common
print(dict(sorted(dictionary.items(), key=lambda item: item[1])))

# Filter values depending on given function
print(len(dict(filter(filteringFunction, dictionary.items()))))