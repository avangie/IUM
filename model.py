from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.metrics import accuracy_score, classification_report
from jsonOperations import *

# Przykładowe dane w formie listy słowników
data = getObjectsFromJson('data/sampled_tracks.jsonl')

# Podział danych na cechy (X) i zmienną celu (y)
X = []
y = []
for entry in data:
    features = [entry[key] for key in entry if key not in ["popularity", "release_date", "mode", "genre"]]
    X.append(features)
    y.append(entry["genre"][0])

# Podział danych na zbiór treningowy i testowy
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.05, random_state=42)

# Utworzenie modelu SVM
model = make_pipeline(StandardScaler(), SVC(kernel='linear', C=1))

# Trenowanie modelu
model.fit(X_train, y_train)

# Ocena modelu na zbiorze testowym
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")
print("Classification Report:")
print(classification_report(y_test, y_pred))
