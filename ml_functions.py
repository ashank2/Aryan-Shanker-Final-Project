#-------------------------------------------------------
# Machine Learning Library Stack & Analytics Functions:
#-------------------------------------------------------
# pandas: For data manipulation and analysis, especially for Tabular Data. 
import pandas as pd

# numpy: For efficient numerial computations.
import numpy as np

# scikit-learn: For classic machine learning algorithms, model selection, and pre-processing.
from sklearn.model_selection import train_test_split 
# To split data into training and testing sets for predictions.

from sklearn.ensemble import RandomForestClassifier
# For building a random forest classifier.

from sklearn.naive_bayes import MultinomialNB
# For text classification (for future use, not implemented yet). 

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
# For text feature extraction (for future use, not implemented yet).

from sklearn.metrics import classification_report, accuracy_score
# For evaluating ML models. 

# matplotlib: For visualizing data and results (ex: in chart & graphical forms).
import matplotlib.pyplot as plt

from textblob import TextBlob
#  

#-------------------------------
# AI-Based Analytical Functions:
#-------------------------------

def recommend_greener_mode(distance_km, current_mode):
    """
    Suggest a greener or more efficient mode of transport to the user based on
    distance travelled and choice of mode of transportation. 

    distance_km (float): Distance of the user's trip in kilometres.
    current_mode (str): The user's chosen mode of transportation.

    Returning a simple, and effective recommendation message for the user.
    """
    if distance_km <2:
        if current_mode != "walk":
            return "For short trips undr 2km, consider walking for zero carbon emission emiitance and for superior health benefits!"
        
    if distance_km < 5:
        if current_mode not in ["walk", "bike"]: 
            return "For trips under 5km, biking is a nicer, eco-friendlier option. What's better than experiencing nature itself? :)"
    
    if current_mode == "car":
        return "Consider public transport or carpooling with a friend to reduce your carbon footprint." 
    
    return "Great choice! Keep using low-emission transport when possible! :)"
    
def summarize_user_trips(trip_df):
    """
    Summarizes a user's trip history, showing total distance travelled, total emissions,
    and most common mode of transport taken. As a result, conducting trip analytics for the user using
    python's pandas library.



    trip_df (pd.DataFrame): DataFrame with columns: ['date', 'distance_km', 'mode', 'emissions_kg'].

    Returning a dictionary with summary statistics for the user!
    """
    total_distance = trip_df['distance_km'].sum()
    total_emissions = trip_df['emissions_kg'].sum()
    most_common_mode = trip_df['mode'].mode()[0] if not trip_df['mode'].empty else None

    summary = {
        "total_distance_km": total_distance,
        "total_emissions_kg": total_emissions,
        "most_common_mode": most_common_mode,
        "trip_count": len(trip_df)
    }
    return summary

def plot_emissions_over_time(trip_df):
    """
    Plotting the user's emissions over time. As a result, using matplotlib for data visualization.

    trip_df (pd.DataFrame): DataFrame with columns: ['date', 'distance_km', 'mode', 'emissions_kg'].
    """

    plt.figure(figsize=(8, 4))
    plt.plot(trip_df['date'], trip_df['emissions_kg'], marker='o')
    plt.title('Your Carbon Emissions Over Time!')
    plt.xlabel('Date')
    plt.ylabel('Emissions (kg of CO2 Emitted)')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def predict_mode(trip_df):
    """
    Training a classifier to predict mode of transport to use based on distance, for users.

    trip_df (pd.DataFrame): DataFrame with columns: ['distance_km' and 'mode'].

    Returning a model: Trained scikit-learn classifier.

    """
    X = trip_df[['distance_km']]
    y = trip_df['mode']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    clf = RandomForestClassifier(n_estimators=50, random_state=42)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)

    print("Prediction Accuracy:", accuracy_score(y_test, y_pred))
    print(classification_report(y_test, y_pred))
    return clf

def analyze_user_commute_feedback(feedback_list, top_n=5):
    """
    Analyzes user's commute routines (once they input their daily commutes).

    TextBlob for Sentiment Analysis, CountVectorizer for Word Frequency and TfidVectorizer for Word Importance.

    feedback_list (list of str): List of user comments.
    top_n (int): Number of top words used by user.

    Returning a list of dictionaries containing sentiment results for each daily commute routine inputted by the user. 
    """

    #-----Sentiment Analysis (TextBlob)-----
    sentiment_results = []
    for feedback in feedback_list:
        blob = TextBlob(feedback)
        polarity = blob.sentiment.polarity 
        if polarity > 0.1:
            sentiment = 'positive'
        elif polarity < -0.1:
            sentiment = 'negative'
        else:
            sentiment = 'neutral'
        sentiment_results.append({
            'feedback': feedback,
            'polarity': polarity,
            'sentiment': sentiment,
        })
    
     #-----Most Common Words (CountVectorizer)-----
    count_vect = CountVectorizer(stop_words='english')
    X_counts = count_vect.fit_transform(feedback_list)
    word_counts = np.asarray(X_counts.sum(axis=0)).flatten()
    vocab = np.array(count_vect.get_feature_names_out())
    top_indices = word_counts.argsort()[::-1][:top_n]

    print(f"\nTop {top_n} most common words (CountVectorizer):")
    for idx in top_indices:
        print(f"{vocab[idx]}: {int(word_counts[idx])}")

    #-----Most Important Words (TfidVectorizer)-----
    tfidf_vect = TfidfVectorizer(stop_words='english')
    X_tfidf = tfidf_vect.fit_transform(feedback_list)
    tfidf_scores = np.asarray(X_tfidf.mean(axis=0)).flatten()
    vocab_tfidf = np.array(tfidf_vect.get_feature_names_out())
    top_tfidf_indices = tfidf_scores.argsort()[::-1][:top_n]

    print(f"\nTop {top_n} most important words (TF-IDF):")
    for idx in top_tfidf_indices:
        print(f"{vocab_tfidf[idx]}: {tfidf_scores[idx]:.3f}")

    #-----Print Sentiment Analysis Results-----
    print("\nSentiment Analysis For Each User's Commute Feedback:")
    for result in sentiment_results:
        print(f"Feedback: {result['feedback']}\nSentiment:{result['sentiment']} (Polarity: {result['polarity']:.2f})\n")

    return sentiment_results

def save_user_trips_to_csv(trip_df, filename='user_trips.csv'):
    """
    Saves the user's trip DataFrame to a CSV file.

    trip_df (pd.DataFrame): DataFrame with user's trip data.
    filename (str): Name of the CSV file to save a user's data to.

    No returns - this function is to save user data for user's to see their analytics
    over time. 
    """
    trip_df.to_csv(filename, index=False)
    print(f"User trips saved to {filename}")

def load_user_trips_from_csv(filename='user_trips.csv'):
    """
    Loads the user's trip data from a CSV file into a DataFrame.

    filename (str): Name of the CSV file to load data from. 

    Returning a pd.DataFrame: The DataFrame with user trip data.
    """
    try:
        trip_df = pd.read_csv(filename)
        print(f"User trips loaded from {filename}")
        return trip_df
    
    except FileNotFoundError:
        print(f"No saved trip data found at {filename}.")

        # Return an empty DataFrame with expected columns, for consistency:
        columns = ['date', 'distance_km', 'mode', 'emissions_kg']
        return pd.DataFrame(columns=columns)
    
def main():
    """
    Main testing function to showcase all ML and analytics functions above.
    Utilzing sample trip data and user commute feedback data, to run all functions.
    """
    #----Sample Trip Data----
    trip_data = [
        {'date': '2025-05-01', 'distance_km': 1.5, 'mode': 'car', 'emissions_kg': 0.35},
        {'date': '2025-05-02', 'distance_km': 4.0, 'mode': 'bike', 'emissions_kg': 0.0},
        {'date': '2025-05-03', 'distance_km': 10.0, 'mode': 'car', 'emissions_kg': 1.7},
        {'date': '2025-05-04', 'distance_km': 2.2, 'mode': 'walk', 'emissions_kg': 0.0},
        {'date': '2025-05-05', 'distance_km': 6.0, 'mode': 'bus', 'emissions_kg': 0.6},
    ]
    trip_df = pd.DataFrame(trip_data)

    #----Sample User Feedback----
    feedback = [
        "I love biking back home after work, it's super healthy and relaxing.",
        "The bus was late and very crowded today.",
        "Walking in the morning is very refreshing.",
        "Driving in traffic is stressful.",
        "I wish there were more bike lanes downtown."
    ]

    print("\n----Testing recommend_greener_mode----")
    print(recommend_greener_mode(1.5, 'car'))
    print(recommend_greener_mode(4.0, 'bike'))
    print(recommend_greener_mode(10.0, 'car'))
    print(recommend_greener_mode(2.2, 'walk'))
    print(recommend_greener_mode(6.0, 'bus'))

    print("\n----Testing summarize_user_trips----")
    summary = summarize_user_trips(trip_df)
    print(summary)

    print("\n----Testing plot_emissions_over_time----")
    plot_emissions_over_time(trip_df)

    print("\n----Testing predict_mode----")
    model = predict_mode(trip_df)

    print("\n----Testing analyze_user_commute_feedback")
    analyze_user_commute_feedback(feedback, top_n=3)

    print("\n----Testing save & load user trips----")
    save_user_trips_to_csv(trip_df, filename='test_user_trips.csv')
    loaded_df = load_user_trips_from_csv(filename='test_user_trips.csv')
    print(loaded_df)

if __name__ == "__main__":
    main()

