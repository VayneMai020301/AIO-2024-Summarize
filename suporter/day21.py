import numpy as np
import matplotlib.pyplot as plt



corpus = ["Tôi thích học AI", "AI là trí tuệ nhân tạo",
             "AGI là siêu trí tuệ nhân tạo"]

def plot(matrix):
    plt.imshow(matrix, cmap='viridis', interpolation='nearest')
    plt.colorbar() 
    plt.grid(False)  # Thêm thanh màu
    plt.show()

def get_vocab_from_corpus(corpus : list[str]) -> list:
    """
        * Return vocabs from corpus
    """
    vocabs = list()
    for doc in corpus:
        vocabs.extend(doc.split())
        
    unique_vocabs = list(set(vocabs))
    sorted_list = sorted(unique_vocabs)
    return sorted_list

def get_term_frequency(corpus: list[str]) -> np.ndarray:
    """
        * Return term_frequency with Input is Corpus
    """
    vocabs = get_vocab_from_corpus(corpus)
    term_frequency = np.zeros((len(corpus), len(vocabs)))
    for i, doc in enumerate(corpus):
        for word in doc.split():
            term_frequency[i, list(vocabs).index(word)] += 1
    term_frequency /= term_frequency.sum(axis=1, keepdims=True  ) 
    return term_frequency

def get_inverse_document_frequency(corpus: list[str])-> np.array:
    """
        * Return Inverse Document Frequency from corpus
    """
    vocabs = get_vocab_from_corpus(corpus)
    idf = np.zeros(len(vocabs))
    for i, word in enumerate(vocabs):
        idf[i] = np.log(len(corpus) / (1 + sum([word in doc for doc in corpus])))
    
    return idf


def get_metrix(corpus: list[str]) -> np.ndarray: return get_term_frequency(corpus) * get_inverse_document_frequency(corpus)


if __name__ =="__main__":

    print(f"*************** Vocab from corpus:\n {get_vocab_from_corpus(corpus)}\n")
    print(f"*************** Term Frequency:\n {get_term_frequency(corpus)}\n")
    print(f"*************** Inverse Document Frequency:\n {get_term_frequency(corpus)}\n")

    print(f"*************** TF-IDF Matrix \n {get_metrix(corpus)}\n")

    plot(get_metrix(corpus))
