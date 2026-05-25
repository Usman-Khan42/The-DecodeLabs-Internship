from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ----------------------------
# Sports Dataset 
# ----------------------------
sports = {
    "Football": "team outdoor running ball competition fitness endurance",
    "Basketball": "team indoor outdoor running jumping ball fitness",
    "Cricket": "bat ball team outdoor strategy endurance focus",
    "Tennis": "racket individual outdoor indoor agility speed focus",
    "Badminton": "racket indoor agility speed reaction fitness",
    "Swimming": "water solo fitness endurance full body strength",
    "Cycling": "outdoor endurance speed cardio fitness racing",
    "Running": "solo outdoor endurance cardio fitness speed stamina",
    "Gym Workout": "indoor fitness strength bodybuilding weights health",
    "MMA": "combat fighting martial arts boxing wrestling jiu jitsu strength endurance self defense"
}

# ----------------------------
# Prepare ML model
# ----------------------------
sport_names = list(sports.keys())
descriptions = list(sports.values())

vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(descriptions)

# ----------------------------
# Show options to user
# ----------------------------
print("🏅 Available Sports Categories:\n")

for i, sport in enumerate(sport_names, 1):
    print(f"{i}. {sport}")

print("\n👉 Type numbers OR keywords like: team, fitness, combat, outdoor\n")

# ----------------------------
# User Input
# ----------------------------
user_input = input("Enter your interests: ").lower()

# Convert numbers to sport keywords (optional smart feature)
if user_input.isdigit():
    idx = int(user_input) - 1
    if 0 <= idx < len(sport_names):
        user_input = sports[sport_names[idx]]

# ----------------------------
# ML Processing
# ----------------------------
user_vector = vectorizer.transform([user_input])
similarities = cosine_similarity(user_vector, tfidf_matrix)[0]

# ----------------------------
# Ranking
# ----------------------------
ranked_sports = sorted(
    zip(sport_names, similarities),
    key=lambda x: x[1],
    reverse=True
)

# ----------------------------
# Output
# ----------------------------
print("\n🏆 Recommended Sports for You:\n")

found = False

for sport, score in ranked_sports:
    if score > 0:
        print(f"👉 {sport} (match score: {score:.2f})")
        found = True

if not found:
    print("No strong match found. Try keywords like: fitness, team, combat, outdoor")