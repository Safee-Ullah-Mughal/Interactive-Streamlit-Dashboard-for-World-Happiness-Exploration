# pages/1_Country_Explorer.py

# Import required libraries
import streamlit as st                 # Streamlit for building interactive web apps
import pandas as pd                   # Pandas for data handling
import matplotlib.pyplot as plt       # Matplotlib for static plotting

# ---------------------------
# Page Configuration
# ---------------------------
st.set_page_config(page_title="Country Explorer", layout="wide")  # Set the page title and layout
st.title("🔍 Country Happiness Explorer")                         # Page header/title

# Description of the app functionality
st.markdown("""
Use this page to explore the happiness landscape of countries based on key social, economic, and governance factors.
Gain insights by comparing a specific country's profile with global averages and other countries within a rank range.
""")

# ---------------------------
# Load Dataset with Caching
# ---------------------------
@st.cache_data                        # Cache the function to avoid reloading the data every time
def load_data():
    return pd.read_csv("data/2015.csv")  # Load CSV containing 2015 happiness data

df = load_data()                      # Store dataset in a DataFrame

# ---------------------------
# Sidebar: User Filters
# ---------------------------
with st.sidebar:
    st.header("🎛️ Controls")                                     # Sidebar title
    country_input = st.text_input("Enter a country", value="Norway")  # Input field to enter a country name

    # Determine slider limits based on min and max ranks in data
    min_rank = int(df["Happiness Rank"].min())
    max_rank = int(df["Happiness Rank"].max())
    
    # Slider to select a range of happiness ranks
    rank_range = st.slider("Select rank range", min_rank, max_rank, (1, 50))

# ---------------------------
# Page Layout with Two Columns
# ---------------------------
col1, col2 = st.columns(2)            # Split the page into two vertical columns

# ---------------------------
# Column 1: Country Profile
# ---------------------------
with col1:
    st.subheader(f"📍 Factor Breakdown: {country_input}")  # Subheader for selected country

    # Filter the dataset for the entered country name (case insensitive)
    country_data = df[df["Country"].str.lower() == country_input.lower()]

    # If country exists in the data
    if not country_data.empty:
        country_row = country_data.iloc[0]  # Extract the first (and only) row for that country

        # Define the list of factors to analyze
        factors = [
            "Economy (GDP per Capita)", "Family", "Health (Life Expectancy)",
            "Freedom", "Trust (Government Corruption)", "Generosity"
        ]

        # --- Table: Summary Stats ---
        with st.expander("📋 Country Summary Table"):  # Expandable section to show country details
            display_cols = ["Region", "Happiness Rank", "Happiness Score"] + factors
            st.dataframe(country_data[display_cols].T.rename(columns={country_data.index[0]: country_input}))  # Transpose for vertical display

        # --- Bar Chart: Factor Comparison vs Global Average ---
        st.markdown("### 🧩 Factor Contributions (vs Global Average)")
        global_avg = df[factors].mean()              # Calculate global average for each factor
        values = country_row[factors]                # Get selected country’s factor values
        differences = values - global_avg            # Difference from global average

        # Plotting the bar chart
        fig1, ax1 = plt.subplots(figsize=(6, 4))
        bars = ax1.bar(
            factors,
            values,
            color=["#2a9d8f" if diff >= 0 else "#e76f51" for diff in differences],  # Green if above avg, red if below
            edgecolor="black"
        )
        ax1.axhline(y=global_avg.mean(), color='gray', linestyle='--', linewidth=1)  # Line showing global mean
        ax1.set_ylabel("Score")
        ax1.set_title(f"{country_input} vs Global Average", fontsize=12)
        ax1.tick_params(axis='x', rotation=45)  # Rotate x-axis labels for readability
        ax1.grid(axis='y', linestyle='--', alpha=0.6)
        st.pyplot(fig1)  # Display the plot

        # --- Interpretation Block ---
        st.markdown("#### 📘 Interpretation")
        above_avg = differences[differences > 0].index.tolist()   # Factors above global average
        below_avg = differences[differences < 0].index.tolist()   # Factors below global average

        if above_avg:
            st.success(f"**Above average in:** {', '.join(above_avg)}")  # Show positively performing factors
        if below_avg:
            st.error(f"**Below average in:** {', '.join(below_avg)}")    # Show weaker factors

    else:
        # If country name is not found
        st.warning("🚫 Country not found. Please check your spelling.")

# ---------------------------
# Column 2: Rank Range Comparison
# ---------------------------
with col2:
    st.subheader(f"📊 Countries in Rank Range: {rank_range[0]} - {rank_range[1]}")  # Display selected range

    # Filter countries within selected happiness rank range
    filtered_df = df[(df["Happiness Rank"] >= rank_range[0]) & (df["Happiness Rank"] <= rank_range[1])]
    
    # Select top 5 and bottom 5 by rank (within the range)
    top5 = filtered_df.nsmallest(5, "Happiness Rank")
    bottom5 = filtered_df.nlargest(5, "Happiness Rank")

    # Show top 5 countries in a table
    st.markdown("##### 🏅 Top 5 Countries in Selected Range")
    st.dataframe(top5[["Country", "Happiness Score"]].reset_index(drop=True))

    # Show bottom 5 countries in a table
    st.markdown("##### ⚠️ Bottom 5 Countries in Selected Range")
    st.dataframe(bottom5[["Country", "Happiness Score"]].reset_index(drop=True))

    # --- Horizontal Bar Chart for Range ---
    fig2, ax2 = plt.subplots(figsize=(6, 8))
    filtered_df_sorted = filtered_df.sort_values(by="Happiness Score")  # Sort by score for better visual
    ax2.barh(filtered_df_sorted["Country"], filtered_df_sorted["Happiness Score"], color="#4361ee")  # Horizontal bar chart
    ax2.set_xlabel("Happiness Score")
    ax2.set_title("Happiness Scores by Country in Selected Rank Range")
    st.pyplot(fig2)

# ---------------------------
# Global Happiness Choropleth Map
# ---------------------------
st.markdown("---")                  # Divider line
st.subheader("🗺️ Global Happiness Map (2015)")  # Section title

# Try importing plotly for choropleth map
try:
    import plotly.express as px     # Try importing Plotly Express for interactive map

    # Create the choropleth map
    fig_map = px.choropleth(
        df,
        locations="Country",                        # Column for country names
        locationmode="country names",               # Use country names to map locations
        color="Happiness Score",                    # Color scale based on happiness score
        hover_name="Country",                       # Show country name on hover
        color_continuous_scale="YlGnBu",            # Color scheme
        title="Global Happiness Scores by Country", # Map title
    )
    fig_map.update_layout(margin={"r":0,"t":30,"l":0,"b":0})  # Remove margins for cleaner display
    st.plotly_chart(fig_map, use_container_width=True)        # Display the interactive map

except ModuleNotFoundError:
    # If plotly isn't installed, show warning
    st.warning("Plotly is not installed. Run `pip install plotly` to enable the map.")
