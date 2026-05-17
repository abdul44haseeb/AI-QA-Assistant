import streamlit as st
import pandas as pd
import os
import json
import matplotlib.pyplot as plt

from app.analyzer import analyze_conversation

# =====================================
# PAGE SETTINGS
# =====================================

st.set_page_config(
    page_title="AI QA Dashboard",
    layout="wide"
)

# =====================================
# REPORTS FOLDER
# =====================================

REPORTS_FOLDER = "reports"

# =====================================
# PAGE TITLE
# =====================================

st.title("AI QA Assistant Dashboard")

# =====================================
# SIDEBAR FILTERS
# =====================================

st.sidebar.header("Filters")

# =====================================
# FILE UPLOAD SECTION
# =====================================

st.subheader("Upload Customer Transcript")

uploaded_file = st.file_uploader(
    "Upload a .txt transcript file",
    type=["txt"]
)

if uploaded_file is not None:

    transcript = uploaded_file.read().decode("utf-8")

    st.text_area(
        "Transcript Preview",
        transcript,
        height=200
    )

    if st.button("Analyze Transcript"):

        with st.spinner("Analyzing transcript with AI..."):

            # Analyze transcript
            analysis_data, raw_response = analyze_conversation(
                transcript
            )

            # Generate report file name
            report_name = uploaded_file.name.replace(
                ".txt",
                "_report.json"
            )

            report_path = os.path.join(
                REPORTS_FOLDER,
                report_name
            )

            # Save report JSON
            with open(
                report_path,
                "w",
                encoding="utf-8"
            ) as report_file:

                json.dump(
                    analysis_data,
                    report_file,
                    indent=4
                )

            st.success(
                "Analysis completed successfully!"
            )

            # Show JSON result
            st.json(analysis_data)

# =====================================
# LOAD REPORT FILES
# =====================================

report_files = [
    file for file in os.listdir(REPORTS_FOLDER)
    if file.endswith(".json")
]

all_reports = []

# =====================================
# READ EACH REPORT
# =====================================

for file_name in report_files:

    file_path = os.path.join(
        REPORTS_FOLDER,
        file_name
    )

    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as file:

        data = json.load(file)

        all_reports.append({

            "File Name":
            file_name,

            "Sentiment":
            data["customer_sentiment"].capitalize(),

            "Empathy Score":
            data["empathy_score"],

            "Professionalism Score":
            data["professionalism_score"],

            "Summary":
            data["summary"]
        })

# =====================================
# CREATE DATAFRAME
# =====================================

df = pd.DataFrame(all_reports)

# =====================================
# SENTIMENT FILTER
# =====================================

selected_sentiment = st.sidebar.selectbox(
    "Select Sentiment",
    ["All"] + list(df["Sentiment"].unique())
)

# Apply filter
if selected_sentiment != "All":

    df = df[
        df["Sentiment"] == selected_sentiment
    ]

# =====================================
# SHOW DATAFRAME
# =====================================

st.subheader("QA Analysis Reports")

st.dataframe(
    df,
    width="stretch"
)

# =====================================
# METRICS SECTION
# =====================================

st.subheader("Overall Metrics")

avg_empathy = df["Empathy Score"].mean()

avg_professionalism = df[
    "Professionalism Score"
].mean()

col1, col2 = st.columns(2)

with col1:

    st.metric(
        "Average Empathy Score",
        round(avg_empathy, 2)
    )

with col2:

    st.metric(
        "Average Professionalism Score",
        round(avg_professionalism, 2)
    )

# =====================================
# ANALYTICS CHARTS
# =====================================

st.subheader("Analytics Charts")

# Create aligned columns
chart1, chart2 = st.columns(
    [1, 1],
    vertical_alignment="top"
)

# =====================================
# BAR CHART
# =====================================

with chart1:

    fig, ax = plt.subplots(
        figsize=(5, 3)
    )

    scores = {
        "Empathy": avg_empathy,
        "Professionalism": avg_professionalism
    }

    ax.bar(
        scores.keys(),
        scores.values()
    )

    ax.set_title(
        "Average QA Scores"
    )

    ax.set_ylim(0, 10)

    plt.tight_layout()

    st.pyplot(fig)

# =====================================
# PIE CHART
# =====================================

with chart2:

    sentiment_counts = (
        df["Sentiment"]
        .value_counts()
    )

    fig2, ax2 = plt.subplots(
        figsize=(5, 3)
    )

    ax2.pie(
        sentiment_counts,
        labels=sentiment_counts.index,
        autopct="%1.1f%%"
    )

    ax2.axis("equal")

    ax2.set_title(
        "Customer Sentiment Distribution"
    )

    plt.tight_layout()

    st.pyplot(fig2)