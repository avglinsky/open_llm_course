import re
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer

# Sample documents
documents = [
    "The cat sat on the mat.",
    "The dog sat on the log!"
]

# Custom preprocessing function
def custom_preprocessor(text):
    # Приведение к нижнему регистру
    text = text.lower()
    # Удаление пунктуации
    text = re.sub(r'[^\w\s]', '', text)
    return text

# Create the Bag of Words model with the custom preprocessor
vectorizer = CountVectorizer(preprocessor=custom_preprocessor)
bow_matrix = vectorizer.fit_transform(documents)

# Convert to array for easy viewing
print(bow_matrix.toarray())

# Display the vocabulary
print(vectorizer.get_feature_names_out())

# Get feature names (words)
vocabulary = vectorizer.get_feature_names_out()

# Create a key-value map (word to index)
word_to_index = {word: idx for idx, word in enumerate(vocabulary)}

# Print the key-value map
print("Word to Index Map:")
for word, idx in word_to_index.items():
    print(f"{word}: {idx}")


one_hot_vectors = vectorizer.transform(documents[0].split()).toarray()

print(one_hot_vectors)

# Суммируем векторы
final_vector = np.sum(one_hot_vectors, axis=0)

from manim import *

class OneHotEncodingScene(Scene):
    def construct(self):
        # Устанавливаем шрифт по умолчанию
        self.font = "Alegreya Sans Medium"

        # Define the words and their corresponding one-hot encodings
        words = documents[0].split()

        # Create and display vectors as text objects
        vectors = []
        for i, (word, vector) in enumerate(zip(words, one_hot_vectors)):
            vector_text = Text(f"{word}: {vector}", font_size=24, font=self.font)
            vector_text.to_edge(UP).shift(DOWN * i)
            vectors.append(vector_text)
            self.play(Write(vector_text))

        # Pause for a moment before moving
        self.wait(1)

        # Animate moving all vectors downwards to form the final document vector
        n = len(vectors)
        for i, vector_text in enumerate(vectors):
            self.play(vector_text.animate.shift(DOWN * (n - i)))
            self.wait(1)
            self.play(FadeOut(vector_text))
            center_coords = vector_text.get_center()
            new_text = Text("Summing up", font_size=24, font="Alegreya Sans Medium")
            new_text.move_to(center_coords)
            self.play(Write(new_text))
            self.play(FadeOut(new_text))

        # Create the final document vector
        final_vector_text = Text(f"Document Vector: {final_vector}", font_size=30, font=self.font)
        final_vector_text.to_edge(DOWN)

        # Show the final document vector
        self.play(Write(final_vector_text))

        # Hold the final scene for a few seconds
        self.wait(3)
