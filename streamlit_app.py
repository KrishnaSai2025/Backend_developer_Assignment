import streamlit as st
import requests

API_URL = "http://localhost:5000"

def fetch_videos(page=1, per_page=5):
    res = requests.get(f"{API_URL}/videos", params={"page": page, "per_page": per_page})
    return res.json()

def search_videos(query, page=1, per_page=5):
    res = requests.get(f"{API_URL}/search", params={"query": query, "page": page, "per_page": per_page})
    return res.json()

def main():
    st.title("🎥 YouTube Videos Dashboard")
    search_query = st.text_input("🔎 Search Videos by Title/Description", "")
    page = st.number_input("Page", min_value=1, step=1, value=1)

    per_page = 5

    if search_query:
        data = search_videos(search_query, page=page, per_page=per_page)
    else:
        data = fetch_videos(page=page, per_page=per_page)

    if not data['videos']:
        st.warning("No videos found.")
    else:
        for video in data['videos']:
            st.subheader(video['title'])
            st.image(video['thumbnail_url'], width=400)
            st.caption(f"Published at: {video['published_at']}")
            st.write(video['description'])
            st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅️ Previous") and page > 1:
            st.experimental_set_query_params(page=page-1)
    with col2:
        if st.button("Next ➡️") and page < data['pages']:
            st.experimental_set_query_params(page=page+1)

if __name__ == "__main__":
    main()
