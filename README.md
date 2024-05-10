# Mood-based-Movie-Recommendation-System
The Mood-Based Movie Recommendation System is designed to provide personalized movie recommendations tailored to the user's current mood. It employs natural language processing (NLP) techniques to analyze text input, such as chat messages or social media posts, and audio processing to interpret the user's tone and emotions.

**Approach**

1. We first analyzed the IMDB movie dataset , on the basis of that we have selected most prefered 6 genres and mapped the movies accordingly.
2. For text based mood recognizer , we first apply NLTK tokenizer and vectorizer , to convert the text into numbers , then used LSTM to do this multiclassification task.
3. For audio, we first applied data augmentation on the audio to generate different types of audio using noise injection, shifting, streching and changing the pitch. We also extract the useful features from the audio using the library librosa like MFCC, chroma shift. Finally used CNN to do the classification.

**Performance**

The following table summarizes the accuracy scores achieved by different models used in the Mood-Based Movie Recommendation System:

| Model             | Accuracy |
|-------------------|----------|
| Text-based-mood-recognizer  | 0.92    |
| Audio-based mood recognizer    | 0.99    |

**Challenges**

1. Mapping of the mood to type of movies.
2. Feature extraction from the audio.
3. Choosing of right model and the choosing the right hyperparameters.

**Improvements**

We are planning to add face based mood recognition as well. Try to introduce more genres for more robust movie recommendation system.

**Contributors**
1. Mrityunjay Singh, 2nd year, EE, IIT Roorkee
2. Kousik Kumar Barnwal, 2nd year, CH, IIT Roorkee
   
