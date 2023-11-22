from jsonOperations import getObjectsFromJson
from languageChecker import checkLanguage

artists = getObjectsFromJson()

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

print(filterGenres(artists))