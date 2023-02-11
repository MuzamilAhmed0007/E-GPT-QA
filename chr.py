import json
import matplotlib.pyplot as plt

# load SQuAD MRC dataset
with open(r"C:\Users\muzam\Downloads\SQuAD-v1.1.json", "r") as f:
    squad_data = json.load(f)

# initialize list to store character counts
char_counts = []

# iterate through each instance in the dataset
for instance in squad_data["data"]:
    for paragraph in instance["paragraphs"]:
        text = paragraph["context"]
        char_counts.append(len(text))

# calculate average character count
average_char_count = sum(char_counts) / len(char_counts)
#print("Average character count:", average_char_count)

# draw histogram of character counts
plt.hist(char_counts, bins=40, color="Orange")
plt.xlabel("Character Count")
plt.ylabel("Frequency")
x = "Avg Char Count:"+str(average_char_count.__round__(2))
plt.legend([x])
plt.show()
