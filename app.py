# app.py

import streamlit as st

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="World Happiness Dashboard",
    page_icon="🌍",
    layout="wide"
)

# -------------------------------
# Main Title
# -------------------------------
st.title("🌍 Global Happiness Dashboard")
st.markdown("### *An Interactive Data Exploration App Built with Streamlit*")

st.markdown("---")

# -------------------------------
# Course & Project Information
# -------------------------------
st.subheader("📚 Course Project Information")
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    - **Course**: Advanced Programming in Python  
    - **Instructor**: Dr. Sohaib Younis  
    - **University**: National University of Science & Technology (NUST) Islamabad 
    - **Semester**: Spring 2025  
    """)

with col2:
    st.markdown("""
    - **Project Title**: *World Happiness Report – Interactive Streamlit Dashboard*  
    - **Dataset**: [Kaggle - World Happiness Report](https://www.kaggle.com/datasets/unsdsn/world-happiness)  
    - **Tool**: Streamlit  
    """)

st.markdown("---")

# -------------------------------
# Team Members
# -------------------------------
st.subheader("👨‍💻 Team Members")
cols = st.columns(4)
team = ["Safee Ullah", "Mohammad Noman", "Tehreem Baig", "Ayesha Ghaffar"]

for i in range(4):
    with cols[i]:
        st.markdown(f"""
        👤 **{team[i]}**  
        - Role: Page {i+1}
        """)

st.markdown("---")

# -------------------------------
# Project Overview
# -------------------------------
st.subheader("🧭 About the Project")
st.markdown("""
The **World Happiness Report** ranks countries based on factors such as:
- **GDP per capita**
- **Social support**
- **Healthy life expectancy**
- **Freedom to make life choices**
- **Generosity**
- **Perceptions of corruption**

This dashboard allows users to explore this dataset through:
- Interactive **charts** and **maps**
- Regional and country-level filtering
- Trend and correlation analysis

Use the sidebar to navigate through **4 dashboard pages**, each created by a different team member.
""")

# -------------------------------
# Optional Visual or Lottie
# -------------------------------
st.markdown("---")
st.info("⬅️ Use the **sidebar** to explore the dashboard pages!")


st.image("logo.png", width=400)

