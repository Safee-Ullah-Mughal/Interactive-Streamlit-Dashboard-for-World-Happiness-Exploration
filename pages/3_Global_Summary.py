import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# === Page Config ===
st.set_page_config(page_title="🌍 2015 Global Happiness Dashboard", layout="wide")

# === Load and Clean Data ===
df = pd.read_csv("data/2015.csv") 
df.columns = df.columns.str.strip().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')

# === Title ===
st.title("🌏 2015 Global Happiness Dashboard")

# === Sidebar Filter ===
st.sidebar.header("🔧 Filters")
rank_limit = st.sidebar.slider("Show countries ranked up to:", 1, int(df['Happiness_Rank'].max()), 50)
filtered_df = df[df['Happiness_Rank'] <= rank_limit]

# === Optional Column Display ===
if st.sidebar.checkbox("Show column names"):
    st.write("📋 Columns:", df.columns.tolist())

# === Global Trend 1: Happiness Score by Region ===
st.subheader("📊 Global Trend: Average Happiness Score by Region")
region_avg_score = df.groupby('Region')['Happiness_Score'].mean().sort_values(ascending=False)
fig1, ax1 = plt.subplots(figsize=(10, 5))
sns.barplot(x=region_avg_score.values, y=region_avg_score.index, palette='viridis', ax=ax1)
ax1.set_title("Average Happiness Score by Region")
ax1.set_xlabel("Score")
ax1.set_ylabel("Region")
st.pyplot(fig1)

# === Global Trend 2: Average Happiness Rank by Region ===
st.subheader("🏅 Global Trend: Average Happiness Rank by Region")
region_avg_rank = df.groupby('Region')['Happiness_Rank'].mean().sort_values()
fig2, ax2 = plt.subplots(figsize=(10, 5))
sns.barplot(x=region_avg_rank.values, y=region_avg_rank.index, palette='coolwarm', ax=ax2)
ax2.set_title("Average Happiness Rank by Region (Lower is Better)")
ax2.set_xlabel("Rank")
ax2.set_ylabel("Region")
st.pyplot(fig2)

# === Global Trend 3: Economy (GDP per Capita) ===
st.subheader("💰 Global Trend: Economy (GDP per Capita) by Region")
region_gdp = df.groupby('Region')['Economy_GDP_per_Capita'].mean()
fig3, ax3 = plt.subplots(figsize=(10, 5))
sns.barplot(x=region_gdp.values, y=region_gdp.index, palette='plasma', ax=ax3)
ax3.set_title("Average GDP per Capita by Region")
ax3.set_xlabel("GDP per Capita")
ax3.set_ylabel("Region")
st.pyplot(fig3)

# === Global Trend 4: Health (Life Expectancy) ===
st.subheader("🏥 Global Trend: Health (Life Expectancy) by Region")
region_health = df.groupby('Region')['Health_Life_Expectancy'].mean().sort_values(ascending=False)
fig4, ax4 = plt.subplots(figsize=(10, 5))
sns.barplot(x=region_health.values, y=region_health.index, palette='rocket', ax=ax4)
ax4.set_title("Average Life Expectancy by Region")
ax4.set_xlabel("Life Expectancy")
ax4.set_ylabel("Region")
st.pyplot(fig4)

# === Global Trend 5: Freedom ===
st.subheader("🕊 Global Trend: Freedom by Region")
region_freedom = df.groupby('Region')['Freedom'].mean().sort_values(ascending=False)
fig5, ax5 = plt.subplots(figsize=(10, 5))
sns.barplot(x=region_freedom.values, y=region_freedom.index, palette='cubehelix', ax=ax5)
ax5.set_title("Average Freedom Score by Region")
ax5.set_xlabel("Freedom Score")
ax5.set_ylabel("Region")
st.pyplot(fig5)

# === Top 5 Happiest Countries ===
st.subheader("🌟 Top 5 Countries with Highest Happiness Scores")
top5 = df.sort_values(by='Happiness_Score', ascending=False).head(5)
fig6, ax6 = plt.subplots(figsize=(8, 5))
sns.barplot(x='Happiness_Score', y='Country', data=top5, palette='crest', ax=ax6)
ax6.set_title("Top 5 Happiest Countries")
st.pyplot(fig6)

# === 🥧 Pie Chart: Country Distribution by Region (Top Ranked Only) ===
st.subheader("🥧 Regional Distribution of Top-Ranked Happy Countries")

region_counts = filtered_df['Region'].value_counts()
fig_pie, ax_pie = plt.subplots()
ax_pie.pie(region_counts, labels=region_counts.index, autopct='%1.1f%%', startangle=140)
ax_pie.axis('equal')  # Equal aspect ratio ensures a circular pie chart
st.pyplot(fig_pie)

# === Raw Data Viewer ===
if st.checkbox("📄 Show Raw Data Table"):
    st.dataframe(filtered_df)
