# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 12:22:44 2019

@author: khk37
"""
import tensorflow as tf
import gensim
#import tensorflow as tf
import json
import os
from konlpy.tag import Okt
from pprint import pprint
import requests
okt = Okt()


def read_data(filename):
    with open(filename, 'r', encoding='UTF8') as f:
        data = [line.split('\t') for line in f.read().splitlines()]
        # txt 파일의 헤더(id document label)는 제외하기
        data = data[1:]
    return data


train_data = read_data('C:/Users/khk37/OneDrive/Desktop/nsmc-master/ratings_train.txt')
test_data = read_data('C:/Users/khk37/OneDrive/Desktop/nsmc-master/ratings_test.txt')


def tokenize(doc):
    # norm은 정규화, stem은 근어로 표시하기를 나타냄
    return ['/'.join(t) for t in okt.pos(doc, norm=True, stem=True)]


#if os.path.isfile('train_docs.json'):
 #   with open('C:/Users/khk37/OneDrive/Desktop/nsmc-master/train_docs.json',encoding="utf-8") as f:
  #      train_docs = json.load(f)
   # with open('C:/Users/khk37/OneDrive/Desktop/nsmc-master/test_docs.json',encoding="utf-8") as f:
    #    test_docs = json.load(f)
#else:


train_docs = [(tokenize(row[1]), row[2]) for row in train_data]
test_docs = [(tokenize(row[1]), row[2]) for row in test_data]
# JSON 파일로 저장
with open('train_docs.json', 'w', encoding="utf-8") as make_file:
        json.dump(train_docs, make_file, ensure_ascii=False, indent="\t")
with open('test_docs.json', 'w', encoding="utf-8") as make_file:
        json.dump(test_docs, make_file, ensure_ascii=False, indent="\t")

tokens = [t for d in train_docs for t in d[0]]
import nltk
text = nltk.Text(tokens, name='NMSC')

selected_words = [f[0] for f in text.vocab().most_common(10000)]

def term_frequency(doc):
    return [doc.count(word) for word in selected_words]

train_x = [term_frequency(d) for d,_ in train_docs]
test_x = [term_frequency(d) for d,_ in test_docs]
train_y = [c for _,c in train_docs]
test_y = [c for _,c in test_docs]

import numpy as np
x_train = np.asarray(train_x).astype('float32')
x_test = np.asarray(test_x).astype('float32')
#np.int64(train_Y)
y_train = np.asarray(train_y).astype('float32')
#y_train = np.asarray(np.int64(train_y))
y_test = np.asarray(test_y).astype('float32')

from tensorflow.keras import models
from tensorflow.keras.models import load_model
from tensorflow.keras import layers
from tensorflow.keras import optimizers
from tensorflow.keras import losses
from tensorflow.keras import metrics
from tensorflow.keras.layers import Dense

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
history = model.fit(x_train, y_train, validation_data=(x_test, y_test), epochs=10, batch_size=512)
from selenium import webdriver
from bs4 import BeautifulSoup
from PIL import ImageGrab
import requests
import os
import subprocess
import time
from datetime import datetime
from selenium.common import exceptions
#import pandas as pd
import re
import random
import string
import pyautogui
from PIL import Image
from selenium.webdriver.common.keys import Keys
from tqdm import tqdm_notebook
from abc import *
import nltk
import numpy as np
from tensorflow.keras import models
from tensorflow.keras.models import load_model
from tensorflow.keras import layers
from tensorflow.keras import optimizers
from tensorflow.keras import losses
from tensorflow.keras import metrics
import json



class Text(object):

    def __init__(self, file_name):
        self.file_name = file_name

    def _write_text(self, text):
        # print(type(text))
        with open(self.file_name, 'a', encoding='utf8') as file:
            file.write(text + "\n")


class Parisng(object):

    def __init__(self):
        pass

    def parsing_html(self, source):
        soup = BeautifulSoup(source, "lxml")
        return soup

    def parsing(self, url):
        html = requests.get(url, headers=self.header)
        # 파싱
        soup = BeautifulSoup(html.content, "lxml")
        return soup


# Stting class
class Setting(object):

    def __init__(self):
        self.__options = webdriver.ChromeOptions()
        self.__options.add_argument('headless')
        self.__options.add_argument('window-size=1920x1080')
        self.__options.add_argument('--disable-gpu')
        self.__options.add_argument("lang=ko_KR")  # 한국어!
        self.__options.add_argument(
            "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
        self.__dirver = ""
        # dirver가 없는 경우.
        try:
            self.__driver = webdriver.Chrome('C:/Users/khk37/Downloads/chromedriver_win32 (2)/chromedriver')
        except:
            print("드라이브를 설치하거나 경로를 다시 설정 해주세요")
            # self.check_chrome_version()

    def get_driver(self):

        return self.__driver


# class LoadModel(metaclass=ABCMeta):
#   model = load_model('C:/Users/khk37/emotional analysis.h5')

bad = 0
good = 0


class DeepleringModel(object):

    def __init__(self):
        with open('C:/Users/khk37/OneDrive/Desktop/nsmc-master/train_docs.json', encoding="utf-8") as f:
            self.train_docs = json.load(f)

        self.model = load_model('C:/Users/khk37/emotional analysis.h5')
        self.text = nltk.Text(tokens, name='NMSC')
        self.tokens = [t for d in self.train_docs for t in d[0]]
        self.selected_words = [f[0] for f in self.text.vocab().most_common(10000)]

    def tokenize(self, doc):

        # norm은 정규화, stem은 근어로 표시하기를 나타냄
        return ['/'.join(t) for t in okt.pos(doc, norm=True, stem=True)]

    def term_frequencys(self, doc):
        return [doc.count(word) for word in self.selected_words]

    def predict_pos_neg(self, review):

        # 형태소 구별.
        token = self.tokenize(review)

        tf = self.term_frequencys(token)

        data = np.expand_dims(np.asarray(tf).astype('float32'), axis=0)

        score = float(self.model.predict(data))

        if (score > 0.5):
            global good
            print("[{}]는 {:.2f}% 확률로 긍정 리뷰이지 않을까 추측해봅니다.^^\n".format(review, score * 100))
            good += 1
            return ""

        else:
            global bad
            print("[{}]는 {:.2f}% 확률로 부정 리뷰이지 않을까 추측해봅니다.^^;\n".format(review, (1 - score) * 100))
            bad += 1
            return review


class Crawling(object):

    def __init__(self):
        self.header = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)\AppleWebKit 537.36 (KHTML, like Gecko) Chrome",
            "Accept": "text/html,application/xhtml+xml,application/xml;\
                        q=0.9,imgwebp,*/*;q=0.8"}

        # 설정된 크롬드라이브 가져오기.
        self.__driver = Setting().get_driver()

    def parsing_html(self, source):
        soup = BeautifulSoup(source, "lxml")
        return soup

    def parsing(self, url):
        html = requests.get(url, headers=self.header)
        # 파싱
        soup = BeautifulSoup(html.content, "lxml")
        return soup

    def Crawling_run_naver(self, start_date, end_date, keyword, sort):
        # 해당 사이트 주소 리스트
        self.href = []
        self.news_title = []
        self.company_name = []
        self.name_commpy = []
        self.select_user_company = []
        self.start_date = start_date
        self.end_date = end_date
        self.keyword = keyword
        self.page = 0

        # 접근 오류 해결하기 위함.
        requests.packages.urllib3.disable_warnings()
        page = 1
        s_from = self.start_date.replace(".", "")
        e_to = self.end_date.replace(".", "")
        # sort 0 : 관련도,  1 : 최신순 , 2 : 오래된

        max_page = (10 - 1) * 10 + 1
        process = tqdm_notebook(range(max_page))

        for i in process:

            process.set_description("페이지를 조회 하고 있습니다.")
            while page <= max_page:
                print("진행중임./...............")
                url = "https://search.naver.com/search.naver?where=news&query=" + keyword + "&sort=" + str(
                    sort) + "&ds=" + self.start_date + "&de=" + self.end_date + "&nso=so%3Ar%2Cp%3Afrom" + s_from + "to" + e_to + "%2Ca%3A&start=" + str(
                    page)

                soup = self.parsing(url)

                new_title = soup.select("._sp_each_url")

                company_names = soup.select("._sp_each_source")

                years = soup.select(".txt_inline")

                # 뉴스 기사 주소 수집
                for urls, name in zip(new_title, company_names):

                    self.href.append(urls['href'])
                    # self.news_title.append(urls['title'])
                    try:

                        # pattern = '\d+.(\d+).(\d+).'  # 정규표현식
                        # r = re.compile(pattern)
                        # match = r.search(year.text).group(0)

                        self.name_commpy.append(name.text.replace("언론사 선정", ""))

                        # Ecexl({name.text.replace("언론사 선정", ""), urls['href'], match}, 'justTT')

                    except Exception as e:
                        print(e)
                # continue

                # 네이버 페이지 전환 규칙
                page += 10

        process.set_description("페이지를 조회 완료.")
        self.collect_comment(keyword)

    def get_company_name(self):

        company_xpath = ['//*[@id="content"]/div[1]/div/div[1]/a/img', '//*[@id="main_content"]/div[1]/div[1]/a/img']
        company = ""

        for xpath in company_xpath:

            if self.__driver.find_elements_by_xpath(xpath):
                for i in self.__driver.find_elements_by_xpath(xpath):
                    company = i.get_attribute("alt")
                break

        return company

    def get_news_title(self, company, css_selector):
        news_title = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]', '',
                            self.__driver.find_element_by_css_selector(css_selector).text)
        collect_text = Text(company + '/' + news_title + ".txt")
        return collect_text

    def collect_comment(self, keyword):

        process = tqdm_notebook(self.href)
        Test = DeepleringModel()

        for news in process:
            process.set_description("댓글 수집 중입니다.")
            self.__driver.implicitly_wait(3)
            self.__driver.get(news)

            try:
                # 최초 더보기 버튼 클릭
                self.__driver.find_element_by_css_selector(".u_cbox_btn_view_comment").click()
                self.__driver.implicitly_wait(3)

            # 버튼의 유형이 다른 경우 발생
            except Exception as e:
                try:
                    self.__driver.find_element_by_css_selector(".simplecmt_link_text").click()
                    self.__driver.implicitly_wait(3)
                except:
                    continue

                # pass

            # 더보기 버튼 계속 누르기.

            # 뉴스 기사 및 회사이름 가져오기.
            company = self.get_company_name()


            collect_text = ""
            company = 'C:/Users/khk37/뉴스기사/' + keyword + company.strip()

            try:

                if not os.path.exists(company.strip()):
                    os.mkdir(company)

            except Exception as e:
                print("os.mkdir 에러", e)

            try:

                collect_text = self.get_news_title(company, '.end_tit')
            except:
                try:
                    collect_text = self.get_news_title(company, '.tts_head')

                except:
                    collect_text = self.get_news_title(company, '#articleTitle')

            try:

                # time.sleep(1.5)
                while True:
                    self.__driver.find_element_by_css_selector(".u_cbox_btn_more").click()

                    pyautogui.screenshot('C:/Users/khk37/OneDrive/Desktop/Test/' + company + ''.join(
                        random.choice(string.ascii_uppercase + string.digits) for _ in range(12)) + '.png')
                    self.__driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")


            except exceptions.ElementNotVisibleException as e:  # 페이지 끝

                pass

            except Exception as e:  # 다른 예외 발생시 확인
                self.page += 1
                print("에러 :  ", e)

            # document.body.scrollHeight
            # 스크롤 끝으로 올림.
            self.__driver.execute_script("window.scrollTo(0, 0);")
            soup = self.parsing_html(self.__driver.page_source)
            comment_list = soup.find_all("span", {"class": "u_cbox_contents"})
            last_height = self.__driver.execute_script("return document.body.scrollHeight")
            elem = self.__driver.find_element_by_tag_name("body")

            down = 0
            number = 1

            for comment in comment_list:
                collect_text._write_text(Test.predict_pos_neg(comment.text))

            self.page += 1

            process.set_description("댓글 수집 완료.")



if __name__ =='__main__':
    Crawling().Crawling_run_naver('2019.10.25','2019.10.26','설리','0')
