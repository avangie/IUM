from jsonOperations import getObjectsFromJson, writeToNewJsonFile, writeToNewJsonFile2
from genresOperations import *

artists = getObjectsFromJson('artists.jsonl')

new_artists = getObjectsFromJson('artists_modified.jsonl')

number = 15
words = ['rock', 'k-pop', 'pop', 'hip hop', 'folk', 'jazz', 'country', 'reggae', 'rap', 'soul', 'punk', 'house', 'trap', 'metal', 'techno', 'indie']
dict = artists.copy()

for word in words:
    list = findGroups(dict, word)
    dict = replaceToGenres(dict, list, word)
low_occurs_genders = getEveryGenreBelowOccursNumber(dict, number)
dict = removeFromGenres(dict, low_occurs_genders)
dict = cleanGenres(dict)
popularity = findPopularity(dict)
dict = chooseOnlyOneGenre(dict, popularity)
dict = cleanArtists(dict)
writeToNewJsonFile2(dict)

# print(sorted(findPopularity(dict)))


print(len(genresToDict(new_artists)))
# print(len(getEveryGenreBelowOccursNumber(artists, 15)))