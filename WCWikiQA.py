import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
dataset = pd.read_csv(r"E:\Muzamil Work\PHD Computer Science\My Submissions\QA MRC\DataSets\WikiQACorpus\WikiQA-train.tsv", sep='\t')

# Create a list to store the word count for each document
word_count = []

# Loop through the rows of the dataset and count the number of words in each document
for i in range(len(dataset)):
    words = dataset.iloc[i]['Sentence']
    word_count.append(len(words.split()))

# Plot the graph
plt.hist(word_count, bins=50, color="Red")
plt.xlabel("Passage Word Count")
plt.ylabel("Frequency")

plt.show()
