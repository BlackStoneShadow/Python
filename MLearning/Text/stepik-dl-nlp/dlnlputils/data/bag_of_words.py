import numpy as np
import scipy.sparse
import torch
from torch.utils.data import Dataset


def vectorize_texts(tokenized_texts, word2id, word2freq, mode='tfidf', scale=True):
    assert mode in {'tfidf', 'idf', 'tf', 'bin', 'pmi'}

    # считаем количество употреблений каждого слова в каждом документе
    result = scipy.sparse.dok_matrix((len(tokenized_texts), len(word2id)), dtype='float32')
    for text_i, text in enumerate(tokenized_texts):
        for token in text:
            if token in word2id:
                result[text_i, word2id[token]] += 1

    # получаем бинарные вектора "встречается или нет"
    if mode == 'bin':
        result = (result > 0).astype('float32')

    # получаем вектора относительных частот слова в документе
    elif mode == 'tf':
        result = result.tocsr()
        result = result.multiply(1 / result.sum(1))

    # полностью убираем информацию о количестве употреблений слова в данном документе,
    # но оставляем информацию о частотности слова в корпусе в целом
    elif mode == 'idf':
        result = (result > 0).astype('float32').multiply(1 / word2freq)

    # учитываем всю информацию, которая у нас есть:
    # частоту слова в документе и частоту слова в корпусе
    elif mode == 'tfidf':
        result = result.tocsr()
        result = result.multiply(1 / result.sum(1))  # разделить каждую строку на её длину
        result = result.multiply(1 / word2freq)  # разделить каждый столбец на вес слова

    # вычисляем Positive Pointwise Mutual Information (PPMI) между документом и словом
    elif mode == "pmi":
        result = result.tocsr()

        # N — общее количество токенов во всем исходном корпусе (сумма всех частот в word2freq)
        total_words = word2freq.sum()
        if total_words == 0:
            total_words = 1.0

        # P(d) — сумма по строкам (длина каждого документа в текущей матрице)
        sum_d = np.array(result.sum(axis=1)).flatten()
        sum_d[sum_d == 0] = 1.0  # избегаем деления на ноль

        # P(w) — сумма по столбцам (общая частота слова в текущей матрице)
        sum_w = word2freq.copy().astype("float32")
        sum_w[sum_w == 0] = 1.0
        
        # Считаем выражение под логарифмом:
        # 1. Делим каждую строку на sum_d
        result = result.multiply(1 / sum_d[:, None])
        # 2. Делим каждый столбец на глобальные частоты из word2freq
        result = result.multiply(1 / sum_w)
        # 3. Умножаем на N (total_words всего корпуса)
        result = result * total_words

        # Берем двоичный логарифм только от ненулевых элементов
        result.data = np.log2(result.data)

        # Применяем PPMI: заменяем отрицательные значения на 0
        result.data = np.maximum(result.data, 0)
        result.eliminate_zeros()
   
    if scale:
        result = result.tocsc()
        result -= result.min()
        result /= (result.max() + 1e-6)

    return result.tocsr()

class SparseFeaturesDataset(Dataset):
    def __init__(self, features, targets):
        self.features = features
        self.targets = targets

    def __len__(self):
        return self.features.shape[0]

    def __getitem__(self, idx):
        cur_features = torch.from_numpy(self.features[idx].toarray()[0]).float()
        cur_label = torch.from_numpy(np.asarray(self.targets[idx])).long()
        return cur_features, cur_label
