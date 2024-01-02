from jsonOperations import getObjectsFromJson, writeToNewJsonFile
from genresOperations import *
from tracksOperations import joinTracksWithArtists, tracksSampler

import numpy as np

# artists = getObjectsFromJson('data/artists.jsonl')
# tracks = getObjectsFromJson('data/tracks.jsonl')
# new_artists = getObjectsFromJson('data/artists_modified.jsonl')
trakcs_with_genre = getObjectsFromJson('data/tracks_with_genre.jsonl')

def firstWay(dictionary, path='data/artists_modified.jsonl'):
    dict = dictionary.copy()
    words = ['rock', 'k-pop', 'pop', 'hip hop', 'folk', 'jazz', 'country', 'reggae', 'rap', 'soul', 'punk', 'house', 'trap', 'metal', 'techno', 'indie', 'opm']
    number = 15
    for word in words:
        list = findGroups(dict, word)
        dict = replaceToGenres(dict, list, word)
    popularity = findPopularity(dict)
    dict = chooseOnlyOneGenre(dict, popularity)
    low_occurs_genders = getEveryGenreBelowOccursNumber(dict, number)
    dict = removeFromGenres(dict, low_occurs_genders)
    dict = cleanGenres(dict)
    dict = cleanArtists(dict)
    writeToNewJsonFile(dict, path)


def secondWay(dictionary, path='data/artists_modified.jsonl'):
    dict = dictionary.copy()
    popularity = findPopularity(dict)
    dict = chooseOnlyOneGenre(dict, popularity)
    words = ['rock', 'k-pop', 'pop', 'hip hop', 'folk', 'jazz', 'country', 'reggae', 'rap', 'soul', 'punk', 'house', 'trap', 'metal', 'techno', 'indie', 'opm']
    number = 15
    for word in words:
        list = findGroups(dict, word)
        dict = replaceToGenres(dict, list, word)
    low_occurs_genders = getEveryGenreBelowOccursNumber(dict, number)
    dict = removeFromGenres(dict, low_occurs_genders)
    dict = cleanGenres(dict)
    dict = cleanArtists(dict)
    writeToNewJsonFile(dict, path)


# secondWay(artists)
# new_artists_2 = getObjectsFromJson('artists_modified_2.jsonl')
# dict = genresToDict(new_artists_2)
# print(sorted(genresToDict(new_artists_2)))

# keys = list(dict.keys())
# values = list(dict.values())
# sorted_value_index = np.argsort(values)
# sorted_dict = {keys[i]: values[i] for i in sorted_value_index}
# print(sorted_dict)
# print(len(sorted_dict))

# joinTracksWithArtists3(new_artists, tracks)

writeToNewJsonFile(tracksSampler(trakcs_with_genre), 'data/sampled_tracks.jsonl')