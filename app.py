import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("🎬 Netflix Data Analysis")
st.write("By: Omkar Patil | March 2026")

df = pd.read_csv("netflix_data.csv")
df["date_added"] = pd.to_datetime(df["date_added"], format="mixed", errors="coerce")
df["year_added"] = df["date_added"].dt.year

# 1. Movies vs TV Shows
st.header("1. Movies vs TV Shows")
fig1, ax1 = plt.subplots()
df["type"].value_counts().plot(kind="bar", color=["red","black"], ax=ax1)
ax1.set_title("Movies vs TV shows")
ax1.set_xlabel("Type")
ax1.set_ylabel("Count")
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(fig1)
plt.close()
st.write("✅ Netflix has more Movies than TV Shows")

# 2. Top 10 Genres
st.header("2. Top 10 Genres")
fig2, ax2 = plt.subplots()
genres = df["listed_in"].str.split(",").explode()
genres.value_counts().head(10).plot(kind="barh", color="red", ax=ax2)
ax2.set_title("Top 10 genres")
ax2.grid(True)
plt.tight_layout()
st.pyplot(fig2)
plt.close()
st.write("✅ Comedies and Dramas are most popular")

# 3. Content Added Per Year
st.header("3. Content Added Per Year")
fig3, ax3 = plt.subplots()
df["year_added"].value_counts().sort_index().plot(kind="line", color="red", ax=ax3)
ax3.set_title("Content Added Per Year")
ax3.set_xlabel("YEARS")
ax3.set_ylabel("movies count")
ax3.grid(True)
plt.tight_layout()
st.pyplot(fig3)
plt.close()
st.write("✅ Netflix grew rapidly between 2015-2020")

# 4. Top 10 Countries
st.header("4. Top 10 Countries Producing Content")
fig4, ax4 = plt.subplots()
df["country"].value_counts().head(10).plot(kind="bar", color="red", ax=ax4)
ax4.set_title("Top 10 countries")
ax4.set_ylabel("Movies count")
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(fig4)
plt.close()
st.write("✅ USA produces the most Netflix content")

# 5. Top 10 Ratings
st.header("5. Top 10 Ratings")
fig5, ax5 = plt.subplots()
df["rating"].value_counts().head(10).plot(kind="bar", color="black", ax=ax5)
ax5.set_title("Top 10 ratings")
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(fig5)
plt.close()
st.write("✅ TV-MA and TV-14 are the most common ratings")