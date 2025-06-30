import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report 
import joblib
from feature_extraction import prepare_features

# Load dataset
df = pd.read_csv("malicious_url_data.csv")

# Label encoding: 0 = benign, 1 = malicious
df['label'] = df['type'].apply(lambda x: 0 if x == 'benign' else 1)

# Feature extraction
print("🔍 Extracting features...")
X = prepare_features(df)
y = df['label']

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
print("🧠 Training Random Forest model...")
model = RandomForestClassifier(n_estimators=100, random_state=42,class_weight='balanced')

model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
print("\n📊 Classification Report:\n")
print(classification_report(y_test, y_pred))

# Save model and columns
joblib.dump(model, "model.pkl")
joblib.dump(X.columns.tolist(), "feature_columns.pkl")

print("\n✅ Model saved as 'model.pkl'")
print("✅ Feature columns saved as 'feature_columns.pkl'")

