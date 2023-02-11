import csv
import matplotlib.pyplot as plt

# read the csv file
with open(r"E:\Muzamil Work\PHD Computer Science\My Submissions\QA MRC\DataSets\newsqa-data-v1\newsqa-data-v1.csv", encoding= "utf-8") as f:
    reader = csv.reader(f)
    header = next(reader)
    
    word_count = []
    for row in reader:
        # extract the document text and count the number of words
        text = row[0]
        print(text)
        count = len(text.split())
        word_count.append(count)
        
# plot the histogram
plt.hist(word_count, bins=50, color='red')
plt.xlabel('Document Word Count')
plt.ylabel('Frequency')
plt.show()
