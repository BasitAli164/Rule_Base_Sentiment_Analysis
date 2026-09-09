# Simple Sentiment Analysis

A simple rule-based sentiment analysis application built with Streamlit.

## Features

- Enter a sentence
- Detect positive words
- Detect negative words
- Classify the sentence as:
  - Positive
  - Negative
  - Neutral
- Display positive and negative word counts

## How It Works

The application uses predefined lists of positive and negative words.

The entered sentence is converted to lowercase and split into words.

If the sentence contains more positive words than negative words, it is classified as Positive.

If it contains more negative words than positive words, it is classified as Negative.

If both scores are equal, it is classified as Neutral.

## Technologies

- Python
- Streamlit
- Rule-Based Sentiment Analysis

## Run Locally

Install the required package:

```bash
pip install -r requirements.txt
