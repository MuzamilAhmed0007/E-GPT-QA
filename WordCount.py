import json
import matplotlib.pyplot as plt

def count_words(sentence):
    return len(sentence.split())

def generate_word_count_graph(data):
    question_word_counts = []
    document_word_counts = []

    for article in data['data']:
        for paragraph in article['paragraphs']:
            document_word_counts.append(count_words(paragraph['context']))
            for qa in paragraph['qas']:
                question_word_counts.append(count_words(qa['question']))

    plt.hist([document_word_counts], bins=20, color="Red", alpha= 0.5)
    plt.legend()
    plt.xlabel('Document Word Count')
    plt.ylabel('Frequency')
    plt.show()

with open(r"E:\Muzamil Work\PHD Computer Science\My Submissions\QA MRC\DataSets\SQuAD 2\train-v2.0.json") as f:
    data = json.load(f)
    generate_word_count_graph(data)
