# 🌎 World Happiness Dashboard

An interactive multi-page web app for exploring global happiness metrics, built with Python and Streamlit.

---

## 📊 Project Overview

This dashboard allows users to explore the **World Happiness Report (2015)** dataset with rich, interactive visualizations.  
It supports country-level, regional, and global insights through four structured pages.

> **Developed as part of an academic project** in compliance with all guidelines, including multi-page layout, interactive filters, and multiple visualization libraries.

---

## 🗂️ Dataset Details

- **Source**: [Kaggle – World Happiness Report](https://www.kaggle.com/datasets/unsdsn/world-happiness)
- **Year**: 2015
- **Features**:
  - Happiness Score
  - GDP per Capita
  - Health (Life Expectancy)
  - Family
  - Freedom
  - Generosity
  - Trust in Government

---

## 🧭 App Navigation (Pages)

| Page | Title | Features |
|------|-------|----------|
| 1️⃣ | Country Explorer | `text_input`, `slider`, bar chart of happiness factors, filtered countries |
| 2️⃣ | Regional Filter | `selectbox`, box plot of scores, GDP vs happiness scatter plot |
| 3️⃣ | Global Summary | World map (choropleth), animated map, correlation heatmap |
| 4️⃣ | Top Performers & Trends | Line chart of top 5 countries, bar chart for metric comparison |

---

## 🎯 Key Features

- 🔄 **Dynamic filtering** by country, region, and rank
- 🧩 Multi-page layout using `st.page`
- 📈 Visuals built with **Matplotlib**, **Seaborn**, and **Plotly**
- 🌐 Interactive choropleth map
- 🧠 Insight boxes and summaries
- 💾 Efficient performance with `@st.cache_data`

---

## 🧪 How to Run the App

```
# Step 1: Clone the repo
In terminal write command
git init
git clone https://github.com/Safee-Ullah-Mughal/Interactive-Streamlit-Dashboard-for-World-Happiness-Exploration
cd Interactive-Streamlit-Dashboard-for-World-Happiness-Exploration

# Step 2: Install dependencies write next command:
pip install -r requirements.txt

# Step 3: Launch Streamlit
streamlit run app.py
```

Contributors
This project was built collaboratively by:

🧑 Safee Ullah Mughal – Page 1

🧑 Mohammad Noman – Page 2

🧑 Tehreem Baig – Page 3

🧑 Ayesha Ghaffar – Page 4

(Each member contributed via Git commits and pull requests.)

---

### Folder Structure

Interactive-Streamlit-Dashboard-for-World-Happiness-Exploration
│
├── data/                      # Dataset (2015.csv)
├── pages/                     # Streamlit pages
│   ├── 1_Country_Explorer.py
│   ├── 2_Regional_Filter.py
│   ├── 3_Global_Summary.py
│   └── 4_Top_Trends.py
│
├── app.py                     # Landing page
├── README.md                  # Project readme
├── requirements.txt           # Python dependencies

---

