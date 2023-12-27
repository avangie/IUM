from jsonOperations import getObjectsFromJson, writeToNewJsonFile, writeToNewJsonFile2
from genresOperations import *

artists = getObjectsFromJson('artists.jsonl')

new_artists = getObjectsFromJson('artists_modified.jsonl')

number = 15
words = ['rock', 'k-pop', 'pop', 'hip hop', 'folk', 'jazz', 'country', 'reggae', 'rap', 'soul', 'punk', 'house', 'trap', 'metal', 'techno', 'indie', 'opm']
dict = artists.copy()

for word in words:
    list = findGroups(dict, word)
    dict = replaceToGenres(dict, list, word)

popularity = findPopularity(dict)
dict = chooseOnlyOneGenre(dict, popularity)
low_occurs_genders = getEveryGenreBelowOccursNumber(dict, number)
dict = removeFromGenres(dict, low_occurs_genders)
dict = cleanGenres(dict)
dict = cleanArtists(dict)
writeToNewJsonFile2(dict)


print(len(genresToDict(new_artists)))
print(genresToDict(new_artists))