import os
from collections import Counter

# Function to read all .txt files from a directory
def read_corpus(directory):
    corpus = ''
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
                corpus += file.read() + ' '  # Add a space between file contents
    return corpus

# Function to calculate tokens and types
def calculate_tokens_and_types(corpus):
    tokens = corpus.split()  # Split the corpus into words (tokens)
    types = set(tokens)  # Get unique words (types)
    return tokens, types

# # Function to calculate frequency of each type
def calculate_frequency(tokens):
    return Counter(tokens)

corpus_directory = 'corpus/'
corpus = read_corpus(corpus_directory)
tokens, types = calculate_tokens_and_types(corpus)
frequency = calculate_frequency(tokens)

print(f"Number of tokens: {len(tokens)}")
print(f"Number of types: {len(types)}")

print("Frequency of each type:")
for word, freq in frequency.items():
    print(f"{word}: {freq}")