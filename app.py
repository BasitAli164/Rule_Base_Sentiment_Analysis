import streamlit as st

# Positive words
positive_words = [
    "good",
    "great",
    "excellent",
    "amazing",
    "awesome",
    "love",
    "like",
    "happy",
    "wonderful",
    "best",
    "fantastic",
    "nice",
    "beautiful"
]

# Negative words
negative_words = [
    "bad",
    "worst",
    "terrible",
    "horrible",
    "hate",
    "sad",
    "angry",
    "poor",
    "awful",
    "disappointed",
    "dislike",
    "ugly"
]


def analyze_sentiment(sentence):
    words = sentence.lower().split()

    positive_score = 0
    negative_score = 0

    for word in words:
        word = word.strip(".,!?;:")

        if word in positive_words:
            positive_score += 1

        if word in negative_words:
            negative_score += 1

    if positive_score > negative_score:
        sentiment = "Positive"
    elif negative_score > positive_score:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return sentiment, positive_score, negative_score


# Page configuration
st.set_page_config(
    page_title="Simple Sentiment Analysis",
    page_icon="💬",
    layout="centered"
)

# Application title
st.title("💬 Simple Sentiment Analysis")

st.write(
    "Enter a sentence and the application will classify it "
    "as Positive, Negative, or Neutral."
)

# Input
sentence = st.text_input(
    "Enter your sentence:",
    placeholder="Example: I love this application"
)

# Analyze button
if st.button("Analyze Sentiment"):

    if not sentence.strip():
        st.warning("Please enter a sentence.")

    else:
        sentiment, positive_score, negative_score = analyze_sentiment(sentence)

        st.subheader("Result")

        if sentiment == "Positive":
            st.success("Sentiment: Positive")

        elif sentiment == "Negative":
            st.error("Sentiment: Negative")

        else:
            st.info("Sentiment: Neutral")

        st.write(f"Positive words found: {positive_score}")
        st.write(f"Negative words found: {negative_score}")
