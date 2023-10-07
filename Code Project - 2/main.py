## Importing ...
from nltk.sentiment import SentimentIntensityAnalyzer
import plotly.express as px
from datetime import datetime
from pathlib import Path
import streamlit as st
import glob


## Making variables
text_analyzer = SentimentIntensityAnalyzer()

## Making values for Plotly to read as x-axis and y-axis
dates = []
positivity = []
negativity = []

## Reading the diary entries' positivity and negativity as well as getting the date.
filepaths = glob.glob("diary\\*txt")
for filepath in filepaths:
    with open(filepath, "r", encoding="utf-8") as file:
        date = Path(filepath).stem
        date = datetime.strptime(date, "%Y-%m-%d")
        dates.append(date)
        diary_entry = file.read()
        positive = text_analyzer.polarity_scores(diary_entry)["pos"]
        negative = text_analyzer.polarity_scores(diary_entry)["neg"]
        negativity.append(negative)
        positivity.append(positive)
    print(positivity)
    print(diary_entry)

## Generating the plots
positivity_chart = px.line(x=dates, y=positivity,
                           labels={"x": "Dates", "y": "Positivity"})
negativity_chart = px.line(x=dates, y=negativity,
                           labels={"x": "Dates", "y": "Negativity"})


## Making the front end
st.title("Diary Tone")
st.subheader("Positivity")
st.plotly_chart(positivity_chart)

st.subheader("Negativity")
st.plotly_chart(negativity_chart)
