from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from jsonOperations import *

data = getObjectsFromJson('data/tracks_with_genre.jsonl')

# Przygotowanie danych
features = []
labels = []

for song in data:
    features.append([song["popularity"], song["duration_ms"], song["explicit"], song["danceability"], song["energy"], song["key"], song["loudness"], song["speechiness"], song["acousticness"], song["instrumentalness"], song["liveness"], song["valence"], song["tempo"], song["time_signature"]])
    labels.append(song["genre"][0])

# Podział danych na zbiór treningowy i testowy
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

# Normalizacja danych
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Wytrenowanie modelu k-najbliższych sąsiadów
knn_classifier = KNeighborsClassifier(n_neighbors=3)
knn_classifier.fit(X_train, y_train)

# Przewidywanie gatunku dla danych testowych
y_pred = knn_classifier.predict(X_test)

# Ocena dokładności modelu
accuracy = accuracy_score(y_test, y_pred)
print(f"Dokładność modelu: {accuracy}")

# Przykład przewidywania gatunku dla nowej piosenki
new_song = [45, 260000, 0, 0.6, 0.7, 3, -6, 0.1, 0.2, 0.0, 0.3, 0.8, 120, 4]
new_song = scaler.transform([new_song])
predicted_genre = knn_classifier.predict(new_song)
print(f"Przewidziany gatunek dla nowej piosenki: {predicted_genre[0]}")