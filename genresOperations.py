def removeFromGenres(dictionary, list):
    for artist in dictionary:
        for genre in artist['genres']:
            if genre in list:
                artist['genres'].remove(genre)
    return dictionary

def replaceToGenres(dictionary, list, word):
    for artist in dictionary:
        for genre in artist['genres']:
            if genre in list:
                index = artist['genres'].index(genre)
                artist['genres'][index] = word
    return dictionary

def checkUnique(dictionary):
    for artist in dictionary:
        if len(artist['genres']) != 1:
            return False
    return True

def findGroups(dict, word):
    group = []
    for artist in dict:
        for genre in artist['genres']:
            if (genre.find(f' {word}') != -1 or genre.find(f'{word} ') != -1) and genre not in group:
                group.append(genre)
    return group

def genresToDict(dictionary):
    genresDictionary = {}
    for artist in dictionary:
        for genre in artist['genres']:
            if genre in genresDictionary:
                genresDictionary[genre] += 1
            else:
                genresDictionary[genre] = 1
    return genresDictionary

def chooseOnlyOneGenre(dictionary, popularity):
    for artist in dictionary:
        if len(artist['genres']) != 1:
            artist['genres'] = chooseMostPopular(artist['genres'], popularity)
    return dictionary

def chooseMostPopular(list, popularity):
    most_popular = None
    most_popular_occurs = -1
    for genre in list:
        num_occurs = popularity[genre]
        if num_occurs > most_popular_occurs:
            most_popular = genre
            most_popular_occurs = num_occurs
    return [most_popular]

def findPopularity(dictionary):
    genres = {}
    for artist in dictionary:
        for genre in artist['genres']:
            if genre in genres:
                genres[genre] += 1
            else:
                genres[genre] = 1
    return genres

def getEveryGenreBelowOccursNumber(dictionary, number):
    genres = []
    popularity = findPopularity(dictionary)
    for genre in popularity:
        if popularity[genre] <= number:
            genres.append(genre)
    return genres

def getGenreOccursNumber(dictionary, genre):
    popularity = findPopularity(dictionary)
    return popularity[genre]

def cleanGenres(dictionary):
    genres = []
    for artist in dictionary:
        for genre in artist['genres']:
            if genre not in genres:
                genres.append(genre)
        artist['genres'] = genres.copy()
        genres = []
    return dictionary

def cleanArtists(dictionary):
    return [artist for artist in dictionary if artist['genres']]
