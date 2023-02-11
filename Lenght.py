import json
import matplotlib.pyplot as plt

def word_count(document):
    return len(document.split())

def length_analysis(dataset):
    lengths = []
    for article in dataset['data']:
        for paragraph in article['paragraphs']:
            text = paragraph['context']
            lengths.append(word_count(text))
    return lengths

# Load the SQuAD dataset
with open(r"E:\Muzamil Work\PHD Computer Science\My Submissions\QA MRC\DataSets\SQuAD 2\dev-v2.0.json") as f:
    dataset = json.load(f)

# Calculate the length of each document in the dataset
lengths = length_analysis(dataset)

# Generate a bar graph to visualize the results
plt.hist(lengths, bins=50)
plt.xlabel("Document Length (Number of Words)")
plt.ylabel("Frequency")
plt.title("Length Analysis of Documents in the SQuAD Dataset")
plt.show()
