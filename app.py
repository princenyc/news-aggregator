import streamlit as st

# Page title and styling
st.set_page_config(page_title="The Daily Report", layout="wide")
st.title("📰 The Daily Report")
st.markdown("A curated feed of stories worth your time.")

# Example news data (you'll replace this with your own later)
news_items = [
    {
        "title": "Black-Owned Bookstores Are Booming",
        "url": "https://example.com/bookstores",
        "image": "https://via.placeholder.com/600x300?text=Bookstores",
        "summary": "Across the U.S., Black-owned bookstores are experiencing a cultural revival and business boom."
    },
    {
        "title": "Inside the Housing Crisis in NYC",
        "url": "https://example.com/housing",
        "image": "https://via.placeholder.com/600x300?text=Housing+Crisis",
        "summary": "The city's rent crisis is exposing gaps in social safety nets and long-term planning."
    },
    {
        "title": "Zendaya to Lead MGM Thriller Series",
        "url": "https://example.com/zendaya-thriller",
        "image": "https://via.placeholder.com/600x300?text=Zendaya+Thriller",
        "summary": "MGM confirms Zendaya as the lead in a new thriller series set for 2025."
    }
]

# Display each news item
for item in news_items:
    st.image(item["image"], use_column_width=True)
    st.markdown(f"### [{item['title']}]({item['url']})")
    st.write(item["summary"])
    st.markdown("---")
