
import os
import logging

# Download cosine_sim.pkl from Google Drive if not present
if not os.path.exists('src/cosine_sim.pkl'):
    import gdown
    gdown.download('https://drive.google.com/uc?id=1kbtRVzKFLYiHpZdkPwf2r36zmciHzyeH', 'src/cosine_sim.pkl', quiet=False)

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("recommend.log", encoding="utf-8"),
        logging.StreamHandler()
    ]
)

import joblib

logging.info("🔁 Loading data...")
try:
    df = joblib.load('src/df_cleaned.pkl')
    cosine_sim = joblib.load('src/cosine_sim.pkl')
    logging.info("✅ Data loaded successfully.")
except Exception as e:
    logging.error("❌ Failed to load required files: %s", str(e))
    raise e


def recommend_movies(movie_name, top_n=5):
    logging.info("🎬 Recommending movies for: '%s'", movie_name)
    idx = df[df['title'].str.lower() == movie_name.lower()].index
    if len(idx) == 0:
        logging.warning("⚠️ Movie not found in dataset.")
        return None
    idx = idx[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:top_n + 1]
    movie_indices = [i[0] for i in sim_scores]
    logging.info("✅ Top %d recommendations ready.", top_n)
    result_df = df[['title']].iloc[movie_indices].reset_index(drop=True)
    result_df.index = result_df.index + 1  # Start from 1
    result_df.index.name = "S.No."
    return result_df
