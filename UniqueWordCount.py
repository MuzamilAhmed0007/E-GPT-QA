import json
import matplotlib.pyplot as plt

def unique_word_count(file):
    with open(file) as f:
        data = json.load(f)
    word_count = {}
    for doc in data['data']:
        for para in doc['paragraphs']:
            words = para['context'].split()
            for word in set(words):
                if word not in word_count:
                    word_count[word] = 1
                else:
                    word_count[word] += 1
    return word_count

def generate_bar_graph(word_count):
    plt.bar(word_count.keys(), word_count.values(), color='blue')
    plt.xlabel("Words")
    plt.ylabel("Count")
    plt.title("Unique Word Count")
    plt.show()

word_count = unique_word_count(r"E:\Muzamil Work\PHD Computer Science\My Submissions\QA MRC\DataSets\SQuAD 2\train-v2.0.json")
generate_bar_graph(word_count)
