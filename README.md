# 🎬 MovieMate – AI Movie Recommendation App

Welcome to **MovieMate**, your intelligent movie recommendation companion! Whether you're feeling happy, sad, romantic, or just bored, MovieMate helps you find the perfect movie using AI-powered similarity detection and mood-based filtering.
🚀 Built using **Python**, **Streamlit**, and the **OMDb API**, this app provides a modern, responsive UI similar to OTT platforms — but with a light theme and personalized suggestions.
---
## 🔗 Live Demo
👉 [Try the app on Render](https://movie-recommendation-app-h2rs.onrender.com/)
---
## ✨ Features
- 🔍 **Smart Search** – Search for any movie and get intelligent recommendations.
- 😄 **Mood-Based Filtering** – Select your current mood from the sidebar and receive curated suggestions.
- 🧠 **Interactive Quiz** – Not sure what to watch? Take a quick quiz and let the app guide you.
- 🎞️ **OMDb API Integration** – Live movie posters, ratings, genres, and plots from the OMDb API.
- 📱 **Clean, Responsive UI** – Inspired by Disney+ and Prime Video interfaces, but light-themed.
---
## 🛠️ Tech Stack
- **Python 3.9+**
- **Streamlit** – UI framework
- **pandas, scikit-learn, gdown** – Recommendation engine
- **OMDb API** – For movie metadata
- **Render** – Deployment
---
##📍 How it Works  
Movie similarity is calculated using TF-IDF vectorization and cosine similarity.

The OMDb API fetches live movie posters, ratings, and plot descriptions.

A mood-based system and quiz are integrated into the UI for user-driven exploration.
Author  
Tanisha Wal  
https://github.com/tanisha-wal

## 📁 Folder Structure

```text
movie_recommendation/
│
├── src/
│   ├── main.py             # Main Streamlit app
│   ├── recommend.py        # Recommendation logic
│   ├── omdb_utils.py       # OMDb API functions
│   ├── config.json         # Stores OMDb API key
│   ├── cosine_sim.pkl      # Precomputed similarity matrix
│   ├── tfidf_matrix.pkl    # TF-IDF matrix
│   ├── movies.csv          # Movie metadata
│   └── df_cleaned.pkl      # Cleaned movie dataframe
│
├── requirements.txt        # Python dependencies
├── .gitignore              # Git ignore file
└── README.md               # You're reading it!

