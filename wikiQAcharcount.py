import pandas as pd
import matplotlib.pyplot as plt

# Read the dataset into a pandas dataframe
df = pd.read_csv(r"E:\Muzamil Work\PHD Computer Science\My Submissions\QA MRC\DataSets\WikiQACorpus\WikiQA-train.tsv", sep='\t')
print(df.head())
# Calculate the average character count for each document
df['doc_len'] = df['Sentence'].apply(lambda x: len(x))
avg_char_count = df['doc_len'].mean()

print("Average character count in the document:", avg_char_count)

# Plot a histogram of the document length
plt.hist(df['doc_len'], bins=40, color="Orange")
plt.xlabel('Character Count')
plt.ylabel('Frequency')
x = "Avg Char Count:"+str(avg_char_count.__round__(2))
plt.legend([x])
plt.show()

