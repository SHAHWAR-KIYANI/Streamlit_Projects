import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from wordcloud import WordCloud, STOPWORDS


st.title("Sentiment Analysis of Tweets About US Airlines")
st.markdown("This Application is a Streamlit Dashboard used to Analyze Sentiments of Tweets  ")
st.sidebar.title("Sentiment Analysis of Tweets")
st.sidebar.markdown("This Application is a Streamlit Dashboard used to Analyze Sentiments of Tweets  ")
st.sidebar.write("__________")

data_url = "C:\\Users\Shahwar\Desktop\Streamlit_Projects\Project_3_SentimentAnalysisOfTweets\Tweets.csv"

@st.cache_data
def load_data():
    loaded_data = pd.read_csv(data_url)
    loaded_data["tweet_created"] = pd.to_datetime(loaded_data["tweet_created"])
    return loaded_data

tweets_df = load_data()

st.sidebar.markdown("### Show Random Sentiment Based Tweet")
sentiment = st.sidebar.radio("Select any One Sentiment:",("Positive","Neutral","Negative")).lower()
st.sidebar.markdown(tweets_df.query('airline_sentiment==@sentiment')[["text"]].sample(n=1).iat[0,0])
st.sidebar.write("__________")

st.write("__________")
st.sidebar.markdown("### Number of Tweets by Sentiment")
select = st.sidebar.selectbox("Visualization Type:",["Histogram","Pie Chart"],key="1")
sentiment_count = tweets_df["airline_sentiment"].value_counts()
sentiment_count = pd.DataFrame({"Sentiment":sentiment_count.index,"Tweets":sentiment_count.values})

if not st.sidebar.checkbox("Hide",False):
    st.markdown("### Number of Tweets by Sentiment")
    if select == "Histogram":
        figure_for_histogram = px.bar(sentiment_count, x="Sentiment", y="Tweets", color="Tweets",height=500)
        st.plotly_chart(figure_for_histogram)
    else:
        figure_for_PieChart = px.pie(sentiment_count, values="Tweets", names="Sentiment")
        st.plotly_chart(figure_for_PieChart)
st.sidebar.write("__________")

st.sidebar.markdown("### Where and When Do Users Tweet?")
hour = st.sidebar.slider("Hour of the Day", 0, 23)
modified_data = tweets_df[tweets_df["tweet_created"].dt.hour == hour]
if not st.sidebar.checkbox("Close", False, key = "2"):
    st.write("__________")
    st.markdown("### Tweets Location Based on Tome of The Day")
    st.markdown("%i Tweets between %i:00 and %i:00" % (len(modified_data), hour, (hour + 1) % 24) )
    st.map(modified_data)
if st.sidebar.checkbox("Show Raw Data for Mapped Tweets", True):
        st.markdown("### Show Raw Data for Mapped Tweets")
        st.write(modified_data)

st.sidebar.write("__________")
st.write("__________")

st.sidebar.subheader("Breakdown of Tweets by Airlines")
choice = st.sidebar.multiselect("Pick Airlines",("US Airways","United","American","Southwest","Delta","Virgin America"),key="3")
if len(choice) > 0:
    choice_data = tweets_df[tweets_df.airline.isin(choice)]
    fig_choice = px.histogram(choice_data, x="airline", y="airline_sentiment", histfunc="count", color="airline_sentiment", facet_col="airline_sentiment", labels={"airline_sentiment":"Tweets"}, height=600, width=800)
    st.markdown("### Breakdown of Tweets by Airlines")
    st.plotly_chart(fig_choice)

st.sidebar.write("__________")

st.sidebar.header("Word Cloud")
word_sentiment = st.sidebar.radio("Display Word Cloud for which Sentiment?",("Positive","Neutral","Negative")).lower()
if not st.sidebar.checkbox("Close",False,key="4"):
    st.header(f"Word Cloud for {word_sentiment.capitalize()} Sentiment")
    df = tweets_df[tweets_df["airline_sentiment"]==word_sentiment]
    words = " ".join(df["text"])
    processed_words = " ".join([word for word in words.split() if "http" not in word and not word.startswith("@") and word != "RT"])
    wordcloud = WordCloud(stopwords=STOPWORDS, background_color="white", width=800, height=640).generate(processed_words)
    fig, ax = plt.subplots()
    ax.imshow(wordcloud)
    ax.set_xticks([])
    ax.set_yticks([])
    st.pyplot(fig)

st.write("__________")