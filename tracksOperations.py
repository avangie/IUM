from jsonOperations import *

def joinTracksWithArtists3(artistsDictionary, tracksDictionary):
    artists_mapping = {artist['id']: artist for artist in artistsDictionary}

    result_list = []
    for track in tracksDictionary:
        artist_id = track['id_artist']
        artist = artists_mapping.get(artist_id)

        if artist:
            genre = artist['genres']
            result_item = {
                # "id_artist": artist_id,
                "popularity": track['popularity'],
                "duration_ms": track['duration_ms'],
                "explicit": track['explicit'],
                "release_date": track['release_date'],
                "danceability": track['danceability'],
                "energy": track['energy'],
                "key": track['key'],
                "mode": track['mode'],
                "loudness": track['loudness'],
                "speechiness": track['speechiness'],
                "acousticness": track['acousticness'],
                "instrumentalness": track['instrumentalness'],
                "liveness": track['liveness'],
                "valence": track['valence'],
                "tempo": track['tempo'],
                "time_signature": track['time_signature'],
                "genre": genre
            }
            result_list.append(result_item)

    writeToNewJsonFile(result_list, 'tracks_with_genre.jsonl')
