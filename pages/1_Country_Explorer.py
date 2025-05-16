# pages/1_Country_Explorer.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------
# Page Config
# ---------------------------
st.set_page_config(page_title="Country Explorer", layout="wide")
st.title("🔍 Country Happiness Explorer")

st.markdown("""
Use this page to explore detailed happiness metrics for any country and compare them with others in a selected happiness rank range.
""")

# ---------------------------
# Load Data
# ---------------------------
@st.cache_data
def load_data():
    return pd.read_csv("data/2015.csv")

df = load_data()

# ---------------------------
# Sidebar: Filters
# ---------------------------
with st.sidebar:
    st.header("🎛️ Controls")
    country_input = st.text_input("Enter a country", value="Norway")

    min_rank = int(df["Happiness Rank"].min())
    max_rank = int(df["Happiness Rank"].max())
    rank_range = st.slider("Select rank range", min_rank, max_rank, (1, 50))

# ---------------------------
# Main Layout: Two Columns
# ---------------------------
col1, col2 = st.columns(2)

# ---------------------------
# Column 1: Country Factor Breakdown
# ---------------------------
with col1:
    st.subheader(f"📍 Factor Breakdown for: {country_input}")

    country_data = df[df["Country"].str.lower() == country_input.lower()]

    if not country_data.empty:
        # --- Table 1: Country Overview ---
        with st.expander("📋 Country Metrics Table"):
            display_cols = ["Region", "Happiness Rank", "Happiness Score",
                            "Economy (GDP per Capita)", "Family", "Health (Life Expectancy)",
                            "Freedom", "Trust (Government Corruption)", "Generosity"]
            st.dataframe(country_data[display_cols].T.rename(columns={country_data.index[0]: country_input}))

        # --- Bar Chart: Happiness Factors (excluding Dystopia Residual) ---
        st.markdown("### 🧩 Factor Contributions")
        factors = ["Economy (GDP per Capita)", "Family", "Health (Life Expectancy)",
                   "Freedom", "Trust (Government Corruption)", "Generosity"]
        values = country_data[factors].iloc[0]

        fig1, ax1 = plt.subplots(figsize=(6, 4))
        bars = ax1.bar(factors, values, color="#00b4d8", edgecolor="black")
        ax1.set_ylabel("Score")
        ax1.set_title(f"{country_input} - Happiness Factor Breakdown", fontsize=12)
        ax1.tick_params(axis='x', rotation=45)
        ax1.grid(axis='y', linestyle='--', alpha=0.7)
        st.pyplot(fig1)

    else:
        st.warning("🚫 Country not found. Please check your spelling.")

# ---------------------------
# Column 2: Horizontal Bar Chart of Filtered Countries
# ---------------------------
# ---------------------------
# World Map of Happiness Scores
# ---------------------------
st.markdown("---")
st.subheader("🗺️ Global Happiness Map (2015)")

try:
    import plotly.express as px

    fig_map = px.choropleth(
        df,
        locations="Country",
        locationmode="country names",
        color="Happiness Score",
        hover_name="Country",
        color_continuous_scale="YlGnBu",
        title="Global Happiness Scores by Country",
    )
    fig_map.update_layout(margin={"r":0,"t":30,"l":0,"b":0})
    st.plotly_chart(fig_map, use_container_width=True)

except ModuleNotFoundError:
    st.warning("Plotly is not installed. Run `pip install plotly` to enable the map.")
