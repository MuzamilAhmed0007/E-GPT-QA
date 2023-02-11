import json
import matplotlib.pyplot as plt

# Load the SQuAD MRC dataset
with open(r"E:\Muzamil Work\PHD Computer Science\My Submissions\QA MRC\DataSets\SQuAD 2\dev-v2.0.json", "r") as f:
    squad_data = json.load(f)

# Calculate the average character count for each article in the dataset
average_char_counts = []
for article in squad_data["data"]:
    char_count = 0
    for paragraph in article["paragraphs"]:
        char_count += len(paragraph["context"])
    average_char_counts.append(char_count / len(article["paragraphs"]))

# Plot the results using a bar graph
plt.bar(range(len(average_char_counts)), average_char_counts)
plt.xlabel("Article Index")
plt.ylabel("Average Character Count")
plt.title("Average Character Count per Article in SQuAD MRC Dataset")
plt.show()
