import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt

# ─────────────────────────────────────────
#  STEP 1 — Load the CSV Files
# ─────────────────────────────────────────

print("=" * 50) 
print("       🏎️ F1 CLASSIFICATION MODEL") 
print("       Predicting Podium Finishes!")
print("=" * 50)

# Load results and drivers data
results = pd.read_csv('results.csv') 
drivers = pd.read_csv('drivers.csv')
races   = pd.read_csv('races.csv')

print(f"\n✅ Results loaded   : {len(results)} rows")
print(f"✅ Drivers loaded   : {len(drivers)} rows")
print(f"✅ Races loaded     : {len(races)} rows")


# ─────────────────────────────────────────
#  STEP 2 — Understand the Data
# ─────────────────────────────────────────

print("\n" + "=" * 50)
print("         📋 FIRST 5 ROWS OF RESULTS")
print("=" * 50)
print(results[['raceId', 'driverId', 'grid', 'position', 'points', 'laps']].head())

print("\n📊 Column Names in Results:")
print(list(results.columns))


# ─────────────────────────────────────────
#  STEP 3 — Clean the Data
# ─────────────────────────────────────────

# Replace \N with NaN 
results['position'] = pd.to_numeric(results['position'], errors='coerce')
results['grid']     = pd.to_numeric(results['grid'], errors='coerce')
results['points']   = pd.to_numeric(results['points'], errors='coerce')
results['laps']     = pd.to_numeric(results['laps'], errors='coerce')

# Remove rows with missing values
results = results.dropna(subset=['position', 'grid', 'points', 'laps'])

print(f"\n✅ Clean data rows  : {len(results)} rows")


# ─────────────────────────────────────────
#  STEP 4 — Podium or Not
#
#  Podium = finished in position 1, 2, or 3
#  1 = YES podium
#  0 = NO podium
# ─────────────────────────────────────────

results['podium'] = results['position'].apply(lambda x: 1 if x <= 3 else 0)

podium_count     = results['podium'].sum()
non_podium_count = len(results) - podium_count

print("\n" + "=" * 50)
print("         🏆 PODIUM BREAKDOWN")
print("=" * 50)
print(f"\n🥇 Podium finishes     : {int(podium_count)}")
print(f"❌ Non podium finishes : {int(non_podium_count)}")


# ─────────────────────────────────────────
#  STEP 5 — Features 
#
#  Features = things the model will LEARN from
#  grid     = starting position on the grid
#  points   = points scored
#  laps     = number of laps completed
# ─────────────────────────────────────────

X = results[['grid', 'laps', 'points']]  # Input features
y = results['podium']                     # Output label (1 or 0)

print("\n" + "=" * 50)
print("         🔢 FEATURES USED")
print("=" * 50)
print("\n  • grid   → Starting grid position")
print("  • laps   → Number of laps completed")
print("  • points → Points scored in the race")


# ─────────────────────────────────────────
#  STEP 6 — Split Data into Train & Test
#
#  80% → Training 
#  20% → Testing 
# ─────────────────────────────────────────

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,    # 20% for testing
    random_state=42   # Same results every time
)

print("\n" + "=" * 50)
print("         ✂️  DATA SPLIT")
print("=" * 50)
print(f"\n📚 Training rows : {len(X_train)}")
print(f"🧪 Testing rows  : {len(X_test)}")


# ─────────────────────────────────────────
#  STEP 7 — Train the Model
# ─────────────────────────────────────────

model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)  # Train the model

print("\n" + "=" * 50)
print("         🤖 MODEL TRAINED!")
print("=" * 50)


# ─────────────────────────────────────────
#  STEP 8 — Test the Model & See Results
# ─────────────────────────────────────────

y_predicted = model.predict(X_test)
accuracy    = accuracy_score(y_test, y_predicted)

print("\n" + "=" * 50)
print("         🎯 MODEL RESULTS")
print("=" * 50)
print(f"\n✅ Accuracy : {accuracy * 100:.2f}%")
print("\n📊 Detailed Report:")
print(classification_report(y_test, y_predicted, target_names=['No Podium', 'Podium']))


# ─────────────────────────────────────────
#  STEP 9 — Predict a New Driver
# ─────────────────────────────────────────

print("=" * 50)
print("     🌟 PREDICT A NEW RACE RESULT")
print("=" * 50)

# Let's predict: A driver starts from grid position 1, completes 50 laps, scores 25 points
new_driver = [[1, 50, 25]]  # grid=1, laps=50, points=25
prediction  = model.predict(new_driver)

print(f"\n🏎️  Grid Position : 1")
print(f"🔄  Laps Completed: 50")
print(f"⭐  Points        : 25")

if prediction[0] == 1:
    print("\n🏆 Prediction: YES — This driver will finish on the PODIUM! 🥇")
else:
    print("\n❌ Prediction: NO — This driver will NOT finish on the podium.")

# Another example — starting from back of grid
new_driver2 = [[18, 40, 0]]  # grid=18, laps=40, points=0
prediction2  = model.predict(new_driver2)

print(f"\n🏎️  Grid Position : 18")
print(f"🔄  Laps Completed: 40")
print(f"⭐  Points        : 0")

if prediction2[0] == 1:
    print("\n🏆 Prediction: YES — This driver will finish on the PODIUM! 🥇")
else:
    print("\n❌ Prediction: NO — This driver will NOT finish on the podium.")


