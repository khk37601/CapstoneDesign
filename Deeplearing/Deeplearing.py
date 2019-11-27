import pickle
from tensorflow.keras import models
from tensorflow.keras.models import load_model
from tensorflow.keras import layers
from tensorflow.keras import optimizers
from tensorflow.keras import losses
from tensorflow.keras import metrics
from tensorflow.keras.layers import Dense
import tensorflow as tf
from konlpy.tag import Okt
import numpy as np
import requests
import gensim
import pickle
import json
import nltk
import os


class InitModel(object):

    def __init__(self):
        self.data = None
        self.tokens = None
        self.selected_words = None
        # self.train_x = None
        # self.test_x = None
        # self.train_y = None
        # self.test_y = None
        self.train_docs = None
        self.test_docs = None
        self.train_data = self.read_data('C:/Users/khk37/OneDrive/Desktop/nsmc-master/ratings_train.txt')
        self.test_data = self.read_data('C:/Users/khk37/OneDrive/Desktop/nsmc-master/ratings_test.txt')
        self.okt = Okt()
        self.make_tokens()

    def read_data(self, filename):
        with open(filename, 'r', encoding='UTF8') as f:
            self.data = [line.split('\t') for line in f.read().splitlines()]
            # txt 파일의 헤더(id document label)는 제외하기
            self.data = self.data[1:]

        return self.data

    def tokenize(self, doc):
        # norm은 정규화, stem은 근어로 표시하기를 나타냄
        return ['/'.join(t) for t in self.okt.pos(doc, norm=True, stem=True)]

    def make_tokens(self):

        if os.path.isfile('train_docs.json'):
            with open('C:/Users/khk37/OneDrive/Desktop/nsmc-master/train_docs.json', encoding="utf-8") as f:
                self.train_docs = json.load(f)
            with open('C:/Users/khk37/OneDrive/Desktop/nsmc-master/test_docs.json', encoding="utf-8") as f:
                self.test_docs = json.load(f)
        else:

            self.train_docs = [(self.tokenize(row[1]), row[2]) for row in self.train_data]
            self.test_docs = [(self.tokenize(row[1]), row[2]) for row in self.test_data]
            # JSON 파일로 저장
            with open('train_docs.json', 'w', encoding="utf-8") as make_file:
                json.dump(self.train_docs, make_file, ensure_ascii=False, indent="\t")
            with open('test_docs.json', 'w', encoding="utf-8") as make_file:
                json.dump(self.test_docs, make_file, ensure_ascii=False, indent="\t")

        self.tokens = [t for d in self.train_docs for t in d[0]]
        print(self.tokens[:5])
        with open('tokens.txt', 'wb') as token_file:
            pickle.dump(self.tokens, token_file)

        self.text_common()

    def text_common(self):
        text = nltk.Text(self.tokens, name='NMSC')
        self.selected_words = [f[0] for f in text.vocab().most_common(10000)]

        self.make_data_set()

    def term_frequency(self, doc):
        return [doc.count(word) for word in self.selected_words]

    def make_data_set(self):

        train_x = [self.term_frequency(d) for d, _ in self.train_docs]
        test_x = [self.term_frequency(d) for d, _ in self.test_docs]
        train_y = [c for _, c in self.train_docs]
        test_y = [c for _, c in self.test_docs]

        self.model_learn(train_x, test_x, train_y, test_y)

    def model_learn(self, train_x, test_x, train_y, test_y):

        print(train_x)

        x_train = np.asarray(train_x).astype(' float32')
        x_test = np.asarray(test_x).astype('float32')
        y_train = np.asarray(train_y).astype('float32')
        y_test = np.asarray(test_y).astype('float32')

        # 모델 구성하기.

        model = models.Sequential()
        model.add(Dense(64, kernel_initializer='uniform', activation='relu', input_shape=(10000,)))
        model.add(Dense(64, kernel_initializer='uniform', activation='relu'))
        model.add(Dense(1, activation='sigmoid'))

        # 모델 학습과정 설정.
        model.compile(optimizer=optimizers.RMSprop(lr=0.001),
                      loss=losses.binary_crossentropy,
                      metrics=[metrics.binary_accuracy])

        # 모델 학습하기.
        history = model.fit(x_train, y_train, validation_data=(x_test, y_test), epochs=10,
                            batch_size=512)

        results = model.evaluate(x_test, y_test)

        print(results)
        # 모델 저장.
        model.save('emotional analysis.h5')



