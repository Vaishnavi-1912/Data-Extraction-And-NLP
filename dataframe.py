import pandas as pd
import nltk
nltk.download('stopwords')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
import math
import os

# Function to read words from a text file
def read_words(file_path):
    with open(file_path, 'r', encoding='latin-1') as file:
        words = [line.strip() for line in file]
    return set(words)

# Function to calculate positive score
def calculate_positive_score(text, positive_words):
    tokenized_words = word_tokenize(text.lower())
    positive_tokens = [word for word in tokenized_words if word in positive_words]
    return len(positive_tokens)

# Function to calculate negative score
def calculate_negative_score(text, negative_words):
    tokenized_words = word_tokenize(text.lower())
    negative_tokens = [word for word in tokenized_words if word in negative_words]
    return len(negative_tokens)

# Function to calculate polarity score
def calculate_polarity_score(positive_score, negative_score):
    if positive_score + negative_score == 0:
        return 0
    return (positive_score - negative_score) / (positive_score + negative_score)

# Function to calculate subjectivity score
def calculate_subjectivity_score(positive_score, negative_score, word_count):
    if word_count == 0:
        return 0
    return (positive_score + negative_score) / word_count

# Function to calculate average sentence length
def calculate_avg_sentence_length(text):
    sentences = sent_tokenize(text)
    return sum(len(word_tokenize(sentence)) for sentence in sentences) / len(sentences)

# Function to calculate percentage of complex words
def calculate_percentage_of_complex_words(text, complex_words):
    tokenized_words = word_tokenize(text.lower())
    total_words = len(tokenized_words)
    complex_word_count = sum(1 for word in tokenized_words if word in complex_words)
    if total_words == 0:
        return 0
    return complex_word_count / total_words * 100

# Function to calculate Fog index
def calculate_fog_index(avg_sentence_length, percentage_of_complex_words):
    return 0.4 * (avg_sentence_length + percentage_of_complex_words)

# Function to calculate average number of words per sentence
def calculate_avg_number_of_words_per_sentence(text):
    sentences = sent_tokenize(text)
    return sum(len(word_tokenize(sentence)) for sentence in sentences) / len(sentences)

# Function to calculate complex word count
def calculate_complex_word_count(text, complex_words):
    tokenized_words = word_tokenize(text.lower())
    return sum(1 for word in tokenized_words if word in complex_words)

# Function to calculate word count
def calculate_word_count(text):
    return len(word_tokenize(text))

# Function to calculate syllables per word
# Function to calculate syllables per word
def calculate_syllables_per_word(text):
    tokenized_words = word_tokenize(text.lower())
    syllable_count = 0
    for word in tokenized_words:
        vowels = 'aeiouy'
        word = word.lower().strip(".:;?!")
        if len(word) == 0:  # Check if word is empty
            continue
        if word[0] in vowels:
            syllable_count += 1
        for index in range(1, len(word)):
            if word[index] in vowels and word[index - 1] not in vowels:
                syllable_count += 1
        if word.endswith('e'):
            syllable_count -= 1
        if word.endswith('le') and len(word) > 2 and word[-3] not in vowels:
            syllable_count += 1
        if syllable_count == 0:
            syllable_count += 1
    return syllable_count / len(tokenized_words)


# Function to calculate personal pronouns count
def calculate_personal_pronouns(text):
    tokenized_words = word_tokenize(text.lower())
    personal_pronouns = ['i', 'me', 'my', 'mine', 'myself', 'you', 'your', 'yours', 'yourself',
                         'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself',
                         'it', 'its', 'itself', 'we', 'us', 'our', 'ours', 'ourselves',
                         'you', 'your', 'yours', 'yourselves', 'they', 'them', 'their',
                         'theirs', 'themselves']
    return sum(word in personal_pronouns for word in tokenized_words)

# Function to calculate average word length
def calculate_avg_word_length(text):
    tokenized_words = word_tokenize(text.lower())
    return sum(len(word) for word in tokenized_words) / len(tokenized_words)

# Read positive and negative words
positive_words = read_words('positive-words.txt')
negative_words = read_words('negative-words.txt')

# Read stop words
stop_words = set(stopwords.words('english'))
stopwords_files = ['StopWords_Auditor.txt', 'StopWords_Currencies.txt',
                   'StopWords_DatesandNumbers.txt', 'StopWords_Geographic.txt',
                   'StopWords_Names.txt', 'StopWords_Generic.txt', 'StopWords_GenericLong.txt']
for file in stopwords_files:
    stop_words.update(read_words(file))

# Read complex words
complex_words = set()
with open('StopWords_GenericLong.txt', 'r', encoding='latin-1') as file:
    for line in file:
        words = line.strip().split()
        complex_words.update(words)

extracted_text_directory = 'C:\\Users\\DeLL\\PycharmProjects\\blackCoffer\\exracted_texts\\'

# Calculate variables for each extracted text file
results = []
for filename in os.listdir(extracted_text_directory):
    file_path = os.path.join(extracted_text_directory, filename)
    with open(file_path, 'r', encoding='latin-1') as file:
        text = file.read()

# Calculate variables
positive_score = calculate_positive_score(text, positive_words)
negative_score = calculate_negative_score(text, negative_words)
polarity_score = calculate_polarity_score(positive_score, negative_score)
subjectivity_score = calculate_subjectivity_score(positive_score, negative_score, calculate_word_count(text))
avg_sentence_length = calculate_avg_sentence_length(text)
percentage_of_complex_words = calculate_percentage_of_complex_words(text, complex_words)
fog_index = calculate_fog_index(avg_sentence_length, percentage_of_complex_words)
avg_number_of_words_per_sentence = calculate_avg_number_of_words_per_sentence(text)
complex_word_count = calculate_complex_word_count(text, complex_words)
word_count = calculate_word_count(text)
syllable_per_word = calculate_syllables_per_word(text)
personal_pronouns = calculate_personal_pronouns(text)
avg_word_length = calculate_avg_word_length(text)

# Create DataFrame
output_df = pd.DataFrame({
    '1. POSITIVE SCORE': [positive_score],
    '2. NEGATIVE SCORE': [negative_score],
    '3. POLARITY SCORE': [polarity_score],
    '4. SUBJECTIVITY SCORE': [subjectivity_score],
    '5. AVG SENTENCE LENGTH': [avg_sentence_length],
    '6. PERCENTAGE OF COMPLEX WORDS': [percentage_of_complex_words],
    '7. FOG INDEX': [fog_index],
    '8. AVG NUMBER OF WORDS PER SENTENCE': [avg_number_of_words_per_sentence],
    '9. COMPLEX WORD COUNT': [complex_word_count],
    '10. WORD COUNT': [word_count],
    '11. SYLLABLE PER WORD': [syllable_per_word],
    '12. PERSONAL PRONOUNS': [personal_pronouns],
    '13. AVG WORD LENGTH': [avg_word_length]
})

# Write to Excel
output_df.to_excel('output_data_structure.xlsx', index=False)

