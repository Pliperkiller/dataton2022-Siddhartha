import requests
import re
import nltk
import random
import pandas as pd
import numpy as np

from nltk import FreqDist
from nltk import word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.util import ngrams
from bs4 import BeautifulSoup
from urllib import request
from url_config import *
from utilitools import *
from matplotlib import pyplot as plt

# Esta función regresa los tokens del cuerpo de la noticia
def tokenizar_url(url):
    #Se envia solicitud a la página
    resultado=requests.get(url)

    #Se solicita el texo
    content=resultado.text
    soup=BeautifulSoup(content, 'lxml')
    #print(url)

    if 'espectador' in url.lower(): box = bs_espectador(soup)
    elif 'semana' in url.lower(): box = bs_semana(soup)
    elif 'larepublica' in url.lower(): box = bs_larepublica(soup)
    elif 'portafolio' in url.lower(): box = bs_portafolio(soup)
    elif 'elpais' in url.lower(): box = bs_elpais(soup)
    elif 'eltiempo' in url.lower(): box = bs_eltiempo(soup)
    elif 'infobae' in url.lower(): box = bs_infobae(soup)
    elif 'laopinion' in url.lower(): box = bs_laopinion(soup)
    elif 'redmas' in url.lower(): box = bs_redmas(soup)
    elif 'bloomberglinea' in url.lower(): box = bs_bloomberglinea(soup)
    elif 'elespanol' in url.lower(): box = bs_elespanol(soup)
    elif 'elcolombiano' in url.lower(): box = bs_elcolombiano(soup)
    elif 'cnn' in url.lower(): box = bs_cnn(soup)
    elif 'bbc' in url.lower(): box = bs_bbc(soup)

    else: return 'no config'

    tokenizer=RegexpTokenizer('\w+')
    tokens=tokenizer.tokenize(box)
    tokens=[token.lower() for token in tokens]

    return tokens