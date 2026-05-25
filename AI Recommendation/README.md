# 🏅 Sports Recommendation System 
---

## 📌 What This Project Does

This program takes your interests as input (like `"team fitness outdoor"`) and uses **machine learning text similarity** to find the sports that match you best. It ranks all sports by how closely they match your preferences and displays them in order.

---

## What you'll see

```
🏅 Available Sports Categories:

1. Football
2. Basketball
3. Cricket
4. Tennis
5. Badminton
6. Swimming
7. Cycling
8. Running
9. Gym Workout
10. MMA

👉 Type numbers OR keywords like: team, fitness, combat, outdoor

Enter your interests: fitness indoor strength

🏆 Recommended Sports for You:

👉 Gym Workout     (match score: 0.83)
👉 Badminton       (match score: 0.51)
👉 Basketball      (match score: 0.44)
```

---

## 🏟️ Sports in the Dataset

| # | Sport | Key Tags |
|---|-------|----------|
| 1 | Football | team, outdoor, running, ball, endurance |
| 2 | Basketball | team, indoor, jumping, ball, fitness |
| 3 | Cricket | bat, ball, team, strategy, focus |
| 4 | Tennis | racket, agility, speed, focus |
| 5 | Badminton | racket, indoor, agility, reaction |
| 6 | Swimming | water, solo, endurance, full body |
| 7 | Cycling | outdoor, cardio, speed, racing |
| 8 | Running | solo, endurance, stamina, cardio |
| 9 | Gym Workout | strength, weights, bodybuilding, health |
| 10 | MMA | combat, martial arts, wrestling, self defense |

---

## 🔑 Key Parts of the Code

| Part | What it does |
|------|-------------|
| `sports{}` dictionary | Stores each sport with descriptive keyword tags |
| `TfidfVectorizer` | Converts text descriptions into numerical vectors |
| `cosine_similarity()` | Compares user input vector with each sport vector |
| Number input handling | If user types `"3"`, it maps to Cricket's keywords automatically |
| Ranked output | Sorts results from highest to lowest match score |

---

## 💡 Smart Input Feature

You can type either **keywords** or a **number**:

```bash
Enter your interests: 5          # → Uses Badminton's own keywords
Enter your interests: outdoor team running   # → Finds best match
Enter your interests: combat self defense    # → Recommends MMA
```

---

## 📦 Libraries Used

| Library | Purpose |
|---------|---------|
| `scikit-learn` | TF-IDF vectorization and cosine similarity |

Only one external library needed!