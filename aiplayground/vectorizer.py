# -*- coding: utf-8 -*-
from sklearn.feature_extraction.text import HashingVectorizer
import re
import sys
import logging
logger = logging.getLogger(__name__)


def get_stopwords(stopwords):
    logger.info(sys._getframe().f_code.co_name)
    global stop
    stop = stopwords
    return HashingVectorizer(decode_error='ignore',n_features=2**21,preprocessor=None,tokenizer=tokenizer)


def tokenizer(text):
    logger.info(sys._getframe().f_code.co_name)
    text = re.sub('<[^>]*>', '', text)
    emoticons = re.findall('(?::|;|=)(?:-)?(?:\)|\(|D|P)',
                           text.lower())
    text = re.sub('[\W]+', ' ', text.lower()) \
                   + ' '.join(emoticons).replace('-', '')
    tokenized = [w for w in text.split() if w not in stop]
    return tokenized
