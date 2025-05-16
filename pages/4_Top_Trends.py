# -----------------------------------------------------------------------------------------
# 📄 Page: Top Trends in Global Happiness (2015)
# -----------------------------------------------------------------------------------------

# ---------------------------
# Import Required Libraries
# ---------------------------
import streamlit as st               # Streamlit for interactive UI
import pandas as pd                  # Pandas for data manipulation
import matplotlib.pyplot as plt      # Matplotlib for static visualizations
import seaborn as sns                ## Seaborn for enhanced plotting

# ---------------------------
# Page Configuration
# ---------------------------
st.set_page_config(page_title="Top Trends", layout="wide")     ## page title and layout

# ---------------------------
# Load Dataset with Caching
# ---------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("data/2015.csv")  # Adjust path if needed
    return df

df = load_data()

st.title("📊 Top Trends in Global Happiness (2015)")            # Main page title

# ---------------------------
# Sidebar: Filter Options
# ---------------------------
st.sidebar.header("🔍 Filter Options")

# Text input: Optional search for a country
country_input = st.sidebar.text_input("Search Country (optional):").strip().lower()

# Slider: Minimum happiness score
min_score = st.sidebar.slider("Minimum Happiness Score", 2.0, 8.0, 5.0)

# Selectbox: Filter by Region
regions = df["Region"].unique()
selected_region = st.sidebar.selectbox("Select Region (optional):", ["All"] + sorted(regions.tolist()))

# ---------------------------
# Data Filtering Based on Inputs
# ---------------------------
filtered_df = df[df["Happiness Score"] >= min_score]
if selected_region != "All":
    filtered_df = filtered_df[filtered_df["Region"] == selected_region]
if country_input:
    filtered_df = filtered_df[filtered_df["Country"].str.lower().str.contains(country_input)]

# ---------------------------
# Trend 1: Top 10 Happiest Countries
# ---------------------------
st.subheader("🏅 Top 10 Happiest Countries")

top10 = filtered_df.sort_values("Happiness Score", ascending=False).head(10)

fig1, ax1 = plt.subplots(figsize=(10, 5))
sns.barplot(x="Happiness Score", y="Country", data=top10, hue="Country", palette="viridis", ax=ax1,legend=False)
ax1.set_title("Top 10 Happiest Countries (Filtered)")
st.pyplot(fig1)

# ---------------------------
# Trend 2: Average Contribution of Each Factor
# ---------------------------
st.subheader("📈 Average Factor Contributions")

factors = [
    "Economy (GDP per Capita)",
    "Family",
    "Health (Life Expectancy)",
    "Freedom",
    "Trust (Government Corruption)",
    "Generosity"
]

avg_factors = filtered_df[factors].mean().sort_values(ascending=False)

fig2, ax2 = plt.subplots(figsize=(10, 5))
avg_factors.plot(kind='bar', color='skyblue', ax=ax2, edgecolor="black")
ax2.set_title("Average Contribution of Each Factor to Happiness")
ax2.set_ylabel("Score")
st.pyplot(fig2)

# ---------------------------
# Trend 3: Region-wise Happiness Scores
# ---------------------------
st.subheader("🌍 Regional Happiness Trends")

region_avg = filtered_df.groupby("Region")["Happiness Score"].mean().sort_values(ascending=False)

fig3, ax3 = plt.subplots(figsize=(10, 6))
region_avg.plot(kind="barh", color="coral", ax=ax3)
ax3.set_title("Average Happiness Score by Region (Filtered)")
ax3.set_xlabel("Average Score")
st.pyplot(fig3)

# ---------------------------
# Final Table: Display Filtered Dataset
# ---------------------------
st.subheader("📋 Filtered Data Table")

if not filtered_df.empty:
    st.dataframe(filtered_df.reset_index(drop=True), use_container_width=True)
else:
    st.warning("⚠️ No data available for the selected filters.")
