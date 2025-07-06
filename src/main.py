import json
import streamlit as st
from recommend import df, recommend_movies
from omdb_utils import get_movie_details

# Load API key
config = json.load(open("config.json"))
OMDB_API_KEY = config["OMDB_API_KEY"]

# Streamlit page setup
st.set_page_config(
    page_title="MovieMate - Find Your Movie!",
    layout="wide",
    page_icon="🎬"
)

# Custom CSS Styling
st.markdown("""
    <style>
    .block-container {
        padding: 2rem 3rem;
        background-color: #f8f9fa;
    }
    .stTextInput>div>div>input {
        border-radius: 12px;
        padding: 10px;
        border: 1px solid #ccc;
    }
    .movie-card {
        background: white;
        padding: 1rem;
        border-radius: 12px;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }
    .movie-title {
        font-weight: 600;
        font-size: 1.2rem;
    }
    .movie-meta {
        font-size: 0.9rem;
        color: #888;
    }
    .movie-poster {
        border-radius: 8px;
        box-shadow: 0 0 6px rgba(0,0,0,0.15);
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <h1 style='text-align: center;'>🎬 MovieMate: Discover Your Next Favorite Movie</h1>
""", unsafe_allow_html=True)

st.markdown("---")

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Choose Option", ["Search", "Mood Filter", "Smart Quiz"])

# Sidebar Tip
st.sidebar.info("👉 Use this sidebar to explore mood-based or quiz-based suggestions!")

# Page: Search & Recommend
if page == "Search":
    search_input = st.text_input("🔍 Search for a movie title")
    if search_input:
        movie_list = sorted(df['title'].dropna().unique())
        matched_movies = [title for title in movie_list if search_input.lower() in title.lower()]

        if matched_movies:
            selected_movie = st.selectbox("🎞️ Select from matches:", matched_movies)
            if st.button("🚀 Recommend Similar Movies"):
                recommendations = recommend_movies(selected_movie)
                if recommendations is None:
                    st.warning("No similar movies found.")
                else:
                    st.subheader("🎯 Recommended for You")
                    cols = st.columns(2)
                    for i, (_, row) in enumerate(recommendations.iterrows()):
                        title = row["title"]
                        plot, poster, imdb_link, rating = get_movie_details(title, OMDB_API_KEY)
                        with cols[i % 2]:
                            st.markdown("<div class='movie-card'>", unsafe_allow_html=True)
                            st.image(poster, width=200, caption="")
                            st.markdown(f"<div class='movie-title'>{title}</div>", unsafe_allow_html=True)
                            st.markdown(f"⭐ Rating: {rating}")
                            st.markdown(f"📝 {plot}")
                            st.markdown(f"[🔗 IMDb]({imdb_link})")
                            st.markdown("</div>", unsafe_allow_html=True)
        else:
            st.warning("No matches found.")

# Page: Mood Filter
elif page == "Mood Filter":
    st.subheader("🎭 Select Your Mood")
    mood = st.selectbox("Feeling...", ["-- Select --", "Happy", "Sad", "Romantic", "Adventurous", "Thrilled", "Scared"])
    
    genre_map = {
        "Happy": ["Comedy", "Family", "Animation"],
        "Sad": ["Drama"],
        "Romantic": ["Romance"],
        "Adventurous": ["Adventure", "Fantasy", "Action"],
        "Thrilled": ["Thriller", "Crime"],
        "Scared": ["Horror", "Mystery"]
    }

    if mood != "-- Select --":
        selected_genres = genre_map[mood]
        results = df[df["genres"].apply(lambda g: any(genre in g for genre in selected_genres))].drop_duplicates("title")
        st.subheader(f"🎬 Mood Matches for '{mood}'")
        cols = st.columns(2)

        for i, (_, row) in enumerate(results.sample(min(6, len(results))).iterrows()):
            title = row["title"]
            plot, poster, imdb_link, rating = get_movie_details(title, OMDB_API_KEY)
            with cols[i % 2]:
                st.markdown("<div class='movie-card'>", unsafe_allow_html=True)
                st.image(poster, width=200)
                st.markdown(f"<div class='movie-title'>{title}</div>", unsafe_allow_html=True)
                st.markdown(f"⭐ Rating: {rating}")
                st.markdown(f"📝 {plot}")
                st.markdown(f"[🔗 IMDb]({imdb_link})")
                st.markdown("</div>", unsafe_allow_html=True)

# Page: Smart Quiz
elif page == "Smart Quiz":
    st.subheader("🧠 Tell us what you like")
    quiz_genres = st.multiselect("Choose your favorite genres:", ["Action", "Drama", "Comedy", "Romance", "Thriller", "Sci-Fi", "Animation"])
    if st.button("🎯 Get Recommendations"):
        if not quiz_genres:
            st.warning("Please select at least one genre.")
        else:
            results = df[df["genres"].apply(lambda g: any(gen in g for gen in quiz_genres))].drop_duplicates("title")
            st.subheader("🎉 Recommendations for you")
            cols = st.columns(2)

            for i, (_, row) in enumerate(results.sample(min(6, len(results))).iterrows()):
                title = row["title"]
                plot, poster, imdb_link, rating = get_movie_details(title, OMDB_API_KEY)
                with cols[i % 2]:
                    st.markdown("<div class='movie-card'>", unsafe_allow_html=True)
                    st.image(poster, width=200)
                    st.markdown(f"<div class='movie-title'>{title}</div>", unsafe_allow_html=True)
                    st.markdown(f"⭐ Rating: {rating}")
                    st.markdown(f"📝 {plot}")
                    st.markdown(f"[🔗 IMDb]({imdb_link})")
                    st.markdown("</div>", unsafe_allow_html=True)
