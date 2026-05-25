# 🏎️ F1 Podium Prediction — Classification Model

## 📌 What This Project Does

This project uses **real Formula 1 race data** to train a classification model that answers one question:

> *"Will this driver finish in the Top 3 (Podium)?"*

The model looks at a driver's starting grid position, laps completed, and points scored — and predicts **YES (Podium)** or **NO (Not Podium)**.

---

## 📊 Dataset Overview

| File | Rows | What's Inside |
|------|------|---------------|
| `results.csv` | 26,759 | Grid position, laps, points, finish position per race |
| `drivers.csv` | 861 | Driver names, nationality, DOB |
| `races.csv` | 1,125 | Race name, year, circuit, date |

---

### Features used:

| Feature | Description | Why it matters |
|---------|-------------|----------------|
| `grid` | Starting grid position | Front starters win more often |
| `laps` | Laps completed | More laps = stayed in the race |
| `points` | Points scored | Directly tied to finish position |

---

## 🎯 Sample Output

```
==================================================
       🏎️  F1 CLASSIFICATION MODEL
       Predicting Podium Finishes!
==================================================

✅ Results loaded   : 26759 rows
✅ Drivers loaded   : 861 rows
✅ Races loaded     : 1125 rows

🏆 PODIUM BREAKDOWN
🥇 Podium finishes     : 3396
❌ Non podium finishes : 12410

✅ Accuracy : ~97%

🌟 PREDICT A NEW RACE RESULT
🏎️  Grid Position : 1 | Laps: 50 | Points: 25
🏆 Prediction: YES — This driver will finish on the PODIUM!
```
--

## 📦 Libraries Used

| Library | Purpose |
|---------|---------|
| `pandas` | Loading and cleaning CSV data |
| `scikit-learn` | Decision Tree model, train/test split, accuracy metrics |
| `matplotlib` | Plotting the charts |

---

## 👨‍💻 About This Project

This is built as a beginner machine learning project to practise:
- Data cleaning with pandas
- Binary classification concepts
- Training and evaluating a Decision Tree
- Interpreting accuracy and classification reports