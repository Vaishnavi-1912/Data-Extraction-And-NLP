import pandas as pd
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize, sent_tokenize
from textblob import TextBlob
import os

# Step 1: Read extracted text files
# Assuming you have a list of file paths containing the extracted text files
file_paths = ['C:\\Users\\DeLL\\PycharmProjects\\blackCoffer\\exracted_texts\\' + filename for filename in os.listdir('C:\\Users\\DeLL\\PycharmProjects\\blackCoffer\\exracted_texts')]
# Change the file path to your actuall file path

# Step 2: Perform textual analysis and compute variables
data = []

for file_path in file_paths:
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Tokenize the text into words and sentences
    words = word_tokenize(text)
    sentences = sent_tokenize(text)

    # Compute variables
    word_count = len(words)
    sentence_count = len(sentences)
    avg_sentence_length = word_count / sentence_count

    # Calculate other variables based on the definitions provided in the "Text Analysis.docx" file
    # Example: Subjectivity Score using TextBlob library
    blob = TextBlob(text)
    subjectivity_score = blob.sentiment.subjectivity

    # Append computed variables to the data list
    data.append({
        'Word Count': word_count,
        'Sentence Count': sentence_count,
        'Average Sentence Length': avg_sentence_length,
        'Subjectivity Score': subjectivity_score,
        # Add other computed variables as needed
    })

# Step 3: Write computed variables to the output Excel file
output_df = pd.DataFrame(data)
output_df.to_excel('output_data.xlsx', index=False)
