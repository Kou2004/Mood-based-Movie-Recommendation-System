# Mood-Based Movie Recommendation System

## Objective
The objective of this project is to develop a mood-based movie recommendation system that suggests movies or TV shows based on the user's current emotional state. The system leverages facial expressions, text inputs, and audio cues to determine the user's mood and provide personalized content recommendations.

## Features
1. **Face-Based Mood Detection**
   - Utilizes a Convolutional Neural Network (CNN) model.
   - Achieved 93% validation accuracy using the FER (Facial Emotion Recognition) dataset.
   - Detects emotions such as happiness, sadness, anger, and more from facial expressions.

2. **Text-Based Mood Detection**
   - Employs a Long Short-Term Memory (LSTM) model along with the Natural Language Toolkit (nltk).
   - Achieved 92% validation accuracy using the Emotion dataset.
   - Analyzes text inputs to identify the user's emotional state.

3. **Audio-Based Mood Detection**
   - Uses a Convolutional Neural Network (CNN) model in combination with the Librosa library for audio analysis.
   - Utilizes combined TFDS  and RAVDESS (Ryerson Audio-Visual Database of Emotional Speech and Song) datasets.
   - Analyzes audio inputs to detect emotions from the user's voice.

4. **Chatbot Integration**
   - Integrates face, text, and audio-based mood detection into a chatbot interface.
   - Provides an interactive experience where users can communicate with the chatbot through multiple input modalities.

5. **Movie/TV Show Recommendation**
   - Uses web scraping with Beautiful Soup to gather data from IMDb, including movie descriptions and posters.
   - Applies K-means clustering along with the elbow method to group movies and TV shows into clusters based on emotions.
   - Utilizes WordCloud to visualize the distribution of words within the clusters.
   - Recommends the top 10 movies or TV shows to the user based on their detected mood.

## Implementation Details
### Face-Based Mood Detection
- **Model**: Convolutional Neural Network (CNN)
- **Dataset**: FER (Facial Emotion Recognition)
- **Accuracy**: 93% validation accuracy

### Text-Based Mood Detection
- **Model**: Long Short-Term Memory (LSTM)
- **Libraries**: Natural Language Toolkit (nltk)
- **Dataset**: Emotion dataset
- **Accuracy**: 92% validation accuracy

### Audio-Based Mood Detection
- **Model**: Convolutional Neural Network (CNN)
- **Library**: Librosa for audio processing
- **Datasets**: Combined TFDS and RAVDESS datasets

### Web Scraping
- **Tool**: Beautiful Soup
- **Purpose**: Gather movie descriptions, posters, and other relevant data from IMDb

### Clustering
- **Method**: K-means clustering with the elbow method
- **Visualization**: WordCloud to see genre distribution in emotion clusters

### Recommendation System
- **Approach**: Recommend top 10 movies or TV shows to the user based on their detected mood from facial expressions, text inputs, or audio cues.

## Challenges
1. **Clustering Movies into Different Emotions**:
   - Grouping movies and TV shows into distinct emotional clusters was challenging due to the subjective nature of emotions and the variety of content available.
   
2. **Handling Different Sets of Labeled Moods**:
   - Integrating various datasets with different emotion labels required careful handling and mapping to a common set of labels to ensure consistency.

3. **Efficient Dataset Collection and Model Selection**:
   - Identifying and sourcing efficient datasets, as well as selecting and training appropriate models for each modality, was crucial for achieving high accuracy.

4. **Hyperparameter Tuning**:
   - Fine-tuning the hyperparameters for each model to optimize performance and achieve the best results was a significant challenge.

## Improvements
1. **Testing with More Models**:
   - Experimenting with additional models in each category (face, text, audio) and exploring different architectures and techniques to improve accuracy.

2. **Parameter Optimization**:
   - Continuously playing with different parameters and hyperparameters to enhance model performance.

3. **Data Collection**:
   - Gathering more diverse and comprehensive datasets to improve the robustness and generalizability of the system.

## Contributors
- **Kousik Kumar Barnwal** (Chemical Engineering, 2nd year, IIT Roorkee)
- **Mrityunjay Singh** (Electrical Engineering, 2nd year, IIT Roorkee)
