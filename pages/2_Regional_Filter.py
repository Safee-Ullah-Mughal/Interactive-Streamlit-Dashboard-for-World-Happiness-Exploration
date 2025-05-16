# pages/2_Regional_Filter.py

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# ---------------------------
# Page Config
# ---------------------------
st.set_page_config(page_title="Regional Filter", layout="wide")
st.title("🌍 Regional Happiness Comparison")

st.markdown("""
Explore happiness and development metrics across global regions.  
This page helps identify strengths, weaknesses, and relationships between happiness and contributing factors within a selected region.
""")

# ---------------------------
# Load Data
# ---------------------------
@st.cache_data
def load_data():
    return pd.read_csv("data/2015.csv")

df = load_data()

# ---------------------------
# Sidebar Filters
# ---------------------------
with st.sidebar:
    st.header("🌐 Filters")
    
    region_list = sorted(df["Region"].unique())
    selected_region = st.selectbox("Select Region:", region_list)

    metric_options = [
        "Economy (GDP per Capita)", "Family", "Health (Life Expectancy)",
        "Freedom", "Trust (Government Corruption)", "Generosity"
    ]
    selected_metric = st.selectbox("Compare with metric:", metric_options)

# ---------------------------
# Filter Region Data
# ---------------------------
region_df = df[df["Region"] == selected_region]

# ---------------------------
# Layout
# ---------------------------
col1, col2 = st.columns(2)

# ---------------------------
# Column 1: Box Plot & Summary
# ---------------------------
with col1:
    st.subheader(f"📦 Happiness Score Distribution in {selected_region}")

    fig1, ax1 = plt.subplots(figsize=(6, 4))
    sns.boxplot(data=region_df, y="Happiness Score", color="#48cae4", ax=ax1)

    mean_score = region_df["Happiness Score"].mean()
    ax1.axhline(mean_score, color="red", linestyle="--", label=f"Mean: {mean_score:.2f}")
    ax1.set_title("Box Plot of Happiness Scores")
    ax1.set_ylabel("Happiness Score")
    ax1.legend()
    st.pyplot(fig1)

    # Display Summary Stats
    top_country = region_df.loc[region_df["Happiness Score"].idxmax()]
    bottom_country = region_df.loc[region_df["Happiness Score"].idxmin()]
    score_range = top_country["Happiness Score"] - bottom_country["Happiness Score"]

    st.markdown("#### 🔎 Summary")
    st.success(f"Top: *{top_country['Country']}* – {top_country['Happiness Score']:.2f}")
    st.error(f"Bottom: *{bottom_country['Country']}* – {bottom_country['Happiness Score']:.2f}")
    st.info(f"📏 Score Range in Region: *{score_range:.2f}*")

# ---------------------------
# Column 2: Scatter Plot + Correlation
# ---------------------------
with col2:
    st.subheader(f"📉 {selected_metric} vs Happiness Score")

    fig2, ax2 = plt.subplots(figsize=(6, 4))
    sns.scatterplot(
        data=region_df,
        x=selected_metric,
        y="Happiness Score",
        hue="Country",
        palette="viridis",
        s=90,
        ax=ax2,
        legend=False
    )

    # Add regression line
    x = region_df[selected_metric]
    y = region_df["Happiness Score"]
    if len(x.unique()) > 1:  # Avoid crash if all values are the same
        m, b = np.polyfit(x, y, 1)
        ax2.plot(x, m * x + b, color='black', linestyle='--', label='Trend Line')
        corr = np.corrcoef(x, y)[0, 1]
        ax2.legend(title=f"Corr: {corr:.2f}")
    
    ax2.set_title(f"Happiness vs {selected_metric}")
    ax2.set_xlabel(selected_metric)
    ax2.set_ylabel("Happiness Score")
    ax2.grid(True)
    st.pyplot(fig2)

# ---------------------------
# Region Metric Interpretation
# ---------------------------
st.markdown("### 📊 Metric Strength Analysis")

avg_metric_score = region_df[selected_metric].mean()
global_avg = df[selected_metric].mean()
metric_strength = "above" if avg_metric_score > global_avg else "below"
metric_diff = abs(avg_metric_score - global_avg)

st.markdown(f"""
In *{selected_region}, the average **{selected_metric}* score is *{avg_metric_score:.2f}*,  
which is *{metric_strength} the global average* of *{global_avg:.2f}*  
(difference: {metric_diff:.2f}). This may suggest a regional trend worth exploring.
""")

# ---------------------------
# Full Data Table
# ---------------------------
st.markdown("### 📋 Regional Data Table")

sorted_df = region_df.sort_values("Happiness Score", ascending=False)
st.dataframe(sorted_df[["Country", "Happiness Score", selected_metric, "Region"]].reset_index(drop=True))