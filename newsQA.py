import pandas as pd
import matplotlib.pyplot as plt

# Load NewsQA MRC dataset
data = pd.read_csv(r"E:\Muzamil Work\PHD Computer Science\My Submissions\QA MRC\DataSets\newsqa-data-v1\newsqa-data-v1.csv")

# Calculate word count for each document
word_count = [len(str(text).split(" ")) for text in data["question"]]

# Add word count as a column in the dataset
data["word_count"] = word_count

# Group by document and calculate the mean word count
grouped = data.groupby("story_id").mean()

# Plot bar graph of mean word count per document
plt.bar(grouped.index,  grouped["word_count"], bins=40, color='blue')
plt.xlabel("Document")
plt.ylabel("Word Count")
plt.title("Word Count in each Document of NewsQA MRC dataset")
plt.xticks(rotation=90)
plt.show()
