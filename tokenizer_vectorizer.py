import tensorflow as tf
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences

tokenizer=Tokenizer()

def tok_vectorizer(text):
  test_sequences = tokenizer.texts_to_sequences(text)
  X_test_padded = pad_sequences(test_sequences, maxlen=35)
  return X_test_padded