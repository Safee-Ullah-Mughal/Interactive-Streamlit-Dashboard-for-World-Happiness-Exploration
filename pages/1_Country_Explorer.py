# ---------------------------
# Country Happiness Explorer
# ---------------------------

# Import essential libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# ---------------------------
# Streamlit Page Configuration
# ---------------------------
st.set_page_config(page_title="Country Explorer", layout="wide")
st.title("Country Happiness Explorer")

# Introduction text
st.markdown("""
Welcome to the **Country Happiness Explorer**!
This tool allows you to:
- Analyze a country's happiness score across key life factors.
- Compare it with global averages.
- See how countries rank globally in 2015.
- Visualize happiness scores on a world map.
""")

# ---------------------------
# Load Dataset (cached)
# ---------------------------
@st.cache_data
def load_data():
    return pd.read_csv("data/2015.csv")

df = load_data()

# ---------------------------
# Sidebar Filters & Controls
# ---------------------------
with st.sidebar:
    st.header("Controls")

    # Dropdown with searchable country list
    country_list = df["Country"].sort_values().unique()
    country_input = st.selectbox("Select a country", options=country_list, index=list(country_list).index("Pakistan"))

    # Rank range slider
    min_rank = int(df["Happiness Rank"].min())
    max_rank = int(df["Happiness Rank"].max())
    rank_range = st.slider("Select rank range", min_rank, max_rank, (1, 20))

# ---------------------------
# Layout: Two Column Display
# ---------------------------
col1, col2 = st.columns(2)

# ===========================
# COLUMN 1: Country Profile
# ===========================
with col1:
    st.subheader(f"Factor Breakdown for: **{country_input}**")

    # Filter the country data
    country_data = df[df["Country"] == country_input]

    if not country_data.empty:
        country_row = country_data.iloc[0]

        factors = [
            "Economy (GDP per Capita)", "Family", "Health (Life Expectancy)",
            "Freedom", "Trust (Government Corruption)", "Generosity"
        ]

        with st.expander(" Country Summary Table"):
            summary_cols = ["Region", "Happiness Rank", "Happiness Score"] + factors
            st.dataframe(
                country_data[summary_cols].T.rename(columns={country_data.index[0]: country_input})
            )

        st.markdown("### Factor Contributions Compared to Global Average")

        global_avg = df[factors].mean()
        country_values = country_row[factors]
        diff = country_values - global_avg

        fig1, ax1 = plt.subplots(figsize=(6, 4))
        bar_colors = ["#2a9d8f" if d >= 0 else "#e76f51" for d in diff]

        ax1.bar(factors, country_values, color=bar_colors, edgecolor="black")
        ax1.axhline(global_avg.mean(), color='gray', linestyle='--', linewidth=1)
        ax1.set_ylabel("Score")
        ax1.set_title(f"{country_input} vs Global Factor Averages", fontsize=12)
        ax1.tick_params(axis='x', rotation=45)
        ax1.grid(axis='y', linestyle='--', alpha=0.6)
        st.pyplot(fig1)

        st.markdown("#### Interpretation")
        above_avg = diff[diff > 0].index.tolist()
        below_avg = diff[diff < 0].index.tolist()

        if above_avg:
            st.success(f"**Above average in:** {', '.join(above_avg)}")
        if below_avg:
            st.error(f"**Below average in:** {', '.join(below_avg)}")
    else:
        st.warning("Country not found. Please check your spelling.")

# ===========================
# COLUMN 2: Rank Range Overview with Pie Chart
# ===========================
with col2:
    st.subheader(f"Countries Ranked Between {rank_range[0]} and {rank_range[1]}")

    filtered_df = df[(df["Happiness Rank"] >= rank_range[0]) & (df["Happiness Rank"] <= rank_range[1])]
    top5 = filtered_df.nsmallest(5, "Happiness Rank")
    bottom5 = filtered_df.nlargest(5, "Happiness Rank")

    st.markdown("##### Top 5 in Selected Range")
    st.dataframe(top5[["Country", "Happiness Score"]].reset_index(drop=True))

    st.markdown("##### Bottom 5 in Selected Range")
    st.dataframe(bottom5[["Country", "Happiness Score"]].reset_index(drop=True))


    # Tree Map: Happiness Scores in Selected Rank Range
st.markdown("#### Tree Map: Happiness Scores")

fig_tree = px.treemap(
    filtered_df,
    path=["Country"],
    values="Happiness Score",
    color="Happiness Score",
    color_continuous_scale=px.colors.sequential.Tealgrn,
    title="Tree Map of Happiness Scores by Country",
    hover_data={"Happiness Score": ':.2f'},  # show score with 2 decimals on hover
)
# Improve layout for clarity and spacing
fig_tree.update_layout(
    margin=dict(t=60, l=10, r=10, b=10),
    title_font_size=20,
)
# Enhance text visibility inside the treemap
fig_tree.data[0].texttemplate = "%{label}<br>%{value:.2f}"
st.plotly_chart(fig_tree, use_container_width=True)


# ===========================
# Global Choropleth Map
# ===========================
st.markdown("---")
st.subheader("World Happiness Scores (2015)")

try:
    fig_map = px.choropleth(
        df,
        locations="Country",
        locationmode="country names",
        color="Happiness Score",
        hover_name="Country",
        color_continuous_scale="YlGnBu",
        title="Global Happiness Distribution (2015)",
    )
    fig_map.update_layout(margin={"r": 50, "t": 30, "l": 0, "b": 0})
    st.plotly_chart(fig_map, use_container_width=True)
except ModuleNotFoundError:
    st.warning("Plotly is not installed. Please run `pip install plotly` to view the map.")

# ===========================
# Navigation Links
# ===========================
st.markdown("---")
st.title("Quick Navigation")

st.page_link("app.py", label="Home")
st.page_link("pages/1_Country_Explorer.py", label="Country Explorer by Safee Ullah (You are here right now)")
st.page_link("pages/2_Regional_Filter.py", label="Regional Highlights by Muhammad Noman")
st.page_link("pages/3_Global_Summary.py", label="Global Summary by Tehreem Baig")
st.page_link("pages/4_Top_Trends.py", label="Top Trends by Ayesha Ghaffar")
