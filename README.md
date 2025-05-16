# Interactive-Streamlit-Dashboard-for-World-Happiness-Exploration

An **interactive multi-page Streamlit web app** for exploring global happiness metrics based on the **2015 World Happiness Report**. Built with Python, the dashboard provides insights at country, regional, and global levels.

---

## 📊 Project Overview

This dashboard allows users to explore the **World Happiness Report (2015)** dataset through rich, interactive visualizations.  
It features a **multi-page layout**, enabling deep dives into:

- Country-specific metrics
- Regional comparisons
- Global summaries and trends

> Developed as part of an academic project, fulfilling all requirements such as interactive filters, multiple data visualizations, and page-wise separation.

---

## 🗂️ Dataset Details

- **Source**: [Kaggle – World Happiness Report](https://www.kaggle.com/datasets/unsdsn/world-happiness)
- **Year**: 2015
- **Features Included**:
  - Happiness Score  
  - GDP per Capita  
  - Health (Life Expectancy)  
  - Family  
  - Freedom  
  - Generosity  
  - Trust in Government  

---

## 🧭 App Navigation (Pages)

| Page | Title                     | Key Features                                                                 |
|------|---------------------------|------------------------------------------------------------------------------|
| 1️⃣   | Country Explorer          | Text input, slider, bar chart of happiness factors, filtered countries       |
| 2️⃣   | Regional Filter           | Selectbox, box plot of scores, scatter plot for metric vs happiness          |
| 3️⃣   | Global Summary            | Choropleth world map, animated map, correlation heatmap                      |
| 4️⃣   | Top Performers & Trends  | Line chart for top 5 countries, bar chart for metric comparisons             |

---

## 🎯 Key Features

- 🔄 Dynamic filtering by country, region, and rank  
- 🧩 Multi-page layout using `st.page`  
- 📈 Visualizations built with **Matplotlib**, **Seaborn**, and **Plotly**  
- 🌐 Interactive **choropleth map**  
- 💡 Summary insights and comparison stats  
- 💾 Efficient data loading with `@st.cache_data`  

---

## 🧪 How to Run the App

### Step 1: Clone the Repository
```bash
git init
git clone https://github.com/Safee-Ullah-Mughal/Interactive-Streamlit-Dashboard-for-World-Happiness-Exploration
cd Interactive-Streamlit-Dashboard-for-World-Happiness-Exploration
```
### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```
### Step 3: Launch the Streamlit App
```bash
streamlit run app.py
```

## 👥 Contributors
This project was built collaboratively as part of a group academic assignment:

🧑 Safee Ullah Mughal – Page 1: Country Explorer
🧑 Muhammad Noman – Page 2: Regional Filter
🧑 Tehreem Baig – Page 3: Global Summary
🧑 Ayesha Ghaffar – Page 4: Top Performers & Trends

All contributions were made via GitHub commits and pull requests.

## 📁 Project Structure

```bash
world-happiness-dashboard/
│
├── data/                      # Dataset (2015.csv)
│
├── pages/                    # Streamlit multi-page app components
│   ├── 1_Country_Explorer.py
│   ├── 2_Regional_Filter.py
│   ├── 3_Global_Summary.py
│   └── 4_Top_Trends.py
│
├── app.py                    # Main entry point (landing page)
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

💬 For feedback or contributions, feel free to fork and submit a pull request!